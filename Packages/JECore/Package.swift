// swift-tools-version:5.10
import PackageDescription

// Uygulamanın platformdan bağımsız öğrenme mantığı: seviye tespiti,
// aralıklı tekrar (FSRS) ve seri/XP hesapları. UI veya ağ kodu içermez,
// böylece `swift test` ile tek başına test edilebilir.
let package = Package(
    name: "JECore",
    platforms: [.iOS(.v17), .macOS(.v14)],
    products: [
        .library(name: "JECore", targets: ["JECore"]),
    ],
    targets: [
        .target(name: "JECore"),
        .testTarget(name: "JECoreTests", dependencies: ["JECore"]),
    ]
)
