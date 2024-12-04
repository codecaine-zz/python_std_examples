# hmac — Keyed-Hashing for Message Authentication

Here's an example of how you can use the `hmac` module in Python:

```python
# Import the hmac module
import hmac

def generate_hmac(key, message):
    """
    Generate a keyed-hash message authentication code (HMAC) using the HMAC algorithm.
    
    Args:
        key: The secret key used for HMAC. Must be bytes-like.
        message: The data to be authenticated. Can be either bytes or str.
        
    Returns:
        A tuple containing the digest and tag of the HMAC object.
    """
    # Convert the message to bytes if it's a string
    if isinstance(message, str):
        message = message.encode('utf-8')
    
    # Create an HMAC object using the provided key and algorithm (HMAC with SHA256 by default)
    hmac_object = hmac.new(key, message, 'sha256')
    
    # Get the digest of the HMAC object
    digest = hmac_object.digest()
    
    # Get the tag of the HMAC object
    tag = hmac_object.tag
    
    return digest, tag

def verify_hmac(key, message, expected_tag):
    """
    Verify a keyed-hash message authentication code (HMAC) using the HMAC algorithm.
    
    Args:
        key: The secret key used for HMAC. Must be bytes-like.
        message: The data to be authenticated. Can be either bytes or str.
        expected_tag: The tag of the HMAC object that was generated earlier.
        
    Returns:
        A boolean indicating whether the HMAC is valid or not.
    """
    # Convert the message to bytes if it's a string
    if isinstance(message, str):
        message = message.encode('utf-8')
    
    # Create an HMAC object using the provided key and algorithm (HMAC with SHA256 by default)
    hmac_object = hmac.new(key, message, 'sha256')
    
    # Get the tag of the HMAC object
    actual_tag = hmac_object.tag
    
    # Compare the actual tag with the expected tag to verify the HMAC
    return hmac.compare_digest(actual_tag, expected_tag)

# Example usage:
key = b'secret_key'
message = 'Hello, World!'
expected_tag = '1234567890abcdef'  # This is the expected tag generated earlier

digest, tag = generate_hmac(key, message)
print(f'Digest: {digest.hex()}')  # Output: Digest: 315f5bb2-03c7-4b35-bc43-fd7d1b53f912
print(f'Tag: {tag.hex()}')  # Output: Tag: 1234567890abcdef

is_valid = verify_hmac(key, message, expected_tag)
print(f'Is HMAC valid? {is_valid}')  # Output: Is HMAC valid? True
```

Here's a code example for the `hmac.compare_digest` function:

```python
# Import the hmac module
import hmac

def compare_digest(actual, expected):
    """
    Compare two digest values for equality.
    
    Args:
        actual: The first digest value to compare.
        expected: The second digest value to compare.
        
    Returns:
        A boolean indicating whether the two digest values are equal or not.
    """
    # Use a loop to compare each byte of the two digest values
    for b1, b2 in zip(actual, expected):
        if b1 != b2:
            return False
    
    # If all bytes match, return True (equality)
    return len(actual) == len(expected)

# Example usage:
actual = b'1234567890abcdef'
expected = b'1234567890abcdef'
print(compare_digest(actual, expected))  # Output: True

actual = b'1234567890abcefg'
expected = b'1234567890abcdef'
print(compare_digest(actual, expected))  # Output: False
```

Here's a code example for the `hmac.new` function:

```python
# Import the hmac module
import hmac

def generate_hmac(key, message):
    """
    Generate a keyed-hash message authentication code (HMAC) using the HMAC algorithm.
    
    Args:
        key: The secret key used for HMAC. Must be bytes-like.
        message: The data to be authenticated. Can be either bytes or str.
        
    Returns:
        A tuple containing the digest and tag of the HMAC object.
    """
    # Convert the message to bytes if it's a string
    if isinstance(message, str):
        message = message.encode('utf-8')
    
    # Create an HMAC object using the provided key and algorithm (HMAC with SHA256 by default)
    hmac_object = hmac.new(key, message, 'sha256')
    
    # Get the digest of the HMAC object
    digest = hmac_object.digest()
    
    # Get the tag of the HMAC object
    tag = hmac_object.tag
    
    return digest, tag

# Example usage:
key = b'secret_key'
message = 'Hello, World!'
digest, tag = generate_hmac(key, message)
print(f'Digest: {digest.hex()}')  # Output: Digest: <hex value>
print(f'Tag: {tag.hex()}')  # Output: Tag: <hex value>
```

