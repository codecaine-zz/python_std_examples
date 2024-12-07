# unicodedata - Unicode Database

Below are comprehensive and well-documented code examples for the `unicodedata` module in Python, which provides access to a comprehensive database of Unicode characters.

### Example 1: Retrieve Character Name
This example demonstrates how to retrieve the name of a character using its Unicode code point.

```python
import unicodedata

# Define a Unicode code point
code_point = ord('A')

# Retrieve and print the character name
character_name = unicodedata.name(chr(code_point))
print(f"The name of character U+{code_point:04X} is {character_name}")
```

### Example 2: Check Character Properties
This example checks if a character has specific properties like being an uppercase letter, lowercase letter, or digit.

```python
import unicodedata

# Define a Unicode code point
code_point = ord('A')

# Check if the character is an uppercase letter
is_uppercase = unicodedata.category(chr(code_point)).startswith('Lu')
print(f"Character U+{code_point:04X} is uppercase: {is_uppercase}")

# Check if the character is a lowercase letter
is_lowercase = unicodedata.category(chr(code_point)).startswith('Ll')
print(f"Character U+{code_point:04X} is lowercase: {is_lowercase}")

# Check if the character is a digit
is_digit = unicodedata.category(chr(code_point)).startswith('Nd')
print(f"Character U+{code_point:04X} is a digit: {is_digit}")
```

### Example 3: Normalize Text
This example demonstrates how to normalize text using different normalization forms provided by the `unicodedata` module.

```python
import unicodedata

# Define some text with combining characters
text = "éclair"

# Normalize text to NFC (Canonical Decomposition followed by Canonical Composition)
nfc_normalized = unicodedata.normalize('NFC', text)
print(f"Normalized using NFC: {nfc_normalized}")

# Normalize text to NFD (Canonical Decomposition)
nfd_normalized = unicodedata.normalize('NFD', text)
print(f"Normalized using NFD: {nfd_normalized}")

# Normalize text to NFKC (Compatibility Decomposition followed by Canonical Composition)
nfkc_normalized = unicodedata.normalize('NFKC', text)
print(f"Normalized using NFKC: {nfkc_normalized}")

# Normalize text to NFKD (Compatibility Decomposition)
nfkd_normalized = unicodedata.normalize('NFKD', text)
print(f"Normalized using NFKD: {nfkd_normalized}")
```

### Example 4: Extract Combining Characters
This example extracts combining characters from a given string.

```python
import unicodedata

# Define a string with combining characters
text = "éclair"

# Extract and print combining characters
combining_characters = ''.join(
    chr(c) for c in range(0x300, 0x37F) if (
        unicodedata.category(chr(c)).startswith('Me') and unicodedata.decomposition(chr(c)) is not None
    )
)
print(f"Combining characters in '{text}': {combining_characters}")
```

### Example 5: Convert Character to Emoji Sequence
This example demonstrates how to convert a character to its corresponding emoji sequence using the `emoji` module, which is often used alongside `unicodedata`.

pip install emoji

```python
import unicodedata

# Define a Unicode code point for an emoji
code_point = ord('😊')

# Get the character's name
character_name = unicodedata.name(chr(code_point))
print(f"Character U+{code_point:04X} is '{character_name}'")

# Convert to emoji sequence (assuming you have the `emoji` module installed)
import emoji

emoji_sequence = emoji.emojize(character_name)
print(f"Emoji sequence for {character_name}: {emoji_sequence}")
```

### Example 6: Check Character Bidirectional Properties
This example checks if a character has bidirectional properties like being left-to-right, right-to-left, or neutral.

```python
import unicodedata

# Define a Unicode code point
code_point = ord('A')

# Check bidirectional property
is_left_to_right = unicodedata.bidirectional(chr(code_point)) == 'L'
print(f"Character U+{code_point:04X} is left-to-right: {is_left_to_right}")

is_right_to_left = unicodedata.bidirectional(chr(code_point)) == 'R'
print(f"Character U+{code_point:04X} is right-to-left: {is_right_to_left}")

is_neutral = unicodedata.bidirectional(chr(code_point)) in ('LRE', 'LRO', 'PDF', 'NSM', 'AL')
print(f"Character U+{code_point:04X} is neutral: {is_neutral}")
```

These examples cover a range of functionalities provided by the `unicodedata` module, including retrieving character names, checking properties, normalizing text, extracting combining characters, converting to emoji sequences, and checking bidirectional properties.
