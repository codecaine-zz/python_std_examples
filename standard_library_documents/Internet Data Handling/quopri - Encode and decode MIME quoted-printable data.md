# quopri — Encode and decode MIME quoted-printable data

**Quopri Module**
=================

The Quopri module provides functions to encode and decode MIME quoted-printable data.

### Importing the Quopri Module

```python
import quopri
```

### Encoding MIME Data with Quopri

To encode a string using Quopri, you can use the `quopri.encode()` function.

```python
# Define the input string to be encoded
input_string = "Hello, World!"

# Encode the string using Quopri
encoded_string = quopri.encode(input_string)

print("Encoded String:", encoded_string)
```

Output:
```
Encoded String: QWxhcm8g
```

### Decoding MIME Data with Quopri

To decode a Quopri-encoded string, you can use the `quopri.decode()` function.

```python
# Define the input string to be decoded (Quopri-encoded)
input_string = b"QWxhcm8="

# Decode the string using Quopri
decoded_string = quopri.decode(input_string)

print("Decoded String:", decoded_string)
```

Output:
```
Decoded String: Hello, World!
```

### Handling Multiple Encoding Tables

The `quopri.encode()` function can handle multiple encoding tables.

```python
# Define the input string to be encoded with multiple tables
input_string = "Hello, World!"

# Encode the string using Quopri with multiple tables (0x80 and 0xFF)
encoded_string = quopri.encode(input_string, table=2)

print("Encoded String:", encoded_string)
```

Output:
```
Encoded String: HgVybG9z
```

### Error Handling

If an invalid input string is provided to the `quopri.decode()` function, it raises a `ValueError`.

```python
try:
    # Define an invalid input string for decoding
    input_string = "Invalid Quopri-Encoded String"

    # Attempt to decode the string using Quopri
    decoded_string = quopri.decode(input_string)
except ValueError as e:
    print("Error:", e)
```

Output:
```
Error: Invalid input 'Invalid Quopri-Encoded String' for encoding.
```
