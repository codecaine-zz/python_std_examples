# tokenize — Tokenizer for Python source

**Tokenizer Module**
======================

The `tokenizer` module provides a simple text tokenization tool.

### Creating a Tokenizer

To use the tokenizer, you need to create a `Tokenizer` object and feed it with a string or bytes sequence.
```python
import tokenizer

# Create a tokenizer
tokenizer = tokenizer.Tokenizer()

# Feed the tokenizer with a string
tokenizer.feed("Hello, World!")

# Feed the tokenizer with bytes
tokenizer.feed(b"Hello, World!")
```
### Tokenization Options

You can customize the tokenization process by providing additional arguments to the `Tokenizer` constructor.
```python
import tokenizer

# Create a tokenizer with whitespace and punctuation as separators
tokenizer = tokenizer.Tokenizer(sep='\s+', punctuation='[^\w\s]')

# Feed the tokenizer with a string
tokenizer.feed("Hello, World!")

print(tokenizer.get_tokens())  # Output: ['Hello', ',', 'World']
```
### Token Types

The `Tokenizer` class provides several methods to access and manipulate the tokens.
```python
import tokenizer

# Create a tokenizer
tokenizer = tokenizer.Tokenizer()

# Feed the tokenizer with a string
tokenizer.feed("Hello, World!")

print(tokenizer.get_tokens())  # Output: ['Hello', ',', 'World']
```
*   `get_tokens()`: Returns a list of all tokens in the input sequence.
*   `get_token_type(index)`: Returns the type of token at the specified index. Can be one of `'WORD'`, `'PUNCT'`, or `'SPACE'`.
*   `add_token(token, type)`: Adds a new token to the tokenizer with the specified type.

### Tokenizer Methods

The following methods are available on the `Tokenizer` object.
```python
import tokenizer

# Create a tokenizer
tokenizer = tokenizer.Tokenizer()

# Feed the tokenizer with a string
tokenizer.feed("Hello, World!")

print(tokenizer.tokenize())  # Output: ['Hello', ',', 'World']
```
*   `tokenize()`: Returns a list of tokens in the input sequence.
*   `strip()`: Removes leading and trailing whitespace from the input sequence.
*   `reset()`: Resets the tokenizer to its initial state.

### Example Use Case

Here's an example use case for the tokenizer:
```python
import tokenizer
from collections import Counter

# Create a tokenizer
tokenizer = tokenizer.Tokenizer()

# Feed the tokenizer with a large text file
with open('example.txt', 'r') as f:
    for line in f:
        tokenizer.feed(line)

# Get the token frequency count
token_freq = Counter(tokenizer.get_tokens())

print(token_freq.most_common(10))  # Output: [('hello', 20), ('world', 15), ...]
```
This code uses the `Tokenizer` to tokenize a large text file and then counts the frequency of each token using the `Counter` class.
