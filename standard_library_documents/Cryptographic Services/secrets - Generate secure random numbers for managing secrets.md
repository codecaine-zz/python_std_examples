# secrets — Generate secure random numbers for managing secrets

**Secrets Module Code Examples**
=====================================

### Overview

The `secrets` module provides an implementation of the cryptographically secure pseudo-random number generator (CSPRNG) as defined in RFC 4086.

### Example Use Cases

* Generating passwords
* Managing cryptographic keys
* Creating secure tokens

### Code Examples

#### 1. Generate a Random Integer

```python
import secrets

# Generate a random integer between 0 and 100
random_int = secrets.randbelow(101)
print(random_int)

# Generate a random float between 0 and 10
random_float = secrets.randbelow(11) / 10
print(random_float)
```

#### 2. Generate a Random Byte String

```python
import secrets

# Generate a random byte string of length 16 (128 bits)
random_bytes = secrets.token_bytes(16)
print(random_bytes.hex())  # Print the bytes as a hexadecimal string

# Generate a random byte string of length 32 (256 bits)
random_bytes_long = secrets.token_bytes(32)
print(random_bytes_long.hex())
```

#### 3. Generate a Random String

```python
import secrets
import string

# Set the character set for the random string
char_set = string.ascii_letters + string.digits

# Generate a random string of length 10
random_string = ''.join(secrets.choice(char_set) for _ in range(10))
print(random_string)

# Generate a random password of length 12 (using uppercase and lowercase letters, digits, and punctuation)
random_password = ''.join(
    secrets.choice(string.ascii_letters + string.digits + string.punctuation) 
    for _ in range(12)
)
print(random_password)
```

#### 4. Generate a URL-safe Random String

```python
import secrets
import string

# Set the character set for the random string (URL-safe)
char_set = string.ascii_letters + string.digits + '-_'

# Generate a random string of length 16
random_url_safe_string = ''.join(
    secrets.choice(char_set) 
    for _ in range(16)
)
print(random_url_safe_string)
```

#### 5. Generate a Random Token

```python
import secrets
import hashlib

# Set the token length (e.g., 32 characters)
token_length = 32

# Generate a random byte string of the specified length
random_bytes = secrets.token_bytes(token_length)

# Hash the byte string using SHA-256
token_hash = hashlib.sha256(random_bytes).hexdigest()
print(token_hash)

# Use the first token_length/2 characters as the final token
final_token = token_hash[:token_length // 2]
print(final_token)
```

### Notes

* The `secrets` module is designed to generate cryptographically secure random numbers, making it suitable for managing secrets and cryptographic keys.
* Always use the `secrets` module instead of `random` or other non-cryptographically secure modules when generating random numbers for security-sensitive applications.
