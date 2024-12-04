# quopri - Encode and decode MIME quoted-printable data

The `quopri` module in Python is used to encode and decode MIME quoted-printable (QP) encoded strings, which are often used in email headers. Below are comprehensive examples demonstrating how to use this module for encoding and decoding QP data.

### Encoding QP Data

QP encoding converts binary data into a printable format that can be safely transmitted over ASCII-based media like email headers. Here's an example of how to encode binary data using the `quopri` module:

```python
import quopri

def encode_qp_string(input_data):
    # Convert the input data to bytes if it isn't already
    if not isinstance(input_data, bytes):
        input_data = input_data.encode('utf-8')
    
    # Encode the binary data using QP encoding
    encoded_data = quopri.encodestring(input_data)
    
    return encoded_data.decode()

# Example usage
if __name__ == "__main__":
    original_message = "Hello, world! This is a test message with special characters like ñ and €."
    encoded_message = encode_qp_string(original_message)
    print("Original Message:", original_message)
    print("Encoded QP Message:", encoded_message)
```

### Decoding QP Data

Decoding QP encoded strings back to their original binary form can be done using the `quopri` module. Here's an example of how to decode a QP encoded string:

```python
import quopri

def decode_qp_string(encoded_data):
    # Decode the QP encoded data back to bytes
    decoded_bytes = quopri.decodestring(encoded_data)
    
    # Convert the bytes back to a string if needed
    decoded_text = decoded_bytes.decode('utf-8')
    
    return decoded_text

# Example usage
if __name__ == "__main__":
    encoded_message = "Hello, world! This is a test message with special characters like =C3=BA and =E2=82=A2."
    original_message = decode_qp_string(encoded_message)
    print("Encoded QP Message:", encoded_message)
    print("Decoded Original Message:", original_message)
```

### Key Points

1. **Encoding**: The `quopri.encodestring()` function takes binary data as input and returns a QP encoded string.

2. **Decoding**: The `quopri.decodestring()` function takes a QP encoded string and returns the original bytes.

3. **Character Encoding**: Both encoding and decoding assume that the input data is in UTF-8, which is common for text strings. You can specify different encodings if needed by passing them as arguments to the `encode()` and `decode()` methods.

4. **Example Strings**: The example strings used are designed to demonstrate special characters (ñ and €) that might be encoded in QP format.

These examples provide a basic understanding of how to use the `quopri` module for encoding and decoding MIME quoted-printable data.
