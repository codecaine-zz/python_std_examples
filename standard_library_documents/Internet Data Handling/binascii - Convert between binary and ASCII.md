# binascii - Convert between binary and ASCII

The `binascii` module in Python provides functions to convert between various binary formats, including hexadecimal, octal, and base64 encoding/decoding. Below are comprehensive code examples demonstrating each functionality of the `binascii` module.

### Example 1: Hexadecimal Encoding

```python
import binascii

def hex_encoding_example():
    """
    This example demonstrates how to convert a byte string to its hexadecimal representation.
    """
    # Define a sample binary data as bytes
    binary_data = b'Hello, World!'
    
    # Convert the binary data to hexadecimal format
    hex_representation = binascii.hexlify(binary_data)
    
    # Print the result
    print(f"Hexadecimal Representation: {hex_representation.decode('utf-8')}")

# Run the example function
hex_encoding_example()
```

### Example 2: Hexadecimal Decoding

```python
import binascii

def hex_decoding_example():
    """
    This example demonstrates how to convert a hexadecimal string back to its original byte data.
    """
    # Define a sample hexadecimal string
    hex_string = b'48656c6c6f2c20576f726c64'
    
    # Convert the hexadecimal string back to binary data
    binary_data = binascii.unhexlify(hex_string)
    
    # Print the result
    print(f"Original Binary Data: {binary_data.decode('utf-8')}")

# Run the example function
hex_decoding_example()
```

### Example 3: Octal Encoding

```python
import binascii

def octal_encoding_example():
    """
    This example demonstrates how to convert a byte string to its octal representation.
    Note: The output is in 'o' format which is not the standard octal, but rather an internal format used by Python.
    """
    # Define a sample binary data as bytes
    binary_data = b'Hello, World!'
    
    # Convert the binary data to octal format
    octal_representation = binascii.octlify(binary_data)
    
    # Print the result
    print(f"Octal Representation: {octal_representation.decode('utf-8')}")

# Run the example function
octal_encoding_example()
```

### Example 4: Base64 Encoding

```python
import binascii

def base64_encoding_example():
    """
    This example demonstrates how to convert a byte string to its Base64 representation.
    """
    # Define a sample binary data as bytes
    binary_data = b'Hello, World!'
    
    # Convert the binary data to Base64 format
    base64_representation = binascii.b64encode(binary_data)
    
    # Print the result
    print(f"Base64 Representation: {base64_representation.decode('utf-8')}")

# Run the example function
base64_encoding_example()
```

### Example 5: Base64 Decoding

```python
import binascii

def base64_decoding_example():
    """
    This example demonstrates how to convert a Base64 string back to its original byte data.
    """
    # Define a sample Base64 string
    base64_string = b'SGVsbG8sIFdvcmxkIQ=='
    
    # Convert the Base64 string back to binary data
    binary_data = binascii.b64decode(base64_string)
    
    # Print the result
    print(f"Original Binary Data: {binary_data.decode('utf-8')}")

# Run the example function
base64_decoding_example()
```

### Example 6: Binary to String Conversion

```python
import binascii

def binary_to_string_example():
    """
    This example demonstrates how to convert a byte string to its ASCII representation.
    """
    # Define a sample binary data as bytes
    binary_data = b'Hello, World!'
    
    # Convert the binary data to ASCII string
    ascii_representation = binary_data.decode('utf-8')
    
    # Print the result
    print(f"ASCII Representation: {ascii_representation}")

# Run the example function
binary_to_string_example()
```

### Example 7: String to Binary Conversion

```python
import binascii

def string_to_binary_example():
    """
    This example demonstrates how to convert an ASCII string back to its byte data.
    """
    # Define a sample ASCII string
    ascii_string = "Hello, World!"
    
    # Convert the ASCII string to binary data
    binary_data = ascii_string.encode('utf-8')
    
    # Print the result
    print(f"Binary Data: {binary_data}")

# Run the example function
string_to_binary_example()
```

