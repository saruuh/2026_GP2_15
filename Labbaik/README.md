# Labbaik

A Flutter mobile application for Hajj and Umrah pilgrims providing personalized guidance throughout their spiritual journey.

## 📱 About

Labbaik is a comprehensive mobile application designed to guide pilgrims through their Hajj and Umrah experience with personalized assistance, video content, and essential information.

### Key Features

- 🔐 **Authentication System** - Secure login, registration, email verification, and password recovery
- 🏠 **Home Dashboard** - Prayer times integration with location-based services
- 🕋 **Umrah Guidance** - Step-by-step guide through Ihram, Tawaf, Saee, and Tahallul
- 👤 **User Profile** - Comprehensive profile management with country selection
- ⚙️ **Settings** - Theme switching, language selection, location services, and app preferences
- 📱 **Cross-platform** - iOS and Android support
- 🌍 **Internationalization** - English and Arabic language support with RTL support
- 🎨 **Theme Support** - Light, dark, and system theme modes with persistence
- 🔔 **Push Notifications** - Firebase Cloud Messaging integration
- 🌐 **Network Layer** - Robust API connectivity with Dio
- 💾 **Offline Caching** - Local data persistence with SharedPreferences
- 📍 **Geolocation** - Location-based services with permission handling
- 🎬 **Video Content** - Rich media support with thumbnail generation
- 🖼️ **Image/Gallery** - Media picker and album management
- 📝 **Rich Text Editor** - Quill editor integration
- 🎨 **Animated UI** - Lottie animations with shimmer loading effects
- 🔒 **Password Validation** - Real-time password strength indicator with stepper

## 🏗️ Architecture

The app follows a clean architecture pattern with:

- **Core Layer**: Configurations, utilities, widgets, and services
- **Features Layer**: Feature-specific modules (Auth, etc.)
- **Router Layer**: Navigation and routing management
- **Provider**: State management using the Provider pattern

## 🚀 Getting Started

### Prerequisites

- Flutter SDK (>=3.9.2)
- Dart SDK
- Firebase project configured
- iOS development requires Xcode
- Android development requires Android Studio

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd labbaik
```

2. Install dependencies:
```bash
flutter pub get
```

3. Configure Firebase:
   - Ensure `google-services.json` is in `android/app/`
   - Ensure `GoogleService-Info.plist` is in `ios/Runner/`

4. Run the app:
```bash
flutter run
```

## 📁 Project Structure

```
lib/
├── app/              # Main app configuration
├── core/             # Core utilities and services
│   ├── config/       # Provider and app configuration
│   ├── enums/        # Application enums
│   ├── error/        # Error handling
│   ├── instances/     # Dependency injection
│   ├── logs/          # Logging utilities
│   ├── network/       # Network layer and API
│   ├── resources/     # Colors, themes, constants
│   ├── services/       # Business logic services (ThemeService, etc.)
│   ├── use_cases/     # Use case implementations
│   ├── utilities/     # Helper functions (color, path, validators)
│   └── widgets/       # Reusable widgets (theme toggles, headers)
├── features/          # Feature modules
│   ├── auth/          # Authentication feature
│   │   ├── controller/  # Auth providers
│   │   ├── model/       # User model
│   │   ├── presentation/ # Auth screens (profile, settings, password reset)
│   │   └── provider/     # User state provider
│   ├── home/          # Home and prayer times feature
│   │   ├── controller/  # Prayer times provider
│   │   ├── model/       # Prayer times model
│   │   ├── presentation/ # Home screen with drawer, navigation
│   │   └── service/     # Prayer times service
│   └── umrah/         # Umrah guidance feature
│       └── presentation/ # Umrah guidance and step details screens
├── generated/          # Generated files
│   └── intl/          # Internationalization
├── l10n/              # Localization files (AR and EN)
├── router/            # Navigation and routing configuration
└── main.dart          # App entry point
```

## 🎨 Theme System

The app supports both light and dark themes with automatic switching. See [THEME_GUIDE.md](THEME_GUIDE.md) for detailed documentation.

## 📦 Key Dependencies

- **go_router**: Declarative routing for Flutter
- **firebase_core**: Firebase integration
- **firebase_messaging**: Push notifications
- **cloud_firestore**: Cloud database
- **firebase_crashlytics**: Crash reporting
- **firebase_remote_config**: Remote configuration
- **provider**: State management
- **dio**: HTTP client
- **flutter_screenutil**: Responsive UI
- **flutter_quill**: Rich text editor
- **geolocator**: Location services
- **permission_handler**: Permission management
- **shared_preferences**: Local storage persistence
- **flutter_svg**: SVG image support
- **country_code_picker**: Phone country code selection
- **pinput**: PIN input widget for OTP
- **fancy_password_field**: Advanced password input
- **shimmer**: Loading skeleton animations
- **showcaseview**: Feature discovery and onboarding
- **iconsax**: Modern icon library
- **lottie**: Animation support

## 🌐 Internationalization

The app supports multiple languages through the `flutter_intl` package:
- English (en) - Default
- Arabic (ar) - Full RTL support

Localization files are maintained in `lib/l10n/` directory.

## 🔧 Development

### Running Tests

```bash
flutter test
```

### Building for Production

**Android:**
```bash
flutter build apk --release
```

**iOS:**
```bash
flutter build ios --release
```

## 📄 License

© 2025 Labbaik. All rights reserved.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Contact

For support and inquiries, please contact the development team.
