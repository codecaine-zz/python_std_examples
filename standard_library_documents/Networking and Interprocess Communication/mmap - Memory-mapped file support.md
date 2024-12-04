# mmap — Memory-mapped file support

**Memory-Mapped File Support Module: mmap**
====================================================

### Overview

The `mmap` module provides an interface for mapping files into memory, allowing for efficient and flexible access to file contents.

### Functions

#### `mmap.mmap(file descriptor, length, offset, access, device=None)`

*   **file descriptor**: The file descriptor to be mapped.
*   **length**: The size of the area to be mapped (in bytes).
*   **offset**: The offset into the file where mapping begins.
*   **access**: A string specifying the access mode:
    *   'r' for read-only
    *   'w' for write-only
    *   'rw' for read-write
*   **device**: Optional device identifier (for Unix-based systems only)

**Example Usage:**
```python
import mmap

# Open a file in binary mode
with open('example.bin', 'rb') as file:
    # Create an mmap object mapping the entire file into memory
    mapped_file = mmap.mmap(file.fileno(), 0, access='r')

    # Map a specific region of the file into memory
    mapped_region = mmap.mmap(file.fileno(), 1024, offset=512, access='rw')

    # Access and manipulate the mapped data
    print(mapped_file.read(10))  # Read from the entire file
    print(mapped_region.readline())  # Read a line from the specified region

# Close the mmap object to release system resources
mapped_file.close()
```

#### `mmap.mmap.mmap(file descriptor, length, offset, access)`

*   This constructor is deprecated and should not be used directly.

### Classes

#### `mmap.MappedFile`

This class represents a mapped file in memory. It provides methods for accessing the mapped data.

**Example Usage:**
```python
import mmap

# Open a file in binary mode
with open('example.bin', 'rb') as file:
    # Create an MappedFile object mapping the entire file into memory
    with mmap.mmap(file.fileno(), 0, access='r') as mapped_file:
        print(mapped_file.read(10))  # Read from the entire file

# Access and manipulate the mapped data using methods provided by MappedFile
with open('example.bin', 'rb') as file:
    with mmap.MappedFile(file.fileno()) as mapped_file:
        mapped_data = mapped_file.read()
        print(mapped_data)  # Print the contents of the mapped file
```

### Constants

#### `mmap.ACCESS_READ` and `mmap.ACCESS_WRITE`

*   Define the access modes for `read-only` (0x0004) and `write-only` (0x0010), respectively.

```python
import mmap

ACCESS_READ = 0x0004  # Read-only access
ACCESS_WRITE = 0x0010  # Write-only access

# Usage:
with open('example.bin', 'rb') as file:
    with mmap.mmap(file.fileno(), 0, access=ACCESS_READ) as mapped_file:
        print(mapped_file.read(10))  # Read from the entire file
```

### Error Handling

#### `mmap.MAP_FAILED` and `mmap.ENOTFOUND`

*   Define error codes for mapping failures (0x12) and non-existent files (2).

```python
import mmap

MAP_FAILED = -12  # Mapping failed
ENOTFOUND = 2     # Non-existent file

# Usage:
try:
    with open('nonexistent_file.bin', 'rb') as file:
        with mmap.mmap(file.fileno(), 0, access='r') as mapped_file:
            print(mapped_file.read(10))
except OSError as e:
    if e.errno == ENOTFOUND:
        print("File not found:", e)
```

### Example Use Cases

*   **Binary Data Processing**: Map files into memory and process binary data using NumPy or Pandas.
*   **Large File Access**: Use `mmap` to access large files without loading the entire file into memory, reducing memory usage.
*   **Data Compression**: Compress data stored in a mapped file using libraries like gzip or zlib.

By leveraging the `mmap` module, developers can optimize memory usage and improve performance when working with files that contain large amounts of data.
