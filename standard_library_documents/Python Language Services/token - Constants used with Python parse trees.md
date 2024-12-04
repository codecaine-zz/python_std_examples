# token - Constants used with Python parse trees

The `token` module in Python provides constants that are used to identify different types of tokens in a Python source code. These constants are part of the Abstract Syntax Tree (AST) and are used by tools like PEP 8 checkers, linters, and static code analysis tools to analyze Python code.

Here are comprehensive examples for each constant provided by the `token` module:

```python
import token

# Define a simple Python expression as a string
source_code = "42 + 5"

# Tokenize the source code into tokens
tokens = []
for tok in tokenize.tokenize(io.BytesIO(source_code.encode('utf-8')).readline):
    # Append each token to the list with its type and value
    tokens.append((tok.type, tok.string))

# Print the list of tokens
print(tokens)

# Example: Extracting specific tokens from the list
integer_tokens = [t for t in tokens if t[0] == token.NUMBER]
print(integer_tokens)
```

### Explanation:

1. **Import Token**: The `token` module is imported to access the constants and functions related to tokens.

2. **Source Code**: A simple Python expression is defined as a string.

3. **Tokenization**: The `tokenize.tokenize()` function is used to tokenize the source code. It reads the source code line by line, converting it into a sequence of tokens.

4. **Collect Tokens**: Each token is captured and stored in a list along with its type and value.

5. **Print Tokens**: The list of tokens is printed, showing each token's type and string representation.

6. **Extract Specific Tokens**: A list comprehension is used to extract all `NUMBER` tokens from the list, which represent integer literals in Python.

These examples demonstrate how to use the `token` module to process and analyze Python source code tokens.
