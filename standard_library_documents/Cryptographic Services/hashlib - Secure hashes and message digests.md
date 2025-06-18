# hashlib - Secure hashes and message digests
## Table of Contents

1. [Example 1: Creating a Hash Object](#example-1-creating-a-hash-object)
2. [Example 2: Creating Multiple Hash Objects](#example-2-creating-multiple-hash-objects)
3. [Example 3: Using Hash Objects in a Context Manager](#example-3-using-hash-objects-in-a-context-manager)
4. [Example 4: Using Hash Objects with Input Streams](#example-4-using-hash-objects-with-input-streams)
5. [Example 5: Using Hash Objects with Binary Files](#example-5-using-hash-objects-with-binary-files)
6. [Example 6: Using Hash Objects with Custom Algorithms](#example-6-using-hash-objects-with-custom-algorithms)
7. [Example 7: Using Hash Objects with Different Data Types](#example-7-using-hash-objects-with-different-data-types)



The `hashlib` module in Python provides access to secure hash and message digest algorithms. It is part of the Python Standard Library, making it a fundamental tool for cryptographic operations. Below are comprehensive examples demonstrating various functionalities provided by the `hashlib` module.

### Example 1: Creating a Hash Object

```python
import hashlib

# Create a SHA-256 hash object
sha256_hash = hashlib.sha256()

# Update the hash object with some data
sha256_hash.update(b"Hello, World!")

# Get the hexadecimal representation of the hash
hex_digest = sha256_hash.hexdigest()
print("SHA-256 Hash:", hex_digest)
```

**Explanation**: This example demonstrates how to create a SHA-256 hash object using `hashlib.sha256()`. It then updates the hash with the byte string `"Hello, World!"` and retrieves the hexadecimal representation of the resulting hash.

### Example 2: Creating Multiple Hash Objects

```python
import hashlib

# Create multiple hash objects for different algorithms
md5_hash = hashlib.md5()
sha1_hash = hashlib.sha1()

# Update each hash object with some data
md5_hash.update(b"Secure hash and message digest")
sha1_hash.update(b"Secure hash and message digest")

# Get the hexadecimal representation of each hash
md5_hex_digest = md5_hash.hexdigest()
sha1_hex_digest = sha1_hash.hexdigest()

print("MD5 Hash:", md5_hex_digest)
print("SHA-1 Hash:", sha1_hex_digest)
```

**Explanation**: This example shows how to create multiple hash objects for different algorithms (MD5 and SHA-1) using `hashlib.md5()` and `hashlib.sha1()`, respectively. It updates each hash object with the byte string `"Secure hash and message digest"` and retrieves the hexadecimal representation of each resulting hash.

### Example 3: Using Hash Objects in a Context Manager

```python
import hashlib
from contextlib import contextmanager

@contextmanager
def compute_hash(algorithm):
    # Create a hash object using the specified algorithm
    hasher = hashlib.new(algorithm)
    
    try:
        yield hasher
    finally:
        # Update the hash with the bytes from the buffer
        hasher.update(b"Secure hash and message digest")
        print(f"{algorithm.capitalize()} Hash:", hasher.hexdigest())

# Use the context manager to compute a SHA-256 hash
with compute_hash("sha256") as sha256:
    pass
```

**Explanation**: This example demonstrates how to use the `hashlib.new()` function with a context manager (`contextlib.contextmanager`) to create a hash object for a specified algorithm. The hash object is updated with the byte string `"Secure hash and message digest"` in the context, and the final hexadecimal representation of the hash is printed upon exit.

### Example 4: Using Hash Objects with Input Streams

```python
import hashlib
from io import BytesIO

# Create a hash object using SHA-256
sha256_hash = hashlib.sha256()

# Create an input stream from a byte string
input_stream = BytesIO(b"Secure hash and message digest")

# Update the hash with data from the input stream
sha256_hash.update(input_stream.read())

# Get the hexadecimal representation of the hash
hex_digest = sha256_hash.hexdigest()
print("SHA-256 Hash from Stream:", hex_digest)

# Reset the input stream for re-use
input_stream.seek(0)
```

**Explanation**: This example shows how to create a SHA-256 hash object and update it with data read from an `io.BytesIO` object. The hash is then finalized, and the hexadecimal representation of the hash is printed. The input stream is reset for re-use.

### Example 5: Using Hash Objects with Binary Files

```python
import hashlib
from pathlib import Path

# Create a hash object using MD5
md5_hash = hashlib.md5()

# Open a binary file in read mode
with open(Path("example.txt"), "rb") as file:
    # Update the hash object with data from the file
    md5_hash.update(file.read())

# Get the hexadecimal representation of the hash
hex_digest = md5_hash.hexdigest()
print("MD5 Hash from File:", hex_digest)
```

**Explanation**: This example demonstrates how to create an MD5 hash object and update it with data read from a binary file using `Path` for file path handling. The hash is then finalized, and the hexadecimal representation of the hash is printed.

### Example 6: Using Hash Objects with Custom Algorithms

```python
import hashlib

# Define a custom hash algorithm (e.g., MD5-like)
def custom_hash(data):
    # Create an MD5 hash object
    md5_hash = hashlib.md5()
    
    # Update the hash object with the data
    md5_hash.update(data)
    
    # Return the hexadecimal representation of the hash
    return md5_hash.hexdigest()

# Use the custom hash function
custom_hex_digest = custom_hash(b"Custom hash example")
print("Custom Hash:", custom_hex_digest)
```

**Explanation**: This example demonstrates how to define a custom hash algorithm by creating an MD5 hash object and updating it with a given byte string. The hexadecimal representation of the custom hash is then printed.

### Example 7: Using Hash Objects with Different Data Types

```python
import hashlib

# Create a SHA-256 hash object
sha256_hash = hashlib.sha256()

# Update the hash object with integers, floats, and strings
sha256_hash.update(12345)
sha256_hash.update(3.14)
sha256_hash.update("Hello, World!")

# Get the hexadecimal representation of the hash
hex_digest = sha256_hash.hexdigest()
print("SHA-256 Hash with Mixed Data Types:", hex_digest)
```

**Explanation**: This example shows how to create a SHA-256 hash object and update it with integers (12345), floats (3.14), and strings ("Hello, World!"). The hash is then finalized, and the hexadecimal representation of the mixed data types hash is printed.

These examples cover various aspects of using the `hashlib` module, including creating different hash objects, updating them with different inputs, and using hash objects in context managers and streams.
