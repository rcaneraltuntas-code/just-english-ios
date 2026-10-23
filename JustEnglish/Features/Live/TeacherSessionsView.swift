import SwiftUI
import JECore

/// Öğretmenin canlı derslerini açtığı, düzenlediği ve katılımcıları gördüğü ekran.
struct TeacherSessionsView: View {
    @Environment(AppModel.self) private var model
    @Environment(LiveSessionStore.self) private var liveStore
    @State private var store = TeacherStore()
    @State private var editing: EditorRoute?
    @State private var broadcasting: TeacherStore.Session?

    var body: some View {
        List {
            let startable = store.sessions.filter(\.canBroadcast)
            if !startable.isEmpty {
                Section("Şimdi") {
                    ForEach(startable) { session in
                        Button { broadcasting = session } label: {
                            Label("Yayını başlat: \(session.title)", systemImage: "video.fill")
                        }
                        .buttonStyle(PrimaryButtonStyle(color: Theme.brandRed))
                        .listRowBackground(Color.clear)
                        .listRowInsets(EdgeInsets(top: 4, leading: 0, bottom: 4, trailing: 0))
                    }
                }
            }
            if store.sessions.isEmpty && !store.isLoading {
                ContentUnavailableView("Henüz dersiniz yok", systemImage: "calendar.badge.plus",
                                       description: Text("Sağ üstteki + ile ilk canlı dersinizi açın. Ders, seçtiğiniz seviyedeki öğrencilere görünür."))
            }
            ForEach(store.sessions) { session in
                NavigationLink {
                    AttendeesView(session: session, store: store)
                } label: {
                    VStack(alignment: .leading, spacing: 4) {
                        HStack {
                            LevelBadge(level: session.level)
                            Text(session.startsAt.formatted(.dateTime.weekday(.abbreviated).day().month().hour().minute()))
                                .font(.jakarta(.footnote, weight: .semibold))
                                .foregroundStyle(.secondary)
                            if session.cancelled {
                                Text("İptal").font(.jakarta(.caption, weight: .bold)).foregroundStyle(Theme.danger)
                            }
                        }
                        Text(session.title).font(.jakarta(.headline)).strikethrough(session.cancelled)
                        Text(model.library?.unit(id: session.unitID).map { "Ünite \($0.number): \($0.title)" } ?? session.unitID)
                            .font(.jakarta(.footnote))
                            .foregroundStyle(.secondary)
                    }
                }
                .swipeActions {
                    if !session.cancelled {
                        Button("Düzenle") { editing = EditorRoute(session: session) }.tint(Theme.accent)
                        Button("İptal et", role: .destructive) { Task { await store.cancel(session); await liveStore.refresh() } }
                    }
                }
            }
        }
        .tabBarSpacer()
        .navigationTitle("Derslerim")
        .toolbar {
            Button { editing = EditorRoute(session: nil) } label: { Image(systemName: "plus") }
                .accessibilityLabel("Yeni ders")
        }
        .refreshable { await store.refresh() }
        .task { await store.refresh() }
        .fullScreenCover(item: $broadcasting, onDismiss: { Task { await store.refresh(); await liveStore.refresh() } }) { session in
            LiveRoomView(sessionID: session.id, title: session.title)
        }
        .sheet(item: $editing) { route in
            SessionEditorView(store: store, session: route.session) { Task { await liveStore.refresh() } }
        }
        .alert(store.error ?? "", isPresented: Binding(get: { store.error != nil }, set: { if !$0 { store.error = nil } })) {
            Button("Tamam", role: .cancel) {}
        }
    }

    struct EditorRoute: Identifiable {
        let session: TeacherStore.Session?
        var id: String { session?.id.uuidString ?? "new" }
    }
}

struct SessionEditorView: View {
    let store: TeacherStore
    let session: TeacherStore.Session?
    let onSaved: () -> Void

    @Environment(AppModel.self) private var model
    @Environment(\.dismiss) private var dismiss

    @State private var level: CEFRLevel = .a1
    @State private var unitID = ""
    @State private var title = ""
    @State private var startsAt = Calendar.current.date(byAdding: .day, value: 1, to: .now) ?? .now
    @State private var duration = 45
    @State private var teacherName = ""
    @State private var joinURL = ""
    @State private var limitSeats = true
    @State private var capacity = 12
    @State private var saving = false
    @State private var loaded = false

    private var units: [CourseUnit] { model.units(for: level) }
    private var selectedUnit: CourseUnit? { units.first { $0.id == unitID } }
    private var validURL: Bool {
        joinURL.isEmpty || (URL(string: joinURL)?.scheme?.hasPrefix("http") == true)
    }
    private var canSave: Bool {
        selectedUnit != nil && !title.trimmingCharacters(in: .whitespaces).isEmpty
            && !teacherName.trimmingCharacters(in: .whitespaces).isEmpty && validURL && !saving
    }

