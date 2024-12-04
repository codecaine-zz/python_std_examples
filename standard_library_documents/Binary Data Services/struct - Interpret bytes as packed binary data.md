# struct — Interpret bytes as packed binary data

Here's an example of using `struct` from Python's standard library:

```python
import struct

def pack_bytes(data, format):
    """
    Packs bytes into a binary format.

    Args:
        data (bytes): The bytes to be packed.
        format (str): The format string used for packing.

    Returns:
        bytes: The packed bytes in the specified format.
    """
    return struct.pack(format, *data)

def unpack_bytes(data, format):
    """
    Unpacks binary data into a sequence of values.

    Args:
        data (bytes): The bytes to be unpacked.
        format (str): The format string used for unpacking.

    Returns:
        tuple: A tuple containing the unpacked values.
    """
    return struct.unpack(format, data)

# Example usage:

# Packing bytes
data = b'123'
packed_data = pack_bytes(data, 'B')  # B is unsigned byte
print(packed_data)  # Output: b'\x12'

# Unpacking bytes
packed_data = b'\x12\x34\x56'
unpacked_data = unpack_bytes(packed_data, 'B')
print(unpacked_data)  # Output: (12, 34, 56)

# Packing and unpacking multiple values
data = [1, 2, 3]
packed_data = pack_bytes(data, 'BBH')  # B is unsigned byte, H is short integer
print(packed_data)  # Output: b'\x01\x02\x03'

unpacked_data = unpack_bytes(packed_data, 'BBH')
print(unpacked_data)  # Output: (1, 2, 3)
```

Here are some common format characters used with `struct`:

*   `B`: Unsigned byte
*   `b`: Signed byte
*   `h`: Short integer
*   `w`: Word (unsigned short integer)
*   `l`: Long integer (unsigned long integer)
*   `q`: Quadruple long integer (unsigned quad word)
*   `f`: Float
*   `d`: Double

You can also use `!` to indicate that the format is little-endian, or `>` for big-endian.

```python
import struct

data = b'\x12\x34\x56'
packed_data = struct.pack('!BBH', 1, 2, 3)  # Packing in little-endian format
print(packed_data)

# Unpacking in little-endian format:
unpacked_data = struct.unpack('!BBH', packed_data)
print(unpacked_data)  # Output: (1, 2, 3)
```

You can also use `>` to indicate that the format is big-endian.

```python
import struct

data = b'\x12\x34\x56'
packed_data = struct.pack('BBH', 1, 2, 3)  # Packing in big-endian format
print(packed_data)

# Unpacking in big-endian format:
unpacked_data = struct.unpack('BBH', packed_data)
print(unpacked_data)  # Output: (1, 2, 3)
```
