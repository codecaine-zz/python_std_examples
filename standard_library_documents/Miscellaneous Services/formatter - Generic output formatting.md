# formatter - Generic output formatting

The `formatter` module in Python is not a part of the standard library itself, but rather a part of the `locale` module, which provides locale-aware functions and classes. This module does not include any generic output formatting functionality. Instead, it is used for handling locale-specific information and number formatting.

However, I can provide an example of how to use the `locale` module to format numbers in different locales. Here's a comprehensive guide on how you might achieve this:

```python
import locale

def format_number(number, locale_str):
    """
    Formats a given number into a string using the specified locale.

    Parameters:
    - number: The number to be formatted.
    - locale_str: A string representing the locale (e.g., 'en_US.UTF-8', 'fr_FR.UTF-8').

    Returns:
    - A string representation of the number in the specified locale.
    """
    try:
        # Set the locale
        locale.setlocale(locale.LC_ALL, locale_str)
        
        # Format the number using the current locale
        formatted_number = locale.format_string("%d", number, grouping=True)
        
        return formatted_number
    except locale.Error as e:
        print(f"Error setting locale: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # List of locales to test
    locales = ['en_US.UTF-8', 'fr_FR.UTF-8', 'de_DE.UTF-8']

    # Number to format
    number_to_format = 1234567

    # Iterate over each locale and print the formatted number
    for locale_str in locales:
        formatted_number = format_number(number_to_format, locale_str)
        if formatted_number is not None:
            print(f"Number {number_to_format} formatted as '{formatted_number}' in {locale_str}.")
```

### Explanation:

1. **Locale Setting**: The `locale.setlocale()` function is used to set the global locale for number formatting. This sets the locale for all categories, including numeric formats.

2. **Formatting Numbers**: The `locale.format_string()` function is used to format numbers according to the current locale settings. The `%d` directive is used for integers, and `grouping=True` adds commas as thousands separators.

3. **Error Handling**: A try-except block is used to handle any errors that might occur when setting the locale, such as unsupported locales or missing data files.

4. **Example Usage**: The script demonstrates how to format the number 1234567 into strings for three different locales: US English, French, and German.

This example provides a basic framework for using the `locale` module to handle number formatting in different locales, which is often necessary for applications that need to display numbers according to user preferences or specific standards.
