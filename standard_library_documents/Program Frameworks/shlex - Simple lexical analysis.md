# shlex — Simple lexical analysis

**Shlex Module**
================

The `shlex` module provides simple lexical analysis of shell-like input.

### Usage

```python
import shlex

# Parsing example
input_string = 'echo "hello world"'
parsed_string = shlex.split(input_string)
print(parsed_string)  # Output: ['echo', "hello world"]

# Quoting and escaping example
quoted_input = '"foo bar" -- --'
quoting_style = shlex.quote
print(quoting_style(quoted_input))  # Output: 'foo bar -- --'

# Tokenization example
input_string = 'cat -n filename.txt'
tokens = shlex.split(input_string)
for token in tokens:
    print(token)  # Output: ['cat', '-n', 'filename.txt']
```

### Functions

#### `shlex.split(input_string, posix=False)`

Parses a string into a list of tokens.

*   `input_string`: The input string to parse.
*   `posix`: If `True`, splits on whitespace and quoted text according to the POSIX shell syntax. Defaults to `False`.

```python
# Example usage:
input_string = 'foo bar'
parsed_tokens = shlex.split(input_string)
print(parsed_tokens)  # Output: ['foo', 'bar']
```

#### `shlex.quote(value, posix=False)`

Escapes and quotes a value according to the shell syntax.

*   `value`: The input value to quote.
*   `posix`: If `True`, uses POSIX-style quoting. Defaults to `False`.

```python
# Example usage:
quoted_value = shlex.quote('foo bar')
print(quoted_value)  # Output: 'foo\ bar'
```

### Classes

#### `shlex.tokenizer`

Provides a way to tokenize a stream of input.

*   `input_string`: The input string to tokenize.
*   `posix`: If `True`, uses POSIX-style quoting. Defaults to `False`.

```python
# Example usage:
tokenizer = shlex.tokenizer(input_string='foo bar')
while True:
    token = tokenizer.get_token()
    if not token:
        break
    print(token)  # Output: ['foo', 'bar']
```

### Exceptions

#### `shlex.util.error`

Raised when an error occurs during parsing.

```python
try:
    shlex.split('invalid input')
except shlex.util.error as e:
    print(e)  # Output: Invalid input
```

Note that the actual exceptions raised by the `shlex` module may vary depending on the Python version and the specific use case.
