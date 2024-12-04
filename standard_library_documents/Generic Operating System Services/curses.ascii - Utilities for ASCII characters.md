# curses.ascii — Utilities for ASCII characters

**curses.ascii Module**
=======================

The `curses.ascii` module provides functions and classes related to the use of ASCII characters in curses.

### Importing the Module
```python
import curses.ascii as ascii
```

### Functions

#### `ascii.isalnum()`
Checks if a character is alphanumeric (either letter or number).

*   Returns: True if the character is alphanumeric, False otherwise.
*   Example:
    ```python
# Check if a character is alphanumeric
if ascii.isalnum('a'):
    print("Character 'a' is alphanumeric")
else:
    print("Character 'a' is not alphanumeric")
```

#### `ascii.isalpha()`
Checks if a character is an alphabetic character.

*   Returns: True if the character is alphabetic, False otherwise.
*   Example:
    ```python
# Check if a character is alphabetic
if ascii.isalpha('A'):
    print("Character 'A' is alphabetic")
else:
    print("Character 'A' is not alphabetic")
```

#### `ascii.isascii()`
Checks if a character is an ASCII character.

*   Returns: True if the character is ASCII, False otherwise.
*   Example:
    ```python
# Check if a character is ASCII
if ascii.isascii('\u4F60'):
    print("Character '\u4F60' is ASCII")
else:
    print("Character '\u4F60' is not ASCII")
```

#### `ascii.isdigit()`
Checks if a character is a digit.

*   Returns: True if the character is a digit, False otherwise.
*   Example:
    ```python
# Check if a character is a digit
if ascii.isdigit('5'):
    print("Character '5' is a digit")
else:
    print("Character '5' is not a digit")
```

#### `ascii.islower()`
Checks if a character is in the lowercase letter set.

*   Returns: True if the character is lowercase, False otherwise.
*   Example:
    ```python
# Check if a character is lowercase
if ascii.islower('a'):
    print("Character 'a' is lowercase")
else:
    print("Character 'a' is not lowercase")
```

#### `ascii.isprintable()`
Checks if a character can be printed.

*   Returns: True if the character can be printed, False otherwise.
*   Example:
    ```python
# Check if a character can be printed
if ascii.isprintable('\n'):
    print("Character '\n' can be printed")
else:
    print("Character '\n' cannot be printed")
```

#### `ascii.isascii()`
Checks if a character is an ASCII character.

*   Returns: True if the character is ASCII, False otherwise.
*   Example:
    ```python
# Check if a character is ASCII
if ascii.isascii('\u4F60'):
    print("Character '\u4F60' is ASCII")
else:
    print("Character '\u4F60' is not ASCII")
```

#### `ascii.isupper()`
Checks if a character is in the uppercase letter set.

*   Returns: True if the character is uppercase, False otherwise.
*   Example:
    ```python
# Check if a character is uppercase
if ascii.isupper('A'):
    print("Character 'A' is uppercase")
else:
    print("Character 'A' is not uppercase")
```

#### `ascii.isspace()`
Checks if a character is a whitespace character.

*   Returns: True if the character is whitespace, False otherwise.
*   Example:
    ```python
# Check if a character is whitespace
if ascii.isspace(' '):
    print("Character ' ' is whitespace")
else:
    print("Character ' ' is not whitespace")
```

#### `ascii.isidentifier()`
Checks if a string is an ASCII identifier.

*   Returns: True if the string is an ASCII identifier, False otherwise.
*   Example:
    ```python
# Check if a string is an ASCII identifier
if ascii.isidentifier('abc'):
    print("String 'abc' is an ASCII identifier")
else:
    print("String 'abc' is not an ASCII identifier")
```

#### `ascii.isdecimal()`
Checks if a character is a decimal digit.

*   Returns: True if the character is a decimal digit, False otherwise.
*   Example:
    ```python
# Check if a character is a decimal digit
if ascii.isdecimal('0'):
    print("Character '0' is a decimal digit")
else:
    print("Character '0' is not a decimal digit")
```

#### `ascii.islowercase()`
Checks if all characters in the string are lowercase.

*   Returns: True if all characters are lowercase, False otherwise.
*   Example:
    ```python
# Check if all characters in a string are lowercase
if ascii.islowercase('abcdef'):
    print("All characters in 'abcdef' are lowercase")
else:
    print("Not all characters in 'abcdef' are lowercase")
```

#### `ascii.isuppercase()`
Checks if all characters in the string are uppercase.

*   Returns: True if all characters are uppercase, False otherwise.
*   Example:
    ```python
# Check if all characters in a string are uppercase
if ascii.isuppercase('ABCDEF'):
    print("All characters in 'ABCDEF' are uppercase")
else:
    print("Not all characters in 'ABCDEF' are uppercase")
```

#### `ascii.isspace()`
Checks if all characters in the string are whitespace.

*   Returns: True if all characters are whitespace, False otherwise.
*   Example:
    ```python
# Check if all characters in a string are whitespace
if ascii.isspace('   '):
    print("All characters in '   ' are whitespace")
else:
    print("Not all characters in '   ' are whitespace")
```

#### `ascii.isprintable()`
Checks if all characters in the string can be printed.

*   Returns: True if all characters can be printed, False otherwise.
*   Example:
    ```python
# Check if all characters in a string can be printed
if ascii.isprintable('\nabc'):
    print("All characters in '\nabc' can be printed")
else:
    print("Not all characters in '\nabc' can be printed")
```

#### `ascii.digits`
Returns a string of ASCII digit characters.

*   Returns: A string containing only the ASCII digits.
*   Example:
    ```python
# Get a string of ASCII digit characters
digits = ascii.digits
print(digits)  # prints '0123456789'
```

#### `ascii.ascii_letters`
Returns a string of ASCII letter characters.

*   Returns: A string containing only the ASCII letters.
*   Example:
    ```python
# Get a string of ASCII letter characters
letters = ascii.ascii_letters
print(letters)  # prints 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
```
