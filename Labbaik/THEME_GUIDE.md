# 🎨 Theme System Guide

This guide explains how to use the comprehensive light and dark theme system implemented in your Labbaik Flutter app.

## 📋 Overview

The app now supports:
- ✅ **Light Theme** - Clean, bright interface matching your UI designs
- ✅ **Dark Theme** - Dark mode with proper contrast and readability
- ✅ **System Theme** - Automatically follows device theme settings
- ✅ **Theme Persistence** - Remembers user's theme preference
- ✅ **Easy Theme Switching** - Multiple ways to switch themes

## 🏗️ Architecture

### Core Files

1. **`lib/core/resources/app_colors.dart`**
   - Contains all color definitions
   - `LightThemeColors` class for light theme colors
   - `DarkThemeColors` class for dark theme colors
   - `AppColors` class for shared colors (primary, secondary, etc.)

2. **`lib/core/resources/app_theme.dart`**
   - `getLightTheme()` - Returns complete light theme
   - `getDarkTheme()` - Returns complete dark theme
   - `getApplicationTheme()` - Backward compatibility (returns light theme)

3. **`lib/core/services/theme_service.dart`**
   - `ThemeService` class manages theme state
   - Handles theme persistence with SharedPreferences
   - Provides methods to switch themes

4. **`lib/core/widgets/theme_toggle_widget.dart`**
   - Ready-to-use theme switching widgets
   - `ThemeToggleWidget` - Full theme selector
   - `ThemeToggleButton` - Simple toggle button
   - `ThemeCycleButton` - Cycles through all modes

## 🚀 Usage

### Basic Setup

The app is already configured to use both themes. The `MaterialApp.router` in `lib/app/app.dart` includes:

```dart
theme: getLightTheme(),
darkTheme: getDarkTheme(),
themeMode: _themeService.themeMode, // Automatically managed
```

### Theme Service Usage

```dart
// Create theme service instance
final themeService = ThemeService();

// Initialize (loads saved preference)
await themeService.init();

// Switch to specific theme
await themeService.setThemeMode(ThemeMode.light);
await themeService.setThemeMode(ThemeMode.dark);
await themeService.setThemeMode(ThemeMode.system);

// Toggle between light and dark
await themeService.toggleTheme();

// Cycle through all modes
await themeService.cycleTheme();

// Check current state
bool isDark = themeService.isDarkMode;
bool isLight = themeService.isLightMode;
bool isSystem = themeService.isSystemMode;
```

### Adding Theme Widgets to Your Screens

#### 1. Simple Toggle Button (for App Bar)

```dart
AppBar(
  title: Text('Settings'),
  actions: [
    ThemeToggleButton(themeService: themeService),
  ],
)
```

#### 2. Full Theme Selector (for Settings Page)

```dart
ThemeToggleWidget(
  themeService: themeService,
  showLabel: true,
  showSystemOption: true,
)
```

#### 3. Cycle Button (Advanced)

```dart
ThemeCycleButton(themeService: themeService)
```

### Using Colors in Your Widgets

```dart
// Use theme-aware colors
Container(
  color: Theme.of(context).scaffoldBackgroundColor,
  child: Text(
    'Hello World',
    style: TextStyle(
      color: Theme.of(context).textTheme.bodyLarge?.color,
    ),
  ),
)

// Or use direct color classes
Container(
  color: context.isDarkMode 
    ? DarkThemeColors.surface 
    : LightThemeColors.surface,
)
```

## 🎨 Color Scheme

### Light Theme Colors
- **Background**: Pure white (#FFFFFF)
- **Surface**: White (#FFFFFF) 
- **Primary**: Teal (#27929D)
- **Text**: Black for primary, gray variants for secondary
- **Input Fields**: Light gray fill (#F6FBFB)
- **Borders**: Light gray (#EEEEEE)

### Dark Theme Colors
- **Background**: Dark gray (#121212)
- **Surface**: Darker gray (#1E1E1E)
- **Primary**: Same teal (#27929D) - maintains brand consistency
- **Text**: White for primary, light gray variants for secondary
- **Input Fields**: Dark gray fill (#2D2D2D)
- **Borders**: Dark gray (#333333)

## 🔧 Customization

### Adding New Colors

1. **Add to color classes:**
```dart
// In app_colors.dart
class LightThemeColors {
  static Color newColor = const Color(0xFF123456);
}

class DarkThemeColors {
  static Color newColor = const Color(0xFF654321);
}
```

2. **Use in themes:**
```dart
// In app_theme.dart
ThemeData getLightTheme() {
  return ThemeData(
    // ... existing theme
    someProperty: LightThemeColors.newColor,
  );
}
```

### Modifying Existing Colors

Simply update the color values in the respective theme color classes:

```dart
class LightThemeColors {
  static Color scaffold = const Color(0xFFF5F5F5); // Changed from white
}
```

## 📱 Integration Examples

### Settings Screen Integration

```dart
class SettingsScreen extends StatefulWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Settings'),
        actions: [
          ThemeToggleButton(themeService: MyApp.themeService),
        ],
      ),
      body: ListView(
        children: [
          ListTile(
            title: Text('Appearance'),
            subtitle: Text('Choose your preferred theme'),
          ),
          Padding(
            padding: EdgeInsets.all(16),
            child: ThemeToggleWidget(
              themeService: MyApp.themeService,
            ),
          ),
        ],
      ),
    );
  }
}
```

### Profile Screen Integration

```dart
// Add a simple toggle in profile
ListTile(
  leading: Icon(Icons.palette),
  title: Text('Dark Mode'),
  trailing: Switch(
    value: themeService.isDarkMode,
    onChanged: (value) => themeService.toggleTheme(),
  ),
)
```

## 🔍 Testing Themes

1. **Test on different devices** - Colors may appear differently
2. **Test system theme switching** - Ensure automatic switching works
3. **Test persistence** - Theme should persist after app restart
4. **Test all UI components** - Ensure all widgets look good in both themes
5. **Test accessibility** - Ensure proper contrast ratios

## 🐛 Troubleshooting

### Theme not switching?
- Ensure `ThemeService` is properly initialized
- Check that widgets are listening to theme changes
- Verify `ListenableBuilder` is wrapping `MaterialApp`

### Colors not updating?
- Make sure you're using `Theme.of(context)` colors
- Check that custom widgets rebuild when theme changes
- Verify color references point to correct theme classes

### Persistence not working?
- Ensure `shared_preferences` package is added to `pubspec.yaml`
- Check that `ThemeService.init()` is called before app starts
- Verify permissions for local storage

## 📦 Dependencies

The theme system uses:
- `shared_preferences` - For theme persistence (add to pubspec.yaml if not present)
- `flutter/material.dart` - Core Flutter theming

## 🎯 Best Practices

1. **Always use theme colors** instead of hardcoded colors
2. **Test both themes** during development
3. **Use semantic color names** (primary, secondary, surface, etc.)
4. **Maintain consistent branding** across themes
5. **Consider accessibility** in color choices
6. **Provide theme switching options** in settings

## 📈 Future Enhancements

Potential improvements:
- Custom color picker for user-defined themes
- Multiple theme variants (e.g., high contrast)
- Automatic theme scheduling (dark at night)
- Theme animations and transitions
- Per-screen theme overrides

---

Your app now has a complete, production-ready theme system that provides an excellent user experience across both light and dark modes! 🌟
