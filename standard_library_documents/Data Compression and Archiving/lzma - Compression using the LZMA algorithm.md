# lzma - Compression using the LZMA algorithm

The `lzma` module in Python provides support for compressing and decompressing files using the LZMA compression algorithm, which is a variant of the DEFLATE algorithm with extra features such as checksums and better compression ratios.

Below are comprehensive examples demonstrating various functionalities of the `lzma` module. These examples are designed to be clear, concise, and suitable for inclusion in official documentation.

### Example 1: Compressing Data Using LZMA

This example demonstrates how to compress a string using the `lzma` module.

```python
import lzma

# Original data to be compressed
data = b'This is a sample string to be compressed using the LZMA algorithm.'

# Compress the data
compressed_data = lzma.compress(data)

# Print the original and compressed data lengths
print(f'Original Data Length: {len(data)} bytes')
print(f'Compressed Data Length: {len(compressed_data)} bytes')

# Optionally, print the compressed data as a hexadecimal string for comparison
print('Compressed Data (hex):', compressed_data.hex())
```

### Example 2: Decompressing Data Using LZMA

This example demonstrates how to decompress data that was previously compressed using the `lzma` module.

```python
import lzma

# Compressed data from the previous example
compressed_data = b'\x5d\x00\x63\x00\x1b\x00\x08\x00\x97\x00\x2b\x00\x08\x00\xab\x00\x08\x00\x14\x00\x0f\x00\x0c\x00\x0e\x00\x1a\x00\x0c\x00\x13\x00\x06\x00\x0d\x00\x2b\x00\x1a\x00\x08\x00\xab\x00\x08\x00\x14\x00\x0f\x00\x0c\x00\x0e\x00\x1a\x00\x0c\x00\x13\x00\x06\x00\x0d\x00\x2b\x00\x1a\x00\x08\x00\xab\x00\x08\x00\x14\x00\x0f\x00\x0c\x00\x0e\x00\x1a\x00\x0c\x00\x13\x00\x06\x00\x0d\x00\x2b\x00\x1a\x00\x08\x00\xab\x00\x08\x00\x14\x00\x0f\x00\x0c\x00\x0e\x00\x1a\x00\x0c\x00\x13\x00\x06\x00\x0d\x00\x2b\x00\x1a\x00\x08\x00\xab\x00\x08\x00\x14\x00\x0f\x00\x0c\x00\x0e\x00\x1a\x00\x0c\x00\x13\x00\x06\x00\x0d\x00'

# Decompress the data
decompressed_data = lzma.decompress(compressed_data)

# Print the decompressed data
print('Decompressed Data:', decompressed_data.decode('utf-8'))
```

### Example 3: Using Compression Levels

This example demonstrates how to specify different compression levels when compressing data. The higher the level, the more compressed the output but at the cost of increased processing time.

```python
import lzma

# Original data to be compressed
data = b'This is a sample string to be compressed using the LZMA algorithm.'

# Compress data with different levels (0-9)
compressed_data_level_0 = lzma.compress(data, level=0)  # No compression
compressed_data_level_1 = lzma.compress(data, level=1)  # Basic compression
compressed_data_level_9 = lzma.compress(data, level=9)  # Maximum compression

# Print the lengths of compressed data for each level
print(f'Compressed Data (Level 0): {len(compressed_data_level_0)} bytes')
print(f'Compressed Data (Level 1): {len(compressed_data_level_1)} bytes')
print(f'Compressed Data (Level 9): {len(compressed_data_level_9)} bytes')

# Optionally, print the compressed data as a hexadecimal string for comparison
for level, compressed_data in zip([0, 1, 9], [compressed_data_level_0, compressed_data_level_1, compressed_data_level_9]):
    print(f'Compressed Data (Level {level}):', compressed_data.hex())
```

### Example 4: Using File Compression

This example demonstrates how to compress a file using the `lzma` module.

```python
import lzma
import os

# Original file path
original_file_path = 'example.txt'

# Destination file path for the compressed data
compressed_file_path = original_file_path + '.xz'

# Check if the original file exists
if not os.path.exists(original_file_path):
    print('Original file does not exist.')
else:
    # Open the original file in binary read mode
    with open(original_file_path, 'rb') as f_in:
        # Compress the file and write to the compressed file
        with lzma.open(compressed_file_path, 'wb') as f_out:
            f_out.write(f_in.read())

    print('File compressed successfully:', compressed_file_path)
```

### Example 5: Using File Decompression

This example demonstrates how to decompress a file that was previously compressed using the `lzma` module.

```python
import lzma
import os

# Compressed file path
compressed_file_path = 'example.txt.xz'

# Destination file path for the decompressed data
decompressed_file_path = compressed_file_path.replace('.xz', '')

# Check if the compressed file exists
if not os.path.exists(compressed_file_path):
    print('Compressed file does not exist.')
else:
    # Open the compressed file in binary read mode
    with lzma.open(compressed_file_path, 'rb') as f_in:
        # Decompress the file and write to the decompressed file
        with open(decompressed_file_path, 'wb') as f_out:
            f_out.write(f_in.read())

    print('File decompressed successfully:', decompressed_file_path)
```

### Example 6: Using File Compression in a Context Manager

This example demonstrates how to compress and decompress files using the `lzma` module with a context manager.

```python
import lzma
import os

def compress_file(input_file, output_file):
    """Compress a file using LZMA."""
    with open(input_file, 'rb') as f_in:
        with lzma.open(output_file, 'wb') as f_out:
            f_out.write(f_in.read())

def decompress_file(input_file, output_file):
    """Decompress a file using LZMA."""
    with lzma.open(input_file, 'rb') as f_in:
        with open(output_file, 'wb') as f_out:
            f_out.write(f_in.read())

# Original file path
original_file_path = 'example.txt'

# Destination files for compressed and decompressed data
compressed_file_path = original_file_path + '.xz'
decompressed_file_path = compressed_file_path.replace('.xz', '')

# Compress the file
compress_file(original_file_path, compressed_file_path)
print('File compressed successfully:', compressed_file_path)

# Decompress the file
decompress_file(compressed_file_path, decompressed_file_path)
print('File decompressed successfully:', decompressed_file_path)
```

These examples cover various aspects of using the `lzma` module, including compression and decompression of strings, files, and specifying different compression levels. They are designed to be clear, concise, and suitable for inclusion in official documentation to help users understand how to leverage the LZMA compression algorithm in their Python projects.
