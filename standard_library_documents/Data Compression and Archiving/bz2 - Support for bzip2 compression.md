# bz2 — Support for bzip2 compression

**Bz2 Module Example**
=====================================

### Table of Contents

1. [Module Description](#module-description)
2. [Importing the Bz2 Module](#importing-the-bz2-module)
3. [Compression and Decompression](#compression-and-decompression)
4. [Creating a Bz2 Compressor/Decompressor](#creating-a-bz2-compressordecompressor)

### Module Description

The `bz2` module provides support for bzip2 compression.

### Importing the Bz2 Module

```python
import bz2
```

### Compression and Decompression

You can use the `compressobj()` function to create a compressor/decompressor object:

```python
# Create a compressor/decompressor object
compressor = bz2.BZ2Compressor()
decompressor = bz2.BZ2Decompressor()

# Compress data
data = b"Hello, World!"
compressed_data = compressor.compress(data)
print(compressed_data)

# Decompress data
uncompressed_data = decompressor.decompress(compressed_data)
print(uncompressed_data)  # Output: b"Hello, World!"
```

### Creating a Bz2 Compressor/Decompressor

You can create a compressor/decompressor object directly:

```python
# Create a compressor/decompressor object
compressor = bz2.BZ2Compressor(level=9)
decompressor = bz2.BZ2Decompressor()

# Compress data
data = b"Hello, World!"
compressed_data = compressor.compress(data)
print(compressed_data)

# Decompress data
uncompressed_data = decompressor.decompress(compressed_data)
print(uncompressed_data)  # Output: b"Hello, World!"

# Set compression level (1-9)
compressor = bz2.BZ2Compressor(level=7)
decompressor = bz2.BZ2Decompressor()

# Compress data
data = b"Hello, World!"
compressed_data = compressor.compress(data)
print(compressed_data)

# Decompress data
uncompressed_data = decompressor.decompress(compressed_data)
print(uncompressed_data)  # Output: b"Hello, World!"

# Set the compression dictionary (dictionnaire de compresssion)
compressor_dict = bz2.BZ2Compressor(level=7, dict_level=-1)
decompressor_dict = bz2.BZ2Decompressor(dict_level=-1)

# Compress data
data = b"Hello, World!"
compressed_data = compressor_dict.compress(data)
print(compressed_data)

# Decompress data
uncompressed_data = decompressor_dict.decompress(compressed_data)
print(uncompressed_data)  # Output: b"Hello, World!"
```

### Creating a Bz2 Compressor/Decompressor with File Handling

```python
import bz2

def compress_file(input_filename, output_filename):
    with open(input_filename, 'rb') as f_in:
        data = f_in.read()
    
    # Create a compressor/decompressor object
    compressor = bz2.BZ2Compressor(level=9)
    decompressor = bz2.BZ2Decompressor()

    # Compress data
    compressed_data = compressor.compress(data)

    with open(output_filename, 'wb') as f_out:
        f_out.write(compressed_data)

def decompress_file(input_filename, output_filename):
    with open(input_filename, 'rb') as f_in:
        data = f_in.read()

    # Create a compressor/decompressor object
    decompressor = bz2.BZ2Decompressor()

    # Decompress data
    uncompressed_data = decompressor.decompress(data)

    with open(output_filename, 'wb') as f_out:
        f_out.write(uncompressed_data)

# Example usage:
compress_file('input.txt', 'output.b64')
decompress_file('output.b64', 'output_uncompressed.txt')
```
