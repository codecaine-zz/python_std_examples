# bz2 - Support for bzip2 compression
## Table of Contents

1. [1. Compressing a String](#1-compressing-a-string)
2. [2. Decompressing a Byte String](#2-decompressing-a-byte-string)
3. [3. Writing Compressed Data to a File](#3-writing-compressed-data-to-a-file)
4. [4. Reading Compressed Data from a File](#4-reading-compressed-data-from-a-file)
5. [5. Handling Compressed Data in a Streaming Context](#5-handling-compressed-data-in-a-streaming-context)
6. [6. Using `bz2.BZ2File` for File Operations](#6-using-bz2bz2file-for-file-operations)
7. [7. Handling Large Files Efficiently](#7-handling-large-files-efficiently)



Here are comprehensive code examples for the `bz2` module in Python, which provides support for bzip2 compression:

### 1. Compressing a String

```python
import bz2

def compress_string(input_string):
    """
    Compresses a given string using the bzip2 algorithm.

    Args:
        input_string (str): The string to be compressed.

    Returns:
        bytes: The compressed data.
    """
    # Convert the string to bytes if it isn't already
    if not isinstance(input_string, bytes):
        input_bytes = input_string.encode('utf-8')
    else:
        input_bytes = input_string

    # Compress the bytes using bz2
    compressed_data = bz2.compress(input_bytes)

    return compressed_data

# Example usage
original_text = "This is a sample text to be compressed using bzip2."
compressed = compress_string(original_text)
print("Original Length:", len(original_text))
print("Compressed Length:", len(compressed))
```

### 2. Decompressing a Byte String

```python
import bz2

def decompress_bytes(compressed_data):
    """
    Decompresses a compressed byte string using the bzip2 algorithm.

    Args:
        compressed_data (bytes): The compressed data to be decompressed.

    Returns:
        bytes: The decompressed data.
    """
    # Decompress the bytes using bz2
    decompressed_bytes = bz2.decompress(compressed_data)

    return decompressed_bytes

# Example usage
compressed_data = b"1HjBkLmNpQrStUvWxYz01hJkLmNpQrStUvWxYz"
original_text = decompress_bytes(compressed_data)
print("Decompressed Text:", original_text.decode('utf-8'))
```

### 3. Writing Compressed Data to a File

```python
import bz2

def write_compressed_to_file(input_string, filename):
    """
    Writes the compressed version of a string to a file using bzip2.

    Args:
        input_string (str): The string to be compressed and written.
        filename (str): The name of the file to write to.
    """
    # Compress the string
    compressed_data = compress_string(input_string)

    # Open the file in binary write mode and write the compressed data
    with open(filename, 'wb') as file:
        file.write(compressed_data)

# Example usage
input_text = "This is a sample text to be written to a bzip2-compressed file."
write_compressed_to_file(input_text, 'compressed_output.bz2')
```

### 4. Reading Compressed Data from a File

```python
import bz2

def read_compressed_from_file(filename):
    """
    Reads compressed data from a file and returns the decompressed string.

    Args:
        filename (str): The name of the file containing the compressed data.

    Returns:
        str: The decompressed string.
    """
    # Open the file in binary read mode
    with open(filename, 'rb') as file:
        compressed_data = file.read()

    # Decompress the bytes
    decompressed_bytes = decompress_bytes(compressed_data)

    return decompressed_bytes.decode('utf-8')

# Example usage
filename = 'compressed_output.bz2'
original_text = read_compressed_from_file(filename)
print("Original Text:", original_text)
```

### 5. Handling Compressed Data in a Streaming Context

```python
import bz2

def stream_compress(input_stream, output_stream):
    """
    Streams the compression of data from an input stream to an output stream.

    Args:
        input_stream (io.BytesIO): The input stream containing the data to be compressed.
        output_stream (io.BytesIO): The output stream to write the compressed data.
    """
    # Compress the input stream and write it to the output stream
    with bz2.BZ2Compressor() as compressor:
        while True:
            chunk = input_stream.read(1024)
            if not chunk:
                break
            output_stream.write(compressor.compress(chunk))

# Example usage
input_bytes = b"1HjBkLmNpQrStUvWxYz01hJkLmNpQrStUvWxYz"
with io.BytesIO(input_bytes) as input_buffer, io.BytesIO() as output_buffer:
    stream_compress(input_buffer, output_buffer)
    compressed_data = output_buffer.getvalue()
print("Compressed Data:", compressed_data)

# Decompression example
output_buffer.seek(0)
decompressed_data = decompress_bytes(output_buffer.read())
print("Decompressed Data:", decompressed_data.decode('utf-8'))
```

### 6. Using `bz2.BZ2File` for File Operations

```python
import bz2

def read_bz2_file(filename):
    """
    Reads data from a bzip2-compressed file and returns the decompressed string.

    Args:
        filename (str): The name of the bzip2-compressed file to read.

    Returns:
        str: The decompressed string.
    """
    # Open the file in binary read mode
    with bz2.BZ2File(filename, 'r') as bz2_file:
        return bz2_file.read().decode('utf-8')

def write_bz2_file(input_string, filename):
    """
    Writes a compressed version of a string to a bzip2-compressed file.

    Args:
        input_string (str): The string to be compressed and written.
        filename (str): The name of the bzip2-compressed file to write to.
    """
    # Open the file in binary write mode
    with bz2.BZ2File(filename, 'w') as bz2_file:
        bz2_file.write(input_string.encode('utf-8'))

# Example usage
input_text = "This is a sample text to be written to a bzip2-compressed file."
write_bz2_file(input_text, 'compressed_output.bz2')
print("Written Text:", read_bz2_file('compressed_output.bz2'))
```

### 7. Handling Large Files Efficiently

```python
import bz2
import io

def compress_large_file(input_filename, output_filename):
    """
    Compresses a large file using bzip2 in chunks.

    Args:
        input_filename (str): The name of the large file to be compressed.
        output_filename (str): The name of the compressed file to write.
    """
    # Open the large file in binary read mode
    with open(input_filename, 'rb') as input_file, bz2.BZ2File(output_filename, 'w') as output_file:
        while True:
            chunk = input_file.read(1024 * 1024)  # Read 1MB chunks
            if not chunk:
                break
            output_file.write(chunk)

def decompress_large_file(input_filename, output_filename):
    """
    Decompresses a large bzip2-compressed file into another.

    Args:
        input_filename (str): The name of the compressed file to read.
        output_filename (str): The name of the decompressed file to write.
    """
    # Open the compressed file in binary read mode
    with bz2.BZ2File(input_filename, 'rb') as bz2_file, open(output_filename, 'wb') as output_file:
        while True:
            chunk = bz2_file.read(1024 * 1024)  # Read 1MB chunks
            if not chunk:
                break
            output_file.write(chunk)

# Example usage
input_large_file = 'large_input.txt'
output_compressed_file = 'compressed_large_output.bz2'
compress_large_file(input_large_file, output_compressed_file)
print("Compressed Large File:", output_compressed_file)

output_decompressed_file = 'decompressed_large_output.txt'
decompress_large_file(output_compressed_file, output_decompressed_file)
print("Decompressed Large File:", output_decompressed_file)
```

These examples cover various aspects of using the `bz2` module, including basic compression and decompression operations, handling large files efficiently, and working with streams. Each example is designed to be clear and self-contained, making it easy to integrate into a larger project or documentation.
