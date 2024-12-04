# struct - Interpret bytes as packed binary data

The `struct` module in Python provides support for interpreting strings of bytes as packed binary data. It allows you to convert between binary data and native Python data types such as integers, floating-point numbers, and characters. Here are some comprehensive examples demonstrating various functionalities of the `struct` module:

### Example 1: Packing Binary Data

```python
import struct

# Pack an integer into bytes
int_value = 42
packed_int = struct.pack('>I', int_value)
print(f"Packed integer (big-endian): {packed_int}")

# Pack a float into bytes
float_value = 3.14
packed_float = struct.pack('>f', float_value)
print(f"Packed float (big-endian): {packed_float}")
```

### Example 2: Unpacking Binary Data

```python
import struct

# Unpack binary data back to an integer
packed_int = b'\x00\x00\x00\x46'
unpacked_int, consumed_bytes = struct.unpack('>I', packed_int)
print(f"Unpacked integer (big-endian): {unpacked_int}")
print(f"Number of bytes consumed: {consumed_bytes}")

# Unpack binary data back to a float
packed_float = b'\x00\x00\x80\x40'
unpacked_float, consumed_bytes = struct.unpack('>f', packed_float)
print(f"Unpacked float (big-endian): {unpacked_float}")
print(f"Number of bytes consumed: {consumed_bytes}")
```

### Example 3: Packing and Unpacking with Different Endianness

```python
import struct

# Pack an integer into big-endian bytes
int_value = 42
packed_int_big_endian = struct.pack('>I', int_value)
print(f"Packed integer (big-endian): {packed_int_big_endian}")

# Pack an integer into little-endian bytes
packed_int_little_endian = struct.pack('<I', int_value)
print(f"Packed integer (little-endian): {packed_int_little_endian}")

# Unpack big-endian packed data back to an integer
unpacked_int_from_big_endian, consumed_bytes = struct.unpack('>I', packed_int_big_endian)
print(f"Unpacked integer from big-endian: {unpacked_int_from_big_endian}")
print(f"Number of bytes consumed: {consumed_bytes}")

# Unpack little-endian packed data back to an integer
unpacked_int_from_little_endian, consumed_bytes = struct.unpack('<I', packed_int_little_endian)
print(f"Unpacked integer from little-endian: {unpacked_int_from_little_endian}")
print(f"Number of bytes consumed: {consumed_bytes}")
```

### Example 4: Using `struct.calcsize` to Determine the Size of a Format String

```python
import struct

# Define a format string
format_string = '>I'

# Calculate the size of the packed data based on the format string
size = struct.calcsize(format_string)
print(f"Size of the packed data in bytes: {size}")
```

### Example 5: Handling Variable-Length Packed Data

```python
import struct

# Pack a variable-length list of integers into bytes
int_values = [1, 2, 3, 4, 5]
packed_ints = b''.join(struct.pack('>I', value) for value in int_values)
print(f"Packed list of integers (big-endian): {packed_ints}")

# Unpack the packed data back to a list of integers
unpacked_ints, consumed_bytes = struct.unpack('>' + 'I' * len(int_values), packed_ints)
print(f"Unpacked list of integers: {unpacked_ints}")
```

### Example 6: Handling Special Characters and Strings

```python
import struct

# Pack a string into bytes using ASCII encoding
string_value = "Hello, World!"
packed_string = struct.pack('13s', string_value.encode('ascii'))
print(f"Packed string (using ASCII): {packed_string}")

# Unpack the packed string back to a Python string
unpacked_string, consumed_bytes = struct.unpack('13s', packed_string)
print(f"Unpacked string: {unpacked_string.decode('ascii')}")
```

### Example 7: Handling Non-ASCII Characters

```python
import struct

# Pack a string into bytes using UTF-8 encoding
string_value = "Hello, World!"
packed_string_utf8 = struct.pack('>32s', string_value.encode('utf-8'))
print(f"Packed string (using UTF-8): {packed_string_utf8}")

# Unpack the packed string back to a Python string
unpacked_string_utf8, consumed_bytes = struct.unpack('>32s', packed_string_utf8)
print(f"Unpacked string: {unpacked_string_utf8.decode('utf-8')}")
```

### Example 8: Handling Variable-Length Strings

```python
import struct

# Pack a list of variable-length strings into bytes using ASCII encoding
string_values = ["Hello", "World", "!"]
packed_strings = b''.join(struct.pack('32s', value.encode('ascii')) for value in string_values)
print(f"Packed list of strings (using ASCII): {packed_strings}")

# Unpack the packed strings back to a list of Python strings
unpacked_strings, consumed_bytes = struct.unpack('>I' + '32s' * len(string_values), packed_strings)
unpacked_strings = [value.decode('ascii') for value in unpacked_strings[1:]]
print(f"Unpacked list of strings: {unpacked_strings}")
```

### Example 9: Handling Variable-Length Packed Data with a Fixed Length Prefix

```python
import struct

# Pack a variable-length list of integers into bytes, prefixed by the count
int_values = [1, 2, 3, 4, 5]
count = len(int_values)
packed_ints_with_count = struct.pack('>I' + 'I' * count, count) + b''.join(struct.pack('>I', value) for value in int_values)
print(f"Packed list of integers with count (big-endian): {packed_ints_with_count}")

# Unpack the packed data back to a list of integers
unpacked_count = struct.unpack('>I', packed_ints_with_count[:4])[0]
unpacked_ints, consumed_bytes = struct.unpack('>' + 'I' * unpacked_count, packed_ints_with_count[4:])
print(f"Unpacked count: {unpacked_count}")
print(f"Unpacked list of integers: {unpacked_ints}")
```

These examples cover various scenarios involving the `struct` module, from basic integer and float packing to more complex cases such as variable-length lists and strings. Each example includes comments explaining key aspects, making it easy to understand and use in real-world applications.
