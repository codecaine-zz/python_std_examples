# hmac - Keyed-Hashing for Message Authentication
## Table of Contents

1. [Example 1: Creating an HMAC Using SHA-256](#example-1-creating-an-hmac-using-sha-256)
2. [Example 2: Creating an HMAC Using SHA-1](#example-2-creating-an-hmac-using-sha-1)
3. [Example 3: Verifying an HMAC](#example-3-verifying-an-hmac)
4. [Example 4: Using `hmac.compare_digest` for Safe Comparison](#example-4-using-hmaccompare_digest-for-safe-comparison)
5. [Example 5: Creating an HMAC with Additional Data](#example-5-creating-an-hmac-with-additional-data)



The `hmac` module in Python provides a way to create message authentication codes (MACs) using cryptographic hash functions such as SHA-1, SHA-256, etc. A MAC is a fixed-size binary value that verifies the integrity of a message and ensures it hasn't been tampered with during transmission or storage.

Below are comprehensive examples for various functionalities in the `hmac` module:

### Example 1: Creating an HMAC Using SHA-256

```python
import hmac
import hashlib

# Define a secret key and a message
secret_key = b'secret_key'
message = b'This is a test message'

# Create an HMAC object using SHA-256 and the secret key
hmac_obj = hmac.new(secret_key, msg=message, digestmod=hashlib.sha256)

# Calculate and print the MAC value
mac_value = hmac_obj.digest()
print(f"SHA-256 HMAC: {mac_value.hex()}")
```

### Example 2: Creating an HMAC Using SHA-1

```python
import hmac
import hashlib

# Define a secret key and a message
secret_key = b'secret_key'
message = b'This is a test message'

# Create an HMAC object using SHA-1 and the secret key
hmac_obj = hmac.new(secret_key, msg=message, digestmod=hashlib.sha1)

# Calculate and print the MAC value
mac_value = hmac_obj.digest()
print(f"SHA-1 HMAC: {mac_value.hex()}")
```

### Example 3: Verifying an HMAC

```python
import hmac
import hashlib

# Define a secret key and a message
secret_key = b'secret_key'
message = b'This is a test message'

# Calculate the expected MAC value using SHA-256
expected_mac_value = b'expected_mac_value'  # Replace with the actual expected MAC value

# Create an HMAC object using SHA-256 and the secret key
hmac_obj = hmac.new(secret_key, msg=message, digestmod=hashlib.sha256)

# Calculate the actual MAC value
actual_mac_value = hmac_obj.digest()

# Verify if the calculated MAC matches the expected MAC
if hmac.compare_digest(actual_mac_value, expected_mac_value):
    print("The HMAC is valid.")
else:
    print("The HMAC is invalid.")
```

### Example 4: Using `hmac.compare_digest` for Safe Comparison

```python
import hmac

# Define two MAC values to compare safely
mac1 = b'6c967015e832e1d8f9b7b21a45d8b238'
mac2 = b'6c967015e832e1d8f9b7b21a45d8b238'

# Compare the MACs safely
if hmac.compare_digest(mac1, mac2):
    print("The MACs are identical.")
else:
    print("The MACs differ.")

# Note: Use `hmac.compare_digest` to securely compare MACs to prevent timing attacks.
```

### Example 5: Creating an HMAC with Additional Data

```python
import hmac
import hashlib

# Define a secret key, message, and additional data
secret_key = b'secret_key'
message = b'This is a test message'
additional_data = b'Additional information'

# Create an HMAC object using SHA-256 and the secret key, including additional data
hmac_obj = hmac.new(secret_key, msg=message + additional_data, digestmod=hashlib.sha256)

# Calculate and print the MAC value
mac_value = hmac_obj.digest()
print(f"SHA-256 HMAC with additional data: {mac_value.hex()}")
```

These examples demonstrate how to use the `hmac` module to create, calculate, verify, and compare HMAC values securely. Each example is well-documented with comments explaining the purpose of each part of the code.
