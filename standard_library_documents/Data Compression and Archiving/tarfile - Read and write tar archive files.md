# tarfile - Read and write tar archive files

The `tarfile` module in Python is used to read and write tar archives, which are a common format for archiving multiple files into a single file container. Below are comprehensive examples demonstrating various functionalities of this module:

### 1. Creating a Tar Archive

```python
import tarfile

# Create a new tar archive
with tarfile.open('example.tar.gz', 'w:gz') as tar:
    # Add individual files to the archive
    tar.add('file1.txt')
    tar.add('folder')
```

### 2. Extracting a Tar Archive

```python
import tarfile

# Open an existing tar archive for reading
with tarfile.open('example.tar.gz', 'r:gz') as tar:
    # Extract all contents to the current directory
    tar.extractall()
```

### 3. Writing to a Tar Archive with Specific Compression

```python
import tarfile

# Create a new tar archive with custom compression settings
with tarfile.open('example.tar.bz2', 'w:bz2') as tar:
    # Add files or directories to the archive
    tar.add('file1.txt')
```

### 4. Extracting from a Tar Archive with Specific Compression

```python
import tarfile

# Open an existing tar archive for reading and specifying compression
with tarfile.open('example.tar.bz2', 'r:bz2') as tar:
    # Extract all contents to the current directory
    tar.extractall()
```

### 5. Adding Files or Directories Recursively

```python
import tarfile

# Create a new tar archive and add directories recursively
with tarfile.open('example.tar.gz', 'w:gz') as tar:
    # Add all files and subdirectories in the current directory to the archive
    tar.add('.', recursive=True)
```

### 6. Extracting Files or Directories with Specific Options

```python
import tarfile

# Open an existing tar archive for reading and extract with options
with tarfile.open('example.tar.gz', 'r:gz') as tar:
    # Extract all contents to a specific directory, ignoring existing files
    tar.extractall(path='extracted_files', members=tar.getmembers(), numeric_owner=True)
```

### 7. Checking Tar Archive Integrity

```python
import tarfile

# Open an existing tar archive for reading and check its integrity
with tarfile.open('example.tar.gz', 'r:gz') as tar:
    # Check if all files in the archive are intact
    print(tar.check())
```

### 8. Writing to a Tar Archive with Custom File Mode

```python
import tarfile

# Create a new tar archive and add files with specific permissions
with tarfile.open('example.tar.gz', 'w:gz') as tar:
    # Add file1.txt with read-only mode for all users
    info = tar.gettarinfo(name='file1.txt')
    info.mode = 0o444  # 0o444 is the decimal representation of 444, which is r--r--r--
    tar.add('file1.txt', arcname='file1.txt', tarinfo=info)
```

### 9. Extracting Files with Specific Permissions

```python
import tarfile

# Open an existing tar archive for reading and extract files with specific permissions
with tarfile.open('example.tar.gz', 'r:gz') as tar:
    # Extract file1.txt to a directory, setting its mode to read-only for all users
    info = tar.gettarinfo(name='file1.txt')
    info.mode = 0o444
    tar.extract('file1.txt', path='extracted_files', tarinfo=info)
```

### 10. Writing to a Tar Archive with Custom File Date

```python
import tarfile
from datetime import datetime

# Create a new tar archive and add files with a specific modification date
with tarfile.open('example.tar.gz', 'w:gz') as tar:
    # Define the desired modification time
    modification_time = datetime(2023, 10, 5, 14, 30)
    
    # Add file1.txt with a custom modification time
    info = tar.gettarinfo(name='file1.txt')
    info.mtime = modification_time.timestamp()
    tar.add('file1.txt', arcname='file1.txt', tarinfo=info)
```

### 11. Extracting Files with Custom File Date

```python
import tarfile
from datetime import datetime

# Open an existing tar archive for reading and extract files with a specific modification date
with tarfile.open('example.tar.gz', 'r:gz') as tar:
    # Define the desired modification time
    modification_time = datetime(2023, 10, 5, 14, 30)
    
    # Extract file1.txt from the archive, setting its modification time to the defined value
    info = tar.gettarinfo(name='file1.txt')
    info.mtime = modification_time.timestamp()
    tar.extract('file1.txt', path='extracted_files', tarinfo=info)
```

### 12. Writing to a Tar Archive with Custom Link Type

```python
import tarfile

# Create a new tar archive and add symbolic links
with tarfile.open('example.tar.gz', 'w:gz') as tar:
    # Add a symbolic link named 'link.txt' pointing to 'source_file'
    info = tarfile.TarInfo(name='link.txt')
    info.type = tarfile.SYMTYPE  # Symbolic link type
    info.linkname = 'source_file'  # Path to the target file
    tar.addfile(info, open('source_file', 'rb'))
```

### 13. Extracting Files with Custom Link Type

```python
import tarfile

# Open an existing tar archive for reading and extract symbolic links
with tarfile.open('example.tar.gz', 'r:gz') as tar:
    # Extract a symbolic link from the archive
    tar.extract('link.txt', path='extracted_files')
```

These examples cover various aspects of using the `tarfile` module, including creating, extracting, writing to and reading from tar archives with different compression types, handling file permissions, modification times, and symbolic links.
