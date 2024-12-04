# locale — Internationalization services

Here's an example of how you can use the `locale` module in Python:
```python
import locale

# Get the current locale
def get_current_locale():
    """Return the current locale"""
    return locale.getlocale()

print("Current Locale:", get_current_locale())

# Set a new locale
def set_new_locale(locale_code, language_code):
    """
    Set a new locale.

    Args:
        locale_code (str): The full locale code (e.g. 'en_US.UTF-8')
        language_code (str): The language code (e.g. 'en' for English)

    Returns:
        bool: True if the locale was successfully set, False otherwise
    """
    try:
        locale.setlocale(locale.LC_ALL, locale_code)
        return True
    except Exception as e:
        print(f"Failed to set locale: {str(e)}")
        return False

# Test setting a new locale
print("Setting locale...")
set_new_locale('en_US.UTF-8', 'en')

# Get the language and country codes from the locale code
def get_language_and_country_code(locale_code):
    """
    Extract the language and country codes from the locale code.

    Args:
        locale_code (str): The full locale code

    Returns:
        tuple: A tuple containing the language code and the country code
    """
    parts = locale.getdefaultlocale()
    if parts is None:
        return None, None  # No suitable locale found
    language_code = parts[0]
    country_code = parts[1]
    return language_code, country_code

print("Language Code:", get_language_and_country_code('en_US.UTF-8'))
print("Country Code:", get_language_and_country_code('fr_FR.UTF-8'))

# Get the list of available locales
def get_available_locales():
    """Return a list of available locale codes"""
    return locale.getlocale()[0]

available_locales = get_available_locales()
for locale in available_locales:
    print(locale)

# Use locale for date and number formatting
import datetime

def format_date(date_obj):
    """
    Format the given date object as per the current locale.

    Args:
        date_obj (datetime.date): The date object to be formatted

    Returns:
        str: The formatted date string
    """
    return locale.format_string('%B %d, %Y', date_obj)

date_obj = datetime.date(2022, 12, 25)
print("Formatted Date:", format_date(date_obj))

def format_number(num):
    """
    Format the given number as per the current locale.

    Args:
        num (float): The number to be formatted

    Returns:
        str: The formatted number string
    """
    return locale.format_string('%d', num)

num = 12345.6789
print("Formatted Number:", format_number(num))
```
This code demonstrates how you can use the `locale` module to:

*   Get the current locale and set a new one
*   Extract language and country codes from the locale code
*   Get a list of available locales
*   Use locale for date and number formatting

Note that the behavior of some functions in the `locale` module can vary depending on the underlying operating system, so you may need to adjust your expectations or use platform-specific checks when working with these functions.
