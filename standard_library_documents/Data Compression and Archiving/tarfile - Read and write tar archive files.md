# tarfile — Read and write tar archive files

**Tarfile Module Code Examples**
=====================================

The `tarfile` module provides an interface for reading and writing tar archive files.

### Creating a Tar Archive File

```python
import tarfile

# Create a new tar archive file
with tarfile.open('example.tar', 'w') as tar:
    # Add files to the archive
    tar.add('./file1.txt')
    tar.add('./file2.txt')

# List of all files and directories in the archive
for member in tar.getmembers():
    print(member.name)

# Close the file without writing any data (i.e., empty archive)
with tarfile.open('example.tar', 'w') as tar:
    pass
```

### Reading a Tar Archive File

```python
import tarfile

# Open the tar archive file for reading
with tarfile.open('example.tar', 'r') as tar:
    # Extract files from the archive
    tar.extractall()

# List of all files and directories in the archive
for member in tar.getmembers():
    print(member.name)
```

### Reading Specific Members

```python
import tarfile

# Open the tar archive file for reading
with tarfile.open('example.tar', 'r') as tar:
    # Extract specific members from the archive
    tar.extractall(path='extracted_path')

    # Get specific member
    with tar.getmember('specific_member.txt') as member:
        print(member.size, member.mtime)

# List of all files and directories in the archive
for member in tar.getmembers():
    print(member.name)
```

### Tarfile Options

```python
import tarfile

# Open the tar archive file for reading with options
with tarfile.open('example.tar', 'r') as tar:
    # Specify compression level
    tar = tar.open('w:gz', 'r')

    # List of all files and directories in the archive
    for member in tar.getmembers():
        print(member.name)
```

### Writing Multiple Files

```python
import tarfile

# Open the tar archive file for writing with options
with tarfile.open('example.tar', 'w') as tar:
    # Add multiple files to the archive
    tar.add('./file1.txt')
    tar.add('./file2.txt')
    tar.add('./dir')

# List of all files and directories in the archive
for member in tar.getmembers():
    print(member.name)
```

### Writing a Large Number of Files

```python
import tarfile

# Open the tar archive file for writing with options
with tarfile.open('example.tar', 'w') as tar:
    # Create an iterable of files to add to the archive
    files = ['file1.txt'] * 1000 + ['dir'] * 10
    tar.addall(files)

# List of all files and directories in the archive
for member in tar.getmembers():
    print(member.name)
```

### Extracting Files with Options

```python
import tarfile

# Open the tar archive file for reading
with tarfile.open('example.tar', 'r') as tar:
    # Extract specific members from the archive with options
    tar.extractall(path='extracted_path', compress_types=tar.GZ)
```

### Creating a Recursive Tar Archive File

```python
import tarfile

# Open the tar archive file for writing
with tarfile.open('example.tar', 'w') as tar:
    # Create an iterable of files and directories to add to the archive
    def generator(path):
        for root, dirs, files in os.walk(path):
            for name in files:
                yield f'{root}/{name}'
            for dir in dirs:
                yield f'{root}/{dir}'

    tar.addall(generator('./path/to/files'))

# List of all files and directories in the archive
for member in tar.getmembers():
    print(member.name)
```