    var body: some View {
        NavigationStack {
            Form {
                Section("Ünite") {
                    Picker("Seviye", selection: $level) {
                        ForEach(CEFRLevel.allCases) { Text("\($0.rawValue) · \($0.title)").tag($0) }
                    }
                    Picker("Ünite", selection: $unitID) {
                        ForEach(units) { Text("\($0.number). \($0.title)").tag($0.id) }
                    }
                    if let unit = selectedUnit {
                        Text(unit.liveClass.goal).font(.jakarta(.footnote)).foregroundStyle(.secondary)
                    }
                }
                Section("Ders") {
                    TextField("Başlık", text: $title)
                    DatePicker("Tarih ve saat", selection: $startsAt, in: Date.now..., displayedComponents: [.date, .hourAndMinute])
                    Stepper("Süre: \(duration) dk", value: $duration, in: 15...180, step: 15)
                    TextField("Öğretmen adı", text: $teacherName).textContentType(.name)
                }
                Section {
                    TextField("https://…", text: $joinURL)
                        .keyboardType(.URL)
                        .textInputAutocapitalization(.never)
                        .autocorrectionDisabled()
                    if !validURL {
                        Text("Bağlantı https:// ile başlamalı.").font(.jakarta(.footnote)).foregroundStyle(Theme.danger)
                    }
                } header: {
                    Text("Harici toplantı bağlantısı (isteğe bağlı)")
                } footer: {
                    Text("Boş bırakın: ders uygulamanın içinde canlı yayınlanır, ders saatinde Derslerim ekranından \"Yayını başlat\"a dokunursunuz. Zoom, Meet ya da Teams kullanmak isterseniz bağlantıyı buraya yazın.")
                }
                Section("Kontenjan") {
                    Toggle("Kontenjan sınırı", isOn: $limitSeats)
                    if limitSeats { Stepper("\(capacity) öğrenci", value: $capacity, in: 1...300) }
                }
            }
            .navigationTitle(session == nil ? "Yeni canlı ders" : "Dersi düzenle")
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .cancellationAction) { Button("Vazgeç") { dismiss() } }
                ToolbarItem(placement: .confirmationAction) {
                    Button("Kaydet") { Task { await save() } }.disabled(!canSave)
                }
            }
            .onAppear(perform: load)
            .onChange(of: level) { _, _ in
                if selectedUnit == nil { unitID = units.first?.id ?? "" }
            }
            .onChange(of: unitID) { old, _ in
                // Başlık boşsa ya da önceki ünitenin önerisiyse yeni ünitenin ders planı başlığı önerilir.
                let previous = model.library?.unit(id: old)?.liveClass.title
                if let unit = selectedUnit, title.isEmpty || title == previous {
                    title = unit.liveClass.title
                    duration = unit.liveClass.durationMinutes
                }
            }
        }
    }

    private func load() {
        guard !loaded else { return }
        loaded = true
        if let session {
            level = session.level
            unitID = session.unitID
            title = session.title
            startsAt = session.startsAt
            duration = session.durationMinutes
            teacherName = session.teacherName
            joinURL = session.joinURL ?? ""
            limitSeats = session.capacity != nil
            capacity = session.capacity ?? 12
        } else {
            level = model.state.currentLevel
            unitID = model.units(for: level).first?.id ?? ""
            teacherName = model.state.name
            if let unit = model.library?.unit(id: unitID) {
                title = unit.liveClass.title
                duration = unit.liveClass.durationMinutes
            }
        }
    }

    private func save() async {
        saving = true
        let link = joinURL.trimmingCharacters(in: .whitespaces)
        let draft = TeacherStore.Draft(unitID: unitID, level: level, title: title.trimmingCharacters(in: .whitespaces),
                                       startsAt: startsAt, durationMinutes: duration,
                                       teacherName: teacherName.trimmingCharacters(in: .whitespaces),
                                       joinURL: link.isEmpty ? nil : link, capacity: limitSeats ? capacity : nil)
        if await store.save(draft, editing: session?.id) {
            onSaved()
            dismiss()
        }
        saving = false
    }
}

struct AttendeesView: View {
    let session: TeacherStore.Session
    let store: TeacherStore

    @State private var attendees: [TeacherStore.Attendee] = []
    @State private var loaded = false
    @State private var broadcasting = false

    var body: some View {
        List {
            if session.canBroadcast && !session.cancelled {
                Section {
                    Button { broadcasting = true } label: {
                        Label("Yayını başlat", systemImage: "video.fill")
                    }
                    .buttonStyle(PrimaryButtonStyle(color: Theme.brandRed))
                    .listRowBackground(Color.clear)
                    .listRowInsets(EdgeInsets())
                } footer: {
                    Text("Kayıtlı öğrenciler derse uygulamanın içinden katılır. Yayın dersten 30 dakika önce açılabilir.")
                }
            }
            Section {
                LabeledContent("Tarih", value: session.startsAt.formatted(date: .long, time: .shortened))
                LabeledContent("Süre", value: "\(session.durationMinutes) dk")
                LabeledContent("Kayıtlı", value: session.capacity.map { "\(attendees.count)/\($0)" } ?? "\(attendees.count)")
                if let link = session.joinURL, let url = URL(string: link) {
                    Link("Toplantıyı aç", destination: url)
                }
            }
            Section("Öğrenciler") {
                if loaded && attendees.isEmpty {
                    Text("Henüz kayıt yok.").foregroundStyle(.secondary)
                }
                ForEach(attendees) { attendee in
                    HStack {
                        Text(attendee.displayName)
                        Spacer()
                        if attendee.attended {
                            Label("Katıldı", systemImage: "checkmark.circle.fill")
                                .labelStyle(.titleAndIcon)
                                .font(.jakarta(.footnote))
                                .foregroundStyle(Theme.success)
                        }
                    }
                }
            }
        }
        .tabBarSpacer()
        .navigationTitle(session.title)
        .navigationBarTitleDisplayMode(.inline)
        .task {
            attendees = await store.attendees(of: session)
            loaded = true
        }
        .refreshable { attendees = await store.attendees(of: session) }
        .fullScreenCover(isPresented: $broadcasting, onDismiss: { Task { attendees = await store.attendees(of: session) } }) {
            LiveRoomView(sessionID: session.id, title: session.title)
        }
    }
}
