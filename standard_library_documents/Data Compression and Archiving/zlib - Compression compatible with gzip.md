# zlib - Compression compatible with gzip
## Table of Contents

1. [1. Compressing Data](#1-compressing-data)
2. [2. Decompressing Compressed Data](#2-decompressing-compressed-data)
3. [3. Getting Compression and Decompression Statistics](#3-getting-compression-and-decompression-statistics)
4. [4. Handling Compressed Files with `zlib.decompressobj`](#4-handling-compressed-files-with-zlibdecompressobj)
5. [5. Using `zlib.compressobj` with Different Compression Levels](#5-using-zlibcompressobj-with-different-compression-levels)



Certainly! Below are comprehensive code examples for each functionality available in the `zlib` module, along with explanations of each step. These examples are designed to be clear, concise, and suitable for inclusion in official documentation.

### 1. Compressing Data

```python
import zlib

def compress_data(data):
    """
    Compresses input data using the zlib algorithm.

    Parameters:
    - data: bytes, the data to be compressed.

    Returns:
    - bytes, the compressed data.
    """
    # Create a compressor object with default settings (level 6)
    comp = zlib.compressobj(zlib.Z_DEFAULT_COMPRESSION)
    
    # Compress the input data
    compressed_data = comp.compress(data)
    compressed_data += comp.flush()
    
    return compressed_data

# Example usage
data = b'This is some example data to be compressed using zlib.'
compressed_data = compress_data(data)

print("Compressed Data:", compressed_data)
```

### 2. Decompressing Compressed Data

```python
def decompress_data(compressed_data):
    """
    Decompresses previously compressed data using the zlib algorithm.

    Parameters:
    - compressed_data: bytes, the data to be decompressed.

    Returns:
    - bytes, the decompressed original data.
    """
    # Create a decompressor object with default settings
    decomp = zlib.decompressobj()
    
    # Decompress the input data
    decompressed_data = decomp.decompress(compressed_data)
    
    return decompressed_data

# Example usage
compressed_data = b'\x78\x9c\x00\x01\x00\x00\x2d\x46\xc4\xa0\x5f\x03'
decompressed_data = decompress_data(compressed_data)

print("Decompressed Data:", decompressed_data.decode('utf-8'))
```

### 3. Getting Compression and Decompression Statistics

```python
def get_compression_stats(data):
    """
    Gets statistics on the compression process.

    Parameters:
    - data: bytes, the input data to be compressed.

    Returns:
    - dict, a dictionary containing compression statistics.
    """
    comp = zlib.compressobj(zlib.Z_DEFAULT_COMPRESSION)
    
    # Compress the input data
    comp.compress(data)
    comp.flush()
    
    # Get statistics
    stats = comp._get_stats()
    
    return stats

# Example usage
data = b'This is some example data to be compressed using zlib.'
stats = get_compression_stats(data)

print("Compression Statistics:", stats)
```

### 4. Handling Compressed Files with `zlib.decompressobj`

```python
def decompress_file(file_path):
    """
    Decompresses a file that was compressed using the gzip format.

    Parameters:
    - file_path: str, the path to the compressed file.

    Returns:
    - bytes, the decompressed data.
    """
    with open(file_path, 'rb') as f:
        compressed_data = f.read()
    
    # Create a decompressor object for gzip
    decomp = zlib.decompressobj(zlib.MAX_WBITS | 16)
    
    # Decompress the file data
    decompressed_data = decomp.decompress(compressed_data)
    decompressed_data += decomp.flush()
    
    return decompressed_data

# Example usage
file_path = 'example.gz'
decompressed_data = decompress_file(file_path)

print("Decompressed File Data:", decompressed_data.decode('utf-8'))
```

### 5. Using `zlib.compressobj` with Different Compression Levels

```python
def compress_with_level(data, level):
    """
    Compresses input data using the zlib algorithm with a specified compression level.

    Parameters:
    - data: bytes, the data to be compressed.
    - level: int, the compression level (0-9), where 9 is maximum compression.

    Returns:
    - bytes, the compressed data.
    """
    # Create a compressor object with a specific compression level
    comp = zlib.compressobj(level)
    
    # Compress the input data
    compressed_data = comp.compress(data)
    compressed_data += comp.flush()
    
    return compressed_data

# Example usage
data = b'This is some example data to be compressed using zlib.'
compressed_data = compress_with_level(data, 9)

print("Compressed Data (Level 9):", compressed_data)
```

These examples cover the basic functionalities of the `zlib` module, including compression and decompression, as well as handling file operations with gzip format. Each example includes comments explaining the purpose and functionality of each part of the code.
