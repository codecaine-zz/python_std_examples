# gzip — Support for gzip files

**gzip Module Code Generation**
=====================================

The `gzip` module in Python provides functions and classes to read and write gzip-formatted files.

### Importing the gzip Module

```python
import gzip
```

### Reading a Gzip File

```python
def read_gzip_file(file_path):
    """
    Opens a gzip file in binary mode and reads its contents.
    
    Args:
        file_path (str): The path to the gzip file.
    
    Returns:
        bytes: The contents of the gzip file.
    """
    with open(file_path, 'rb') as file:
        return gzip.open(file).read()
```

### Writing a Gzip File

```python
def write_gzip_file(file_path, data):
    """
    Writes data to a gzip file in binary mode.
    
    Args:
        file_path (str): The path to the output gzip file.
        data (bytes): The data to be written to the gzip file.
    """
    with open(file_path, 'wb') as file:
        return gzip.open(file, 'w').write(data)
```

### Decompressing a Gzip File

```python
def decompress_gzip_file(file_path):
    """
    Reads a gzip file and decompresses its contents.
    
    Args:
        file_path (str): The path to the gzip file.
    
    Returns:
        bytes: The decompressed contents of the gzip file.
    """
    with open(file_path, 'rb') as file:
        return gzip.open(file).read()
```

### Creating a Gzip File

```python
def create_gzip_file(file_path, data):
    """
    Creates a new gzip file and writes its contents.
    
    Args:
        file_path (str): The path to the output gzip file.
        data (bytes): The data to be written to the gzip file.
    
    Returns:
        str: The path to the created gzip file.
    """
    with open(file_path, 'wb') as file:
        return file.write(data)
```

### Example Usage

```python
# Read a gzip file
data = read_gzip_file('example.gz')
print(data)

# Write data to a gzip file
write_gzip_file('example.gz', b'Hello, World!')

# Decompress a gzip file
decompressed_data = decompress_gzip_file('example.gz')
print(decompressed_data)

# Create a new gzip file
create_gzip_file('new_example.gz', b'New Example Data!')
```

### Notes

* The `gzip` module uses the `zlib` library under the hood.
* The `open` function is used in binary mode (`'rb'` or `'wb'`) to ensure that the files are read and written correctly.
* The `gzip.open` function is used to open gzip files, which provides a file-like object for reading and writing.
* The `zlib.decompress` function can be used instead of `gzip.open` to decompress gzip files.