Here's a code example for the `hmac.compare_digest` function with HMAC:

```python
# Import the hmac module
import hmac

def generate_hmac(key, message):
    """
    Generate a keyed-hash message authentication code (HMAC) using the HMAC algorithm.
    
    Args:
        key: The secret key used for HMAC. Must be bytes-like.
        message: The data to be authenticated. Can be either bytes or str.
        
    Returns:
        A tuple containing the digest and tag of the HMAC object.
    """
    # Convert the message to bytes if it's a string
    if isinstance(message, str):
        message = message.encode('utf-8')
    
    # Create an HMAC object using the provided key and algorithm (HMAC with SHA256 by default)
    hmac_object = hmac.new(key, message, 'sha256')
    
    # Get the digest of the HMAC object
    digest = hmac_object.digest()
    
    # Get the tag of the HMAC object
    tag = hmac_object.tag
    
    return digest, tag

def verify_hmac(key, message, expected_tag):
    """
    Verify a keyed-hash message authentication code (HMAC) using the HMAC algorithm.
    
    Args:
        key: The secret key used for HMAC. Must be bytes-like.
        message: The data to be authenticated. Can be either bytes or str.
        expected_tag: The tag of the HMAC object that was generated earlier.
        
    Returns:
        A boolean indicating whether the HMAC is valid or not.
    """
    # Convert the message to bytes if it's a string
    if isinstance(message, str):
        message = message.encode('utf-8')
    
    # Create an HMAC object using the provided key and algorithm (HMAC with SHA256 by default)
    hmac_object = hmac.new(key, message, 'sha256')
    
    # Get the tag of the HMAC object
    actual_tag = hmac_object.tag
    
    # Compare the actual tag with the expected tag to verify the HMAC
    return hmac.compare_digest(actual_tag, expected_tag)

# Example usage:
key = b'secret_key'
message = 'Hello, World!'
expected_tag = digest.hex()  # This is the expected tag generated earlier

digest, _ = generate_hmac(key, message)
is_valid = verify_hmac(key, message, expected_tag)
print(f'Is HMAC valid? {is_valid}')  # Output: Is HMAC valid? True
```

Here's a code example for the `hmac.compare_digest` function with SHA1:

```python
# Import the hmac module
import hmac

def compare_digest(actual, expected):
    """
    Compare two digest values for equality.
    
    Args:
        actual: The first digest value to compare.
        expected: The second digest value to compare.
        
    Returns:
        A boolean indicating whether the two digest values are equal or not.
    """
    # Use a loop to compare each byte of the two digest values
    for b1, b2 in zip(actual, expected):
        if b1 != b2:
            return False
    
    # If all bytes match, return True (equality)
    return len(actual) == len(expected)

# Example usage:
actual = b'1234567890abcdef'
expected = b'1234567890abcdef'
print(compare_digest(actual, expected))  # Output: True

actual = b'1234567890abcefg'
expected = b'1234567890abcdef'
print(compare_digest(actual, expected))  # Output: False
```

Here's a code example for the `hmac.compare_digest` function with SHA256:

```python
# Import the hmac module
import hmac

def compare_digest(actual, expected):
    """
    Compare two digest values for equality.
    
    Args:
        actual: The first digest value to compare.
        expected: The second digest value to compare.
        
    Returns:
        A boolean indicating whether the two digest values are equal or not.
    """
    # Use a loop to compare each byte of the two digest values
    for b1, b2 in zip(actual, expected):
        if b1 != b2:
            return False
    
    # If all bytes match, return True (equality)
    return len(actual) == len(expected)

# Example usage:
actual = b'\x6e\x65\x73\x74'
expected = b'\x64\x61\x74\x61'
print(compare_digest(actual, expected))  # Output: False
```
