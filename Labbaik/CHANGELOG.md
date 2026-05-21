# Changelog

All notable changes to the Labbaik project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- **Map Feature**
  - Full-screen interactive Google Maps integration
  - Search bar with location labels (Al Muqayti, AL'USAYLAH)
  - Category filter buttons (Mosques, Ritual Sites, Historic Sites, Museums, Hotels)
  - Multiple location markers for important sites (Kaaba, Thour Cave, Mina, Muzdalifa, Wadi Jalil, Batha Quraish)
  - Compass/navigation button for map centering
  - Location info windows with localized names
  - Map tab content widget with reusable components

- **Home Dashboard Feature**
  - Prayer times integration with real-time updates
  - Location-based prayer time calculation
  - Prayer schedule card with current and upcoming prayers
  - Date and location display with Hijri calendar
  - Home drawer with navigation options
  - Custom bottom navigation bar
  - Shimmer loading effects for better UX

- **Umrah Guidance Feature**
  - Step-by-step Umrah guide (Ihram, Tawaf, Saee, Tahallul)
  - Interactive step cards with status indicators
  - Detailed step instructions screen
  - Progress tracking through Umrah journey
  - SVG icon support for visual guidance

- **Enhanced Authentication**
  - Email verification screen with OTP support using Pinput
  - Password reset functionality with verification
  - Password change success confirmation
  - User profile screen with editable information
  - Country code picker for international users
  - Password validation stepper with strength indicators
  - Fancy password field for enhanced security

- **Settings & Profile Management**
  - Comprehensive settings screen
  - Theme switching (Light, Dark, System)
  - Language selection with RTL support
  - Location services toggle
  - User profile management
  - Contact information settings
  - Technical support options

- **UI Enhancements**
  - SVG image support with flutter_svg
  - Shimmer loading animations
  - Showcase views for feature discovery
  - Iconsax icon library integration
  - Custom app headers and navigation
  - Theme toggle widgets
  - Responsive design improvements

- **Assets & Localization**
  - New icon set for features (calendar, location, dark mode, etc.)
  - SVG illustrations for home, chat, map, and more
  - Enhanced Lottie animations (not-found states)
  - Updated localization files with new strings
  - Full RTL support for Arabic interface
  - Map-related localization strings (search, category filters, location names)

- **Authentication Architecture**
  - AuthService for centralized Firebase authentication operations
  - AuthErrorLocalizer utility for localizing authentication error messages
  - LoadingButton reusable widget with loading state support
  - SplashScreen with authentication state checking and navigation

### Changed
- Enhanced theme system with light, dark, and system modes
- Improved color utilities and validators
- Updated path utilities for asset management
- Enhanced app configuration with provider updates
- Improved router configuration with new routes
- Refactored AuthProvider to use AuthService following repository pattern
- Updated UserModel with improved type safety and date handling
- Updated auth screens to use new service layer architecture
- Updated localization files with authentication error messages
- Updated provider configuration for better state management
- Updated locale service implementation
- Redesigned map interface to match design specifications
- Updated home screen to display map in full-screen mode without header when on map tab
- Improved map zoom level to show wider Makkah region view

### Fixed
- Google Maps crash on iOS by adding proper SDK initialization in AppDelegate.swift
- Map initialization error that occurred when opening maps tab
- Missing Google Maps API key configuration for iOS platform

### Removed
- UserProvider (consolidated into AuthProvider)
- Bottom info bar from map tab (replaced with full-screen map design)

### Technical Improvements
- Initial project setup with Flutter architecture
- Internationalization support (English and Arabic)
- Firebase integration (Cloud Messaging, Crashlytics, Firestore, Remote Config, Database)
- Navigation system using go_router with declarative routing
- Network layer with Dio for API calls
- Responsive UI using flutter_screenutil
- Image picker and gallery functionality
- Location services integration with permission handling
- Push notifications support
- Rich text editor with flutter_quill
- Lottie animations support
- Offline caching with SharedPreferences
- Permission handling with permission_handler

## [1.0.0] - 2025-01-01

### Added
- Initial release of Labbaik application
- Hajj and Umrah guidance platform
- User authentication and registration
- Multi-language support
- Dark and light theme modes
- Firebase backend integration
- Push notification support
- Location-based services
- Media support (images, videos)
- Rich text content support
- Offline capabilities

### Features
- Authentication flow (Login, Sign Up, Forgot Password)
- Bilingual support (English, Arabic)
- Theme switching and persistence
- Firebase Cloud Messaging for notifications
- Geolocation services
- Image and video picker
- Rich text editor for content creation
- Responsive design for multiple screen sizes
- Lottie animations for better UX

---

## Version History

### Version 1.0.0 (Initial Release - January 2025)
- Initial project setup
- Core features implementation
- Basic authentication
- Internationalization setup
- Theme system
- Firebase integration

### Future Releases
- Enhanced Hajj guidance features
- Companion management system
- Real-time chat support
- Enhanced map integration
- Additional language support

---

## Types of Changes

- **Added** - New features
- **Changed** - Changes in existing functionality
- **Deprecated** - Soon-to-be removed features
- **Removed** - Removed features
- **Fixed** - Bug fixes
- **Security** - Vulnerability fixes

---

*For detailed commit history, please refer to the Git history.*

