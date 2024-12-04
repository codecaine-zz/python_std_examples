# tokenize - Tokenizer for Python source

The `tokenize` module in Python is used to break a Python source file into tokens, which are the smallest units of Python syntax. Below are comprehensive examples demonstrating various functionalities provided by the `tokenize` module.

### Example 1: Basic Tokenization

```python
import tokenize
from io import BytesIO

# Define a sample Python code as a byte string
code = b'print("Hello, World!")'

# Create a buffer from the byte string
buffer = BytesIO(code)

# Get an iterator over the tokens in the buffer
tokens = tokenize.tokenize(buffer.readline)

# Iterate and print each token
for toknum, tokval, start, end, line in tokens:
    print(f"Token: {toknum}, Value: '{tokval}', Start: {start}, End: {end}, Line: '{line}'")
```

### Explanation:

- **Import Statements**: We import the `tokenize` module and `BytesIO` from the `io` module.
- **Buffer Creation**: We create a byte string representing a simple Python statement and wrap it in a `BytesIO` buffer. This allows us to simulate reading from a file-like object.
- **Tokenization**: We use the `tokenize.tokenize()` function, which takes a generator that returns lines of input. Each token is returned as an iterable of five elements: `(toknum, tokval, start, end, line)`.
- **Output**: We print each token's numeric type, value, and location within the source code.

### Example 2: Handling Errors in Tokenization

```python
import tokenize
from io import BytesIO

# Define a sample Python code with an error
code = b'print("Hello, World!'; # This is a syntax error'

# Create a buffer from the byte string
buffer = BytesIO(code)

# Get an iterator over the tokens in the buffer
tokens = tokenize.tokenize(buffer.readline)

try:
    for toknum, tokval, start, end, line in tokens:
        print(f"Token: {toknum}, Value: '{tokval}', Start: {start}, End: {end}, Line: '{line}'")
except tokenize.TokenError as e:
    print(f"Error encountered at tokenization: {e}")
```

### Explanation:

- **Error Handling**: We handle `tokenize.TokenError` to catch and report any errors that occur during tokenization.
- **Output**: The error message is printed if an exception occurs, providing more context about the problem.

### Example 3: Extracting Tokens with Specific Names

```python
import tokenize
from io import BytesIO

# Define a sample Python code with multiple tokens
code = b'x = y + z; print(x);'

# Create a buffer from the byte string
buffer = BytesIO(code)

# Get an iterator over the tokens in the buffer
tokens = tokenize.tokenize(buffer.readline)

# Extract and print only 'NAME' (variable names) and 'NUMBER' (numeric literals)
for toknum, tokval, start, end, line in tokens:
    if toknum in (tokenize.NAME, tokenize.NUMBER):
        print(f"Token: {toknum}, Value: '{tokval}', Start: {start}, End: {end}, Line: '{line}'")
```

### Explanation:

- **Filtering Tokens**: We filter tokens based on their numeric identifiers `tokenize.NAME` (variable names) and `tokenize.NUMBER` (numeric literals).
- **Output**: Only the filtered tokens are printed, showcasing how to selectively extract specific types of tokens.

### Example 4: Tokenizing from a File

```python
import tokenize
import os

# Define the path to a Python source file
file_path = 'example.py'

# Open and read the file
with open(file_path, 'rb') as file:
    code = file.read()

# Create a buffer from the file content
buffer = BytesIO(code)

# Get an iterator over the tokens in the buffer
tokens = tokenize.tokenize(buffer.readline)

# Iterate and print each token
for toknum, tokval, start, end, line in tokens:
    print(f"Token: {toknum}, Value: '{tokval}', Start: {start}, End: {end}, Line: '{line}'")
```

### Explanation:

- **File Handling**: We open a file in binary mode and read its content into a byte string.
- **Buffer Creation**: Similar to the previous examples, we create a `BytesIO` buffer from the file content.
- **Tokenization**: The tokenization process is identical to before, but now we are processing tokens from a file instead of a byte string.

These examples demonstrate how to use the `tokenize` module effectively for various tasks such as analyzing Python code, debugging, or extracting specific information from source files.
