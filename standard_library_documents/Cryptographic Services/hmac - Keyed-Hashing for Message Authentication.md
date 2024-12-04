# hmac — Keyed-Hashing for Message Authentication

Here's an example of how you can use the `hmac` module from Python's standard library:

```python
# Import the hmac module from the standard library
import hmac

def generate_hmac(key, message):
    """
    Generates a HMAC (Keyed-Hashing for Message Authentication) object.

    Args:
        key (bytes): The secret key used to authenticate the message.
        message (bytes): The message to be authenticated.

    Returns:
        hmac.HMAC: A HMAC object containing the authentication key and other metadata.
    """
    return hmac.new(key, message, hashlib.sha256)

def verify_hmac(key, message, expected_hmac):
    """
    Verifies a given HMAC against a secret key and expected HMAC value.

    Args:
        key (bytes): The secret key used to generate the expected HMAC.
        message (bytes): The message that was authenticated with the HMAC.
        expected_hmac (bytes): The expected HMAC value.

    Returns:
        bool: True if the provided HMAC matches the expected HMAC, False otherwise.
    """
    try:
        hmac_object = hmac.new(key, message, hashlib.sha256)
        return hmac.compare_digest(hmac_object.hexdigest(), expected_hmac)
    except ValueError as e:
        print(f"Error generating HMAC: {e}")
        return False

# Example usage
if __name__ == "__main__":
    # Generate a random key and a message
    import secrets
    key = secrets.token_bytes(32)  # Use a secret key of length 32 bytes
    message = b"Hello, World!"  # The message to be authenticated

    # Generate an HMAC object using the generated key and message
    hmac_object = generate_hmac(key, message)

    # Get the authentication key from the HMAC object
    auth_key = hmac_object.digest()

    # Verify the HMAC against the secret key and expected HMAC value
    expected_hmac = "1234567890abcdef"  # Replace with your expected HMAC value
    print("Verification result:", verify_hmac(key, message, expected_hmac))
```

Here's a breakdown of what each part of this example does:

1. **Generating an HMAC**: We create a new `hmac` object using the `generate_hmac` function. This takes our secret key and message as arguments.
2. **Verifying an HMAC**: The `verify_hmac` function checks whether a given HMAC matches our expected value. It uses the same secret key and provided HMAC value to compare them.

**Additional Functions in hmac**

1.  `hmac.new(key, msg=None, alg=None)` : Creates a new HMAC object with optional message and algorithm.
2.  `hmac.compare_digest(hmac_value1, hmac_value2)` : Compares two HMAC values for equality, considering the possibility of different byte orders.
3.  `hmac.new(key, msg=b'', digestmod=hashlib.sha256)` : Creates a new HMAC object using an optional message and digest algorithm.
4.  `hmac.compare_digest(hmac_object.hexdigest(), expected_hmac)` : Compares two HMAC values for equality using hexadecimal representation.