### Example 8: Hexadecimal to String Conversion

```python
import binascii

def hex_to_string_example():
    """
    This example demonstrates how to convert a hexadecimal string back to its ASCII representation.
    """
    # Define a sample hexadecimal string
    hex_string = "48656c6c6f2c20576f726c64"
    
    # Convert the hexadecimal string to binary data
    binary_data = binascii.unhexlify(hex_string)
    
    # Convert the binary data back to ASCII string
    ascii_representation = binary_data.decode('utf-8')
    
    # Print the result
    print(f"ASCII Representation: {ascii_representation}")

# Run the example function
hex_to_string_example()
```

### Example 9: String to Hexadecimal Conversion

```python
import binascii

def string_to_hex_example():
    """
    This example demonstrates how to convert an ASCII string to its hexadecimal representation.
    """
    # Define a sample ASCII string
    ascii_string = "Hello, World!"
    
    # Convert the ASCII string to binary data
    binary_data = ascii_string.encode('utf-8')
    
    # Convert the binary data to hexadecimal format
    hex_representation = binascii.hexlify(binary_data)
    
    # Print the result
    print(f"Hexadecimal Representation: {hex_representation.decode('utf-8')}")

# Run the example function
string_to_hex_example()
```

### Example 10: Base64 to String Conversion

```python
import binascii

def base64_to_string_example():
    """
    This example demonstrates how to convert a Base64 string back to its ASCII representation.
    """
    # Define a sample Base64 string
    base64_string = "SGVsbG8sIFdvcmxkIQ=="
    
    # Convert the Base64 string to binary data
    binary_data = binascii.b64decode(base64_string)
    
    # Convert the binary data back to ASCII string
    ascii_representation = binary_data.decode('utf-8')
    
    # Print the result
    print(f"ASCII Representation: {ascii_representation}")

# Run the example function
base64_to_string_example()
```

### Example 11: String to Base64 Conversion

```python
import binascii

def string_to_base64_example():
    """
    This example demonstrates how to convert an ASCII string to its Base64 representation.
    """
    # Define a sample ASCII string
    ascii_string = "Hello, World!"
    
    # Convert the ASCII string to binary data
    binary_data = ascii_string.encode('utf-8')
    
    # Convert the binary data to Base64 format
    base64_representation = binascii.b64encode(binary_data)
    
    # Print the result
    print(f"Base64 Representation: {base64_representation.decode('utf-8')}")

# Run the example function
string_to_base64_example()
```

### Additional Examples

1. **Escape Sequences to Binary Conversion**:
   ```python
   import binascii

   def escape_sequences_to_binary():
       """
       This example demonstrates how to convert escape sequences in a string back to binary data.
       """
       # Define a sample string with escape sequences
       escape_string = "\x48\x65\x6c\x6c\x6f\x2c\x20\x57\x6f\x72\x6c\x64"
       
       # Convert the escape string to binary data
       binary_data = binascii.unhexlify(escape_string)
       
       # Print the result
       print(f"Binary Data: {binary_data.decode('utf-8')}")

   # Run the example function
   escape_sequences_to_binary()
   ```

2. **Binary to Escape Sequences Conversion**:
   ```python
   import binascii

   def binary_to_escape_sequences():
       """
       This example demonstrates how to convert binary data to its escape sequence representation.
       """
       # Define a sample byte string
       binary_data = b'Hello, World!'
       
       # Convert the binary data to hexadecimal format and then to escape sequences
       hex_representation = binascii.hexlify(binary_data)
       escape_sequences = "\\x" + "\\x".join(hex_representation.decode('utf-8'))
       
       # Print the result
       print(f"Escape Sequences: {escape_sequences}")

   # Run the example function
   binary_to_escape_sequences()
   ```

These examples cover a wide range of functionalities provided by the `binascii` module, from basic conversions to more complex operations involving escape sequences. Each example is self-contained and demonstrates a specific use case for converting between different data formats using Python's `binascii` library.
