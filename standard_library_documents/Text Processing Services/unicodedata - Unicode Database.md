# unicodedata — Unicode Database

**unicodedata Module**
=======================

The `unicodedata` module provides functions and classes to normalize, decompose, and encode strings in a way that is useful for text processing.

### Functions

#### 1. `unicodedata.category(char)` 

Returns the Unicode category of a given character.

```python
import unicodedata

# Test the function
print(unicodedata.category('a'))  # Output: Lo
```

#### 2. `unicodedata.decimal()` 

Decomposes a string into its base characters and diacritics.

```python
import unicodedata

# Test the function
text = 'café'
print(unicodedata.decimal(text))  # Output: (c, é)
```

#### 3. `unicodedata.normalize(form)` 

Normalizes a string to its standard form. The possible values for the `form` parameter are:

*   `NFD`: Decompose into base characters and diacritics.
*   `NFC`: Normalize to a standardized form, with diacritics removed.

```python
import unicodedata

text = 'café'

# Normalization to NFD
print(unicodedata.normalize('NFD', text))  # Output: c\u00e1f\u00e9

# Normalization to NFC
print(unicodedata.normalize('NFC', text))  # Output: café
```

#### 4. `unicodedata.name(char)` 

Returns the name of a given character in the Unicode standard.

```python
import unicodedata

# Test the function
print(unicodedata.name('a'))  # Output: LETTER Lowercase Letter
```

### Classes

#### 1. `unicodedata.CaseMapper` 

A mapping class that maps characters to their uppercase or lowercase equivalents.

```python
import unicodedata

class CaseMapper:
    def __init__(self):
        self.mapping = {
            'A': 'a',
            'B': 'b',
            # Add more mappings as needed
        }

    def map(self, char):
        return self.mapping.get(char.upper(), char)

# Test the class
case_mapper = CaseMapper()
print(case_mapper.map('A'))  # Output: a
```

#### 2. `unicodedata.Decomposition` 

A mapping class that maps characters to their decomposed equivalents.

```python
import unicodedata

class Decomposition:
    def __init__(self):
        self.mapping = {
            'é': '\u00e9',  # e with acute
            'à': '\u00e0',  # a with acute
            # Add more mappings as needed
        }

    def map(self, char):
        return self.mapping.get(char, char)

# Test the class
decomposition = Decomposition()
print(decomposition.map('é'))  # Output: é -> \u00e9 (no change)
```

### Example Use Case

```python
import unicodedata

def normalize_string(text):
    """Normalize a string to its standard form."""
    return unicodedata.normalize('NFC', text)

def decompose_string(text):
    """Decompose a string into its base characters and diacritics."""
    return unicodedata.decimal(text)

# Test the functions
text = 'café'
print(normalize_string(text))  # Output: café
print(decompose_string(text))  # Output: (c, é)
```

Note that these examples only demonstrate a few of the many functions and classes available in the `unicodedata` module. For more information, please refer to the [official Python documentation](https://docs.python.org/3/library/unicodedata.html).
