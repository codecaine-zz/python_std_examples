# gzip - Support for gzip files

The `gzip` module provides support for reading from and writing to .gz (gzip) compressed files. Below are comprehensive examples of how to use this module, including functions for both reading and writing files.

### Writing Gzip Files

```python
import gzip

def write_to_gz_file(file_path, data):
    """
    Write data to a gzip file.

    :param file_path: Path to the gzip file.
    :param data: Data to be written into the gzip file.
    """
    with gzip.open(file_path, 'wb') as f:
        # Writing bytes directly is common for gzip files
        f.write(data.encode('utf-8'))

# Example usage
data_to_write = "This is some text that will be compressed and saved to a gzip file."
write_to_gz_file('example.gz', data_to_write)
```

### Reading Gzip Files

```python
import gzip

def read_from_gz_file(file_path):
    """
    Read data from a gzip file.

    :param file_path: Path to the gzip file.
    :return: The content of the gzip file as a string.
    """
    with gzip.open(file_path, 'rb') as f:
        # Reading bytes and decoding back to string
        return f.read().decode('utf-8')

# Example usage
file_content = read_from_gz_file('example.gz')
print(file_content)
```

### Compressing Data

```python
import gzip

def compress_data(data):
    """
    Compress data using gzip.

    :param data: The data to be compressed.
    :return: A bytes object containing the compressed data.
    """
    # Using gzip.compress() to compress a byte string
    return gzip.compress(data.encode('utf-8'))

# Example usage
original_data = "This is some text that will be compressed."
compressed_data = compress_data(original_data)
print(f"Compressed Data Length: {len(compressed_data)} bytes")
```

### Decompressing Data

```python
import gzip

def decompress_data(compressed_data):
    """
    Decompress data using gzip.

    :param compressed_data: A bytes object containing the compressed data.
    :return: The original content as a string.
    """
    # Using gzip.decompress() to decompress a byte string
    return gzip.decompress(compressed_data).decode('utf-8')

# Example usage
compressed_bytes = compress_data("This is some text that will be compressed.")
decompressed_text = decompress_data(compressed_bytes)
print(decompressed_text)
```

### Handling Errors

```python
import gzip

def handle_gzip_error(file_path):
    """
    Handle errors when reading from or writing to a gzip file.

    :param file_path: Path to the gzip file.
    """
    try:
        with gzip.open(file_path, 'rb') as f:
            # Attempt to read data from a gzip file
            content = f.read().decode('utf-8')
            print(content)
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
handle_gzip_error('non_existent_file.gz')
```

### Additional Examples

#### Writing and Reading Multiple Files

```python
import gzip

def write_multiple_files(file_paths, data_list):
    """
    Write multiple pieces of data to different gzip files.

    :param file_paths: List of paths for the gzip files.
    :param data_list: List of data strings to be written into the gzip files.
    """
    if len(file_paths) != len(data_list):
        raise ValueError("The number of file paths must match the number of data items.")

    with gzip.open(file_paths[0], 'wb') as f:
        # Writing bytes directly is common for gzip files
        f.write(data_list[0].encode('utf-8'))

    for i, (file_path, data) in enumerate(zip(file_paths[1:], data_list[1:])):
        with gzip.open(file_path, 'wb') as f:
            f.write(data.encode('utf-8'))

# Example usage
data_list = ["First file content", "Second file content"]
write_multiple_files(['first_file.gz', 'second_file.gz'], data_list)
```

#### Compressing and Decompressing Multiple Files

```python
import gzip

def compress_multiple_files(file_paths):
    """
    Compress multiple files into a single gzip archive.

    :param file_paths: List of paths to the files to be compressed.
    """
    with gzip.open('archive.gz', 'wb') as outfile:
        for infile_path in file_paths:
            with open(infile_path, 'rb') as infile:
                outfile.write(inf.read())

# Example usage
compress_multiple_files(['file1.txt', 'file2.txt'])
```

These examples cover the basic functionalities of the `gzip` module, including reading from, writing to, compressing, and decompressing gzip files. They also demonstrate error handling and how to work with multiple files in a single operation.
