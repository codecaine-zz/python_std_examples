# mmap - Memory-mapped file support

The `mmap` module in Python allows you to memory-map files, which means that it creates a view of a file as if it were an array of bytes in memory. This can be useful for working with large files efficiently without loading the entire file into memory at once.

Here are some code examples demonstrating various functionalities of the `mmap` module:

### Example 1: Basic Memory Mapping

```python
import mmap
import os

# Path to a sample file
file_path = 'example.txt'

# Create or open the file in binary mode for reading and writing
with open(file_path, 'r+b') as f:
    # Create a memory-mapped file object
    mm = mmap.mmap(f.fileno(), 0)

    # Write some data to the memory-mapped area
    mm.write(b'Hello, world!')

    # Move the cursor to the beginning of the mapped region
    mm.seek(0)

    # Read the data from the memory-mapped area
    print(mm.read().decode('utf-8'))

    # Close the memory mapping
    mm.close()
```

### Example 2: Synchronization with File

```python
import mmap
import os

# Path to a sample file
file_path = 'example.txt'

# Create or open the file in binary mode for reading and writing
with open(file_path, 'r+b') as f:
    # Create a memory-mapped file object
    mm = mmap.mmap(f.fileno(), 0)

    # Write some data to the memory-mapped area
    mm.write(b'Hello, synchronization!')

    # Sync the memory-mapped area with the file's contents
    mm.flush()

    # Seek back to the beginning of the mapped region
    mm.seek(0)

    # Read the data from the memory-mapped area
    print(mm.read().decode('utf-8'))

    # Close the memory mapping
    mm.close()
```

### Example 3: Writing and Reading Large Files

```python
import mmap
import os

# Path to a large sample file
file_path = 'large_file.txt'

# Create or open the file in binary mode for reading and writing
with open(file_path, 'r+b') as f:
    # Create a memory-mapped file object
    mm = mmap.mmap(f.fileno(), 0)

    # Write some large data to the memory-mapped area
    mm.write(b'Large data repeated many times')

    # Sync the memory-mapped area with the file's contents
    mm.flush()

    # Seek back to the beginning of the mapped region
    mm.seek(0)

    # Read the entire content of the memory-mapped area
    large_data = mm.read()

    # Close the memory mapping
    mm.close()
```

### Example 4: Memory-Mapping Multiple Regions

```python
import mmap
import os

# Path to a sample file
file_path = 'example.txt'

# Create or open the file in binary mode for reading and writing
with open(file_path, 'r+b') as f:
    # Create a memory-mapped file object
    mm = mmap.mmap(f.fileno(), 0)

    # Write some data to the first region
    mm.write(b'First region: Hello, ')

    # Seek back to the beginning of the mapped region
    mm.seek(0)

    # Read and print the first region
    print(mm.read(13).decode('utf-8'))

    # Seek to the second position in the file
    f.seek(14)

    # Create a new memory-mapped object for the remaining data
    mm2 = mmap.mmap(f.fileno(), os.path.getsize(file_path) - 14, offset=14)

    # Read and print the second region
    print(mm2.read().decode('utf-8'))

    # Close both memory mappings
    mm.close()
    mm2.close()
```

### Example 5: Using Memory-Mapped Files with Multiple Processes

```python
import mmap
import os
import multiprocessing

def process_data(data):
    with open('data.txt', 'r+b') as f:
        mm = mmap.mmap(f.fileno(), 0)
        mm.write(data)
        mm.flush()
        mm.seek(0)
        print(mm.read().decode('utf-8'))
        mm.close()

# Data to be processed
data_to_process = b'Process data example'

# Create a process and pass the data to it
process = multiprocessing.Process(target=process_data, args=(data_to_process,))
process.start()
process.join()
```

These examples demonstrate how to use the `mmap` module for various operations such as writing to, reading from, and synchronizing memory-mapped files. Each example includes comments explaining the steps involved.
