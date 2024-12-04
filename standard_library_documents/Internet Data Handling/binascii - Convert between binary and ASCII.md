# binascii — Convert between binary and ASCII

**Binascii Module**
====================
```python
import binascii

# Functions
------------------

### hexlify()

Converts a bytes-like object into a hexadecimal string.

```python
# Example usage:
bytes_obj = b'Hello, World!'
hex_string = binascii.hexlify(bytes_obj)
print(hex_string)  # Output: b'48656c6c6f2c20576f726c6421'

# Convert back to bytes
bytes_again = binascii.unhexlify(hex_string)
print(bytes_again == bytes_obj)  # Output: True
```

### unhexlify()

Converts a hexadecimal string into a bytes-like object.

```python
# Example usage:
hex_string = '48656c6c6f2c20576f726c6421'
bytes_obj = binascii.unhexlify(hex_string)
print(bytes_obj == b'Hello, World!')  # Output: True
```

### getbase64()

Converts a bytes-like object into a base64-encoded string.

```python
# Example usage:
bytes_obj = b'Hello, World!'
base64_string = binascii.getbase64(bytes_obj)
print(base64_string)  # Output: SGVsbG8sIFdvcmxkIQ==

# Convert back to bytes
bytes_again = binascii.getbase64decode(base64_string)
print(bytes_again == bytes_obj)  # Output: True
```

### getbase64decode()

Converts a base64-encoded string into a bytes-like object.

```python
# Example usage:
base64_string = 'SGVsbG8sIFdvcmxkIQ=='
bytes_obj = binascii.getbase64decode(base64_string)
print(bytes_obj == b'Hello, World!')  # Output: True
```

### ascii()

Converts a bytes-like object into an ASCII string.

```python
# Example usage:
bytes_obj = b'\xc3\xbctest'
ascii_str = binascii.ascii(bytes_obj)
print(ascii_str)  # Output: test

# Convert back to bytes
bytes_again = binascii.ascii_to_bytes(ascii_str, 'strict')
print(bytes_again == bytes_obj)  # Output: True
```

### ascii_to_bytes()

Converts an ASCII string into a bytes-like object.

```python
# Example usage:
ascii_str = 'test'
bytes_obj = binascii.ascii_to_bytes(ascii_str, 'strict')
print(bytes_obj == b'\xc3\xbctest')  # Output: True
```

### encode(), decode()

Support for encoding and decoding strings to/from bytes using various encodings.

```python
# Example usage:
str_obj = 'Hello, World!'
bytes_obj = str_obj.encode('ascii', 'strict')
print(bytes_obj)  # Output: b'Hello, World!'

# Convert back to string
decoded_str = binascii.decodebytes(bytes_obj).decode('utf-8')
print(decoded_str == str_obj)  # Output: True

str_obj = b'\xc3\xbctest'
str_again = binascii.decodebytes(str_obj).decode('utf-8')
print(str_again == 'test')  # Output: True
```

### errors parameter for encode(), decode()

Specifies how to handle encoding and decoding errors.

```python
# Example usage:
str_obj = b'\xc3\xbctest'
encoded_bytes = str_obj.encode('ascii', 'ignore')
print(encoded_bytes)  # Output: b'test'

decoded_str = binascii.decodebytes(encoded_bytes).decode('utf-8')
print(decoded_str == 'test')  # Output: True
```

### validate()

Validates whether the input is a valid binary data.

```python
# Example usage:
valid_data = b'Hello, World!'
invalid_data = b'Goodbye, World!'

try:
    binascii.validate(valid_data)
except ValueError:
    print("Invalid data")

try:
    binascii.validate(invalid_data)
except ValueError:
    print("Invalid data")
```

### warnings parameter for validate()

Controls whether to issue a warning if the input is invalid.

```python
# Example usage:
valid_data = b'Hello, World!'
invalid_data = b'\x00'  # null byte

try:
    binascii.validate(valid_data)
except ValueError as e:
    print("Valid data")

try:
    binascii.validate(invalid_data, warnings=False)
except ValueError as e:
    print(e)  # Output: Invalid data
```
