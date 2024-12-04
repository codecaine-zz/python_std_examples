# errno - Standard errno system symbols

Certainly! Below is a comprehensive set of code examples demonstrating various functionalities provided by the `errno` module in Python's standard library. These examples are designed to be clear, concise, and suitable for inclusion in official documentation.

### 1. Accessing Error Numbers

The `errno` module provides a dictionary-like object that maps error numbers to their corresponding symbolic names. Here's how you can access these values:

```python
import errno

# Example: Get the symbolic name for an error number
try:
    with open('nonexistent_file.txt', 'r') as file:
        pass
except FileNotFoundError as e:
    print(f"FileNotFoundError: {e.errno}")  # Output: File not found (2)
    print(errno.errorcode[e.errno])             # Output: ENOENT

# Example: Accessing a specific error number directly
print(errno.ENOENT)                   # Output: 2
```

### 2. Handling Errors in I/O Operations

The `errno` module is useful for handling errors that occur during file operations or other I/O-related tasks.

```python
import errno
import os

try:
    # Attempt to remove a non-existent directory
    os.rmdir('nonexistent_directory')
except OSError as e:
    print(f"OSError: {e.errno}")  # Output: Directory not found (2)
    print(errno.errorcode[e.errno])     # Output: ENOTDIR

# Using errno directly in an exception block
try:
    with open('nonexistent_file.txt', 'r') as file:
        pass
except OSError as e:
    if e.errno == errno.ENOENT:
        print("File not found")
```

### 3. Error Codes for File Operations

The `errno` module provides specific error codes for various file operations.

```python
import errno
import os

try:
    # Attempt to open a non-existent file
    with open('nonexistent_file.txt', 'r') as file:
        pass
except OSError as e:
    print(f"FileNotFoundError: {e.errno}")  # Output: File not found (2)
    if e.errno == errno.ENOENT:
        print("File does not exist")

# Error codes for specific file operations
try:
    # Attempt to remove a non-empty directory
    os.rmdir('empty_directory')
except OSError as e:
    print(f"DirectoryNotEmptyError: {e.errno}")  # Output: Directory is not empty (30)
    if e.errno == errno.ENOTEMPTY:
        print("Directory is not empty")

# Error codes for specific I/O errors
try:
    with open('nonexistent_file.txt', 'r') as file:
        pass
except IOError as e:
    print(f"IOError: {e.errno}")  # Output: Input/output error (5)
```

### 4. Error Codes for General I/O Errors

The `errno` module provides specific error codes for general input/output errors.

```python
import errno

# Example: Handling a general IO error
try:
    file = open('nonexistent_file.txt', 'r')
    content = file.read()
except IOError as e:
    print(f"IOError: {e.errno}")  # Output: Input/output error (5)
    if e.errno == errno.EIO:
        print("I/O error occurred")

# Handling a specific I/O error
try:
    with open('nonexistent_file.txt', 'r') as file:
        pass
except IOError as e:
    if e.errno == errno.ESPIPE:
        print("Pipe error")
```

### 5. Error Codes for Permissions Issues

The `errno` module provides specific error codes for permission issues.

```python
import errno
import os

try:
    # Attempt to write to a read-only file
    with open('readonly_file.txt', 'w') as file:
        file.write("Hello, World!")
except IOError as e:
    print(f"IOError: {e.errno}")  # Output: Permission denied (13)
    if e.errno == errno.EACCES:
        print("Permission denied")
```

### 6. Error Codes for Connection Issues

The `errno` module provides specific error codes for connection issues.

```python
import socket
import errno

try:
    # Attempt to connect to a non-existent server
    sock = socket.create_connection(('nonexistent_server', 80))
except ConnectionRefusedError as e:
    print(f"ConnectionRefusedError: {e.errno}")  # Output: Connection refused (111)
    if e.errno == errno.ECONNREFUSED:
        print("Connection refused")

# Handling a specific connection error
try:
    with socket.create_connection(('localhost', 80)) as sock:
        pass
except IOError as e:
    if e.errno == errno.ETIMEDOUT:
        print("Connection timeout")
```

### 7. Error Codes for Timeout Issues

The `errno` module provides specific error codes for timeout issues.

```python
import socket
import time

try:
    # Attempt to connect to a server with a timeout
    sock = socket.create_connection(('localhost', 80), timeout=1)
except IOError as e:
    print(f"IOError: {e.errno}")  # Output: Connection timed out (110)
    if e.errno == errno.ETIMEDOUT:
        print("Connection timed out")
```

### 8. Error Codes for Invalid Argument Issues

The `errno` module provides specific error codes for invalid argument issues.

```python
import os

try:
    # Attempt to open a file with an invalid path
    with open('invalid:/path/to/file', 'r') as file:
        pass
except OSError as e:
    print(f"OSError: {e.errno}")  # Output: Invalid argument (22)
    if e.errno == errno.EINVAL:
        print("Invalid argument")
```

### 9. Error Codes for File System Full Issues

The `errno` module provides specific error codes for file system full issues.

```python
import os

try:
    with open('full_file.txt', 'wb') as file:
        # Simulate filling the disk
        file.write(b'a' * (os.statvfs('/').f_frsize * 1024**2))
except IOError as e:
    print(f"IOError: {e.errno}")  # Output: No space left on device (28)
    if e.errno == errno.ENOSPC:
        print("No space left on the device")
```

### 10. Error Codes for Path Not Found Issues

The `errno` module provides specific error codes for path not found issues.

```python
import os

try:
    # Attempt to access a non-existent file
    with open('nonexistent_file.txt', 'r') as file:
        pass
except FileNotFoundError as e:
    print(f"FileNotFoundError: {e.errno}")  # Output: No such file or directory (2)
    if e.errno == errno.ENOENT:
        print("File not found")
```

These examples demonstrate various ways to use the `errno` module to handle errors in Python, covering common I/O operations and error conditions. The code is designed to be clear, self-contained, and suitable for integration into documentation.
