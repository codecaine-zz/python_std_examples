# base64 — Base16, Base32, Base64, Base85 Data Encodings

**Base64 Module**
================

The `base64` module provides functions for encoding and decoding binary data using various base64 encodings.

### Functions

#### encode()

Encodes a string into bytes using the specified encoding.

```python
import base64

def encoded_bytes(s, encoding='utf-8'):
    """
    Encode a string into bytes using the specified encoding.
    
    Args:
        s (str): The string to be encoded.
        encoding (str): The encoding scheme. Defaults to 'utf-8'.
    
    Returns:
        bytes: The encoded bytes.
    """
    return base64.b64encode(s.encode(encoding))
```

#### decode()

Decodes a bytes object into a string using the specified encoding.

```python
def decoded_string(b, encoding='utf-8'):
    """
    Decode a bytes object into a string using the specified encoding.
    
    Args:
        b (bytes): The bytes to be decoded.
        encoding (str): The decoding scheme. Defaults to 'utf-8'.
    
    Returns:
        str: The decoded string.
    """
    return base64.b64decode(b).decode(encoding)
```

#### urlsafe_b64encode()

Encodes a bytes object into a URL-safe Base64-encoded bytes.

```python
import base64

def url_safe_encoded_bytes(b):
    """
    Encode a bytes object into a URL-safe Base64-encoded bytes.
    
    Args:
        b (bytes): The bytes to be encoded.
    
    Returns:
        bytes: The URL-safe Base64-encoded bytes.
    """
    return base64.urlsafe_b64encode(b)
```

#### urlsafe_b64decode()

Decodes a URL-safe Base64-encoded bytes into a bytes object.

```python
import base64

def url_safe_decoded_bytes(c):
    """
    Decode a URL-safe Base64-encoded bytes into a bytes object.
    
    Args:
        c (bytes): The URL-safe Base64-encoded bytes.
    
    Returns:
        bytes: The decoded bytes.
    """
    return base64.urlsafe_b64decode(c)
```

#### gcd()

Computes the greatest common divisor (GCD) of two integers.

```python
import math

def gcd(a, b):
    """
    Compute the greatest common divisor (GCD) of two integers.
    
    Args:
        a (int): The first integer.
        b (int): The second integer.
    
    Returns:
        int: The GCD of the two integers.
    """
    return math.gcd(a, b)
```

#### getbase()

Returns a string representing the specified base.

```python
import base64

def get_base(n):
    """
    Return a string representing the specified base.
    
    Args:
        n (int): The base to be represented as a string.
    
    Returns:
        str: A string representation of the base.
    """
    if n == 2:
        return 'binary'
    elif n == 8:
        return 'octal'
    else:
        return ''
```

#### isbase64()

Checks whether a bytes object represents valid Base64-encoded data.

```python
import base64

def is_base64(b):
    """
    Check whether a bytes object represents valid Base64-encoded data.
    
    Args:
        b (bytes): The bytes to be checked.
    
    Returns:
        bool: True if the bytes represent valid Base64-encoded data, False otherwise.
    """
    try:
        base64.b64decode(b)
        return True
    except ValueError:
        return False
```

### Example Usage

```python
# Encode a string into bytes using the 'utf-8' encoding scheme
encoded_bytes = encoded_bytes('Hello, World!')
print(encoded_bytes)

# Decode a bytes object into a string using the 'utf-8' decoding scheme
decoded_string = decoded_string(b'QXV0aGUgbGFzdCBpcyBhIHNpbmdz')
print(decoded_string)

# Encode a bytes object into a URL-safe Base64-encoded bytes
url_safe_encoded_bytes = url_safe_encoded_bytes(b'Hello, World!')
print(url_safe_encoded_bytes)

# Decode a URL-safe Base64-encoded bytes into a bytes object
url_safe_decoded_bytes = url_safe_decoded_bytes(c=b'SGVsbG8gd29ybGQ=')
print(url_safe_decoded_bytes)

# Compute the greatest common divisor (GCD) of two integers
gcd_value = gcd(12, 15)
print(gcd_value)

# Return a string representing the specified base
base_string = get_base(2)
print(base_string)

# Check whether a bytes object represents valid Base64-encoded data
is_valid_base64 = is_base64(b'QXV0aGUgbGFzdCBpcyBhIHNpbmdz')
print(is_valid_base64)
```
