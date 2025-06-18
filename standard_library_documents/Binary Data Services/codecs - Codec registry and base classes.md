# codecs - Codec registry and base classes

The `codecs` module in Python provides a comprehensive set of tools for handling different character encodings, including converting between different character encodings, decoding raw bytes into strings, and encoding strings back into raw bytes. Below are several code examples demonstrating various functionalities within the `codecs` module:

## Table of Contents

1. [Encoding and Decoding Strings](#example-1-encoding-and-decoding-strings)
2. [Handling Non-Breaking Spaces](#example-2-handling-non-breaking-spaces)
3. [Encoding with Different Encodings](#example-3-encoding-with-different-encodings)
4. [Using Codec Aliases](#example-4-using-codec-aliases)
5. [Handling Unicode Characters](#example-5-handling-unicode-characters)
6. [Error Handling during Encoding and Decoding](#example-6-error-handling-during-encoding-and-decoding)
7. [Using codecs.open for File Handling](#example-7-using-codecsopen-for-file-handling)
8. [Using codecs.iterencode and codecs.iterdecode](#example-8-using-codecsiterencode-and-codecsiterdecode)

### Example 1: Encoding and Decoding Strings

```python
import codecs

# Define a string in UTF-8 encoding
original_string = "Hello, World!"

# Encode the string to bytes using UTF-8 encoding
encoded_bytes = original_string.encode('utf-8')
print(f"Original String: {original_string}")
print(f"Encoded Bytes: {encoded_bytes}")

# Decode the bytes back to a string using UTF-8 decoding
decoded_string = encoded_bytes.decode('utf-8')
print(f"Decoded String: {decoded_string}")
```

**Explanation**: This example demonstrates how to encode and decode strings between UTF-8 encoding. The `encode` method converts the string into bytes, and the `decode` method converts bytes back into a string.

### Example 2: Handling Non-Breaking Spaces

```python
import codecs

# Define a string with non-breaking spaces
non_breaking_string = "Hello,\xa0World!"

# Decode the string using UTF-8 decoding to handle non-breakable spaces
decoded_string = non_breaking_string.decode('utf-8')
print(f"Decoded String: {decoded_string}")
```

**Explanation**: This example shows how to handle strings with non-breaking spaces. The `decode` method automatically handles these special characters when decoding from UTF-8.

### Example 3: Encoding with Different Encodings

```python
import codecs

# Define a string in ASCII encoding
ascii_string = "Hello, World!"

# Encode the string to bytes using ASCII encoding
encoded_bytes_ascii = ascii_string.encode('ascii')
print(f"Encoded Bytes (ASCII): {encoded_bytes_ascii}")

# Define another string in ISO-8859-1 encoding
iso_string = "Café"

# Encode the string to bytes using ISO-8859-1 encoding
encoded_bytes_iso = iso_string.encode('iso-8859-1')
print(f"Encoded Bytes (ISO-8859-1): {encoded_bytes_iso}")
```

**Explanation**: This example demonstrates how to encode strings in different character encodings, such as ASCII and ISO-8859-1. The `encode` method converts the string into bytes using the specified encoding.

### Example 4: Using Codec Aliases

```python
import codecs

# Define a string in UTF-8 encoding
original_string = "Hello, World!"

# Encode the string to bytes using the alias 'utf-8'
encoded_bytes_alias = original_string.encode('utf-8')
print(f"Encoded Bytes (Alias): {encoded_bytes_alias}")
```

**Explanation**: This example shows how to use codec aliases to specify an encoding by its alias name. The `encode` method uses the specified alias to encode the string into bytes.

### Example 5: Handling Unicode Characters

```python
import codecs

# Define a string containing a Unicode character
unicode_string = "Hello, 🌍!"

# Encode the string to bytes using UTF-8 encoding
encoded_bytes_unicode = unicode_string.encode('utf-8')
print(f"Encoded Bytes (Unicode): {encoded_bytes_unicode}")

# Decode the bytes back to a string using UTF-8 decoding
decoded_string_unicode = encoded_bytes_unicode.decode('utf-8')
print(f"Decoded String (Unicode): {decoded_string_unicode}")
```

**Explanation**: This example demonstrates how to handle Unicode characters in strings. The `encode` method converts the string into bytes, and the `decode` method converts bytes back into a string, preserving the Unicode representation.

### Example 6: Error Handling during Encoding and Decoding

```python
import codecs

# Define a string containing a character that cannot be encoded with ASCII
non_ascii_string = "Hello, 😊!"

try:
    # Attempt to encode the string using ASCII encoding (this will raise an error)
    encoded_bytes_error = non_ascii_string.encode('ascii')
except UnicodeEncodeError as e:
    print(f"Encoding Error: {e}")

# Define a string containing a character that cannot be decoded with UTF-8
unicode_non_decodable_string = "Hello, 🌍!"

try:
    # Attempt to decode the bytes using UTF-8 decoding (this will raise an error)
    decoded_string_error = unicode_non_decodable_string.decode('utf-8')
except UnicodeDecodeError as e:
    print(f"Decoding Error: {e}")
```

**Explanation**: This example demonstrates how to handle errors during encoding and decoding operations. The `encode` method raises a `UnicodeEncodeError` if it encounters a character that cannot be encoded, and the `decode` method raises a `UnicodeDecodeError` if it encounters an invalid byte sequence.

### Example 7: Using codecs.open for File Handling

```python
import codecs

# Define a string to write to a file using UTF-8 encoding
write_string = "Hello, World!"

# Open a file for writing and encode the string using UTF-8 encoding
with codecs.open('output.txt', 'w', encoding='utf-8') as file:
    file.write(write_string)

# Read the file back and decode it to a string using UTF-8 decoding
with codecs.open('output.txt', 'r', encoding='utf-8') as file:
    read_string = file.read()
    print(f"Read String: {read_string}")
```

**Explanation**: This example demonstrates how to use `codecs.open` for file handling. It writes a string to a file and then reads it back, both using UTF-8 encoding.

### Example 8: Using codecs.iterencode and codecs.iterdecode

```python
import codecs

# Define a list of Unicode characters
unicode_chars = ['Hello', 'World', '!']

# Encode each character in the list using UTF-8 encoding
encoded_iter = codecs.iterencode(unicode_chars, 'utf-8')
for encoded_bytes in encoded_iter:
    print(f"Encoded Bytes: {encoded_bytes}")

# Decode each byte sequence back to a string using UTF-8 decoding
decoded_iter = codecs.iterdecode(encoded_iter, 'utf-8')
for decoded_string in decoded_iter:
    print(f"Decoded String: {decoded_string}")
```

**Explanation**: This example demonstrates how to use `codecs.iterencode` and `codecs.iterdecode` for encoding and decoding multiple strings efficiently. These functions are useful when dealing with sequences of characters.

These examples cover a range of functionalities within the `codecs` module, including basic encoding/decoding operations, handling special characters, using codec aliases, handling Unicode characters, error handling, file handling with `codecs.open`, and more.
