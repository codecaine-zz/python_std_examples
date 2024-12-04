# locale - Internationalization services

Below are comprehensive code examples for the `locale` module in Python, covering various functionalities related to internationalization. Each example is accompanied by comments explaining each step.

```python
import locale

# Set the default locale (system-dependent)
try:
    # Use the system's preferred locale settings
    locale.setlocale(locale.LC_ALL, '')
except locale.Error as e:
    print(f"Failed to set locale: {e}")

# Get information about available locales
available_locales = locale.locale_alias.keys()
print("Available locales:")
for code in available_locales:
    print(code)

# Set a specific locale (example: French)
try:
    # Setting the locale for LC_ALL, ensuring all categories are affected
    locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')
    print(f"Locale set to: {locale.getlocale(locale.LC_ALL)}")
except locale.Error as e:
    print(f"Failed to set locale: {e}")

# Get the current locale settings
current_locale = locale.getlocale()
print("Current locale settings:")
for category, value in current_locale:
    print(f"{category}: {value}")

# Format a number using a specific locale
number = 123456.789
formatted_number = locale.currency(number)
print(f"Formatted currency: {formatted_number}")

# Format a string with localized date and time
now = datetime.datetime.now()
localized_date = now.strftime("%A, %B %d, %Y")
localized_time = now.strftime("%I:%M %p")
print(f"Localized Date: {localized_date}")
print(f"Localized Time: {localized_time}")

# Set the locale for LC_TIME to get localized date and time format
try:
    locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')
    localized_date = now.strftime("%A, %B %d, %Y")
    localized_time = now.strftime("%I:%M %p")
    print(f"Localized Date with LC_TIME: {localized_date}")
    print(f"Localized Time with LC_TIME: {localized_time}")
except locale.Error as e:
    print(f"Failed to set locale: {e}")

# Reset the locale settings to default
try:
    locale.setlocale(locale.LC_ALL, '')
    print(f"Locale reset to system default: {locale.getlocale(locale.LC_ALL)}")
except locale.Error as e:
    print(f"Failed to reset locale: {e}")
```

### Explanation:

1. **Setting the Default Locale**:
   - The `locale.setlocale(locale.LC_ALL, '')` sets the locale according to the system's preferred settings. This is useful for applications that need to adapt to user preferences.

2. **Available Locales**:
   - `locale.locale_alias.keys()` returns a list of all available locales. This can be helpful for users or developers who need to understand what locales are supported on their system.

3. **Setting a Specific Locale**:
   - `locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')` sets the locale to French (France) using UTF-8 encoding. You can replace `'fr_FR.UTF-8'` with any other locale identifier available on your system.

4. **Current Locale Settings**:
   - `locale.getlocale()` retrieves the current locale settings for all categories (`LC_ALL`, `LC_CTYPE`, `LC_COLLATE`, etc.).

5. **Formatting Numbers and Strings**:
   - `locale.currency(number)` formats a number as currency using the specified locale.
   - `strftime` is used to format dates and times according to the locale's date and time formatting rules.

6. **Setting LC_TIME for Locale-Specific Date/Time Formatting**:
   - Changing the locale to `LC_TIME` ensures that date and time formats are displayed according to the chosen locale, which can be useful for applications that need specific date/time formats.

7. **Resetting Locale Settings**:
   - `locale.setlocale(locale.LC_ALL, '')` resets the locale settings back to their system default, ensuring that the application runs without any locale-specific configurations.

These examples cover a range of functionalities provided by the `locale` module, allowing for effective internationalization in Python applications.
