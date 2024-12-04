# string — Common string operations

Here's an example of how you can use common string operations available in Python's `string` module:
```python
import string

# Creating all possible printable ASCII characters
printable_chars = string.printable
for char in printable_chars:
    print(char)

# Creating all punctuation marks
punctuation_marks = string.punctuation
for mark in punctuation_marks:
    print(mark)

# Converting string to lowercase, uppercase and title case
original_string = "Hello World"
lowercase = original_string.lower()
uppercase = original_string.upper()
title_case = original_string.title()
print("Original String:", original_string)
print("Lowercase:", lowercase)
print("Uppercase:", uppercase)
print("Title Case:", title_case)

# Removing leading and trailing whitespaces
string_with_spaces = "   Hello World   "
stripped_string = string_with_spaces.strip()
print("Original String with Spaces:", string_with_spaces)
print("String after removing Leading/Trailing Whitespaces:", stripped_string)

# Splitting a string into substrings
sentence = "Hello, World!"
substrings = sentence.split(',')
print("Original Sentence:", sentence)
print("Substrings:", substrings)

# Joining multiple strings into one
multiple_strings = ["Hello", ", World!", "!"]
joined_string = "".join(multiple_strings)
print("Multiple Strings:", multiple_strings)
print("Joined String:", joined_string)

# Replacing a substring with another string
original_string = "Hello World"
new_string = original_string.replace("World", "Python")
print("Original String:", original_string)
print("String after replacing 'World' with 'Python':", new_string)

# Counting the occurrences of a character in a string
char_to_count = "a"
string = "banana"
count = string.count(char_to_count)
print("Count of '{}' in '{}':".format(char_to_count, string), count)

# Finding the index of a substring within a string
substring = "an"
original_string = "banana"
index = original_string.find(substring)
if index != -1:
    print("Index of '{}' in '{}': {}".format(substring, original_string, index))
else:
    print("'{}' not found in '{}'".format(substring, original_string))

# Creating a string from bytes
bytes_data = b"Hello World"
string_from_bytes = bytes_data.decode('utf-8')
print("Bytes Data:", bytes_data)
print("String from Bytes:", string_from_bytes)

# Encoding and decoding strings to/from bytes
original_string = "Hello World"
encoded_bytes = original_string.encode('utf-8')
decoded_string = encoded_bytes.decode('utf-8')
print("Original String:", original_string)
print("Encoded Bytes:", encoded_bytes)
print("Decoded String:", decoded_string)
```
Note that this example only covers the common string operations available in Python's `string` module. For more advanced string operations, you may need to use other modules like `re` or `datetime`.
