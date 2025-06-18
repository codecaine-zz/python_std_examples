# stat - Interpreting stat() results
## Table of Contents

1. [Example 1: Basic Usage of `stat()`](#example-1-basic-usage-of-stat)
2. [Example 2: Using `os.path.getmtime()` for Modification Time](#example-2-using-ospathgetmtime-for-modification-time)
3. [Example 3: Extracting Permissions and Flags](#example-3-extracting-permissions-and-flags)
4. [Example 4: Handling File Attributes with `os.lstat()` and `os.fstat()`](#example-4-handling-file-attributes-with-oslstat-and-osfstat)
5. [Example 5: Checking File Types](#example-5-checking-file-types)
6. [Example 6: Accessing Extended Attributes with `os.listxattr()`](#example-6-accessing-extended-attributes-with-oslistxattr)
7. [Example 7: Using `os.access()` to Check Permissions](#example-7-using-osaccess-to-check-permissions)
8. [Example 8: Retrieving Filesystem Information with `os.statvfs()`](#example-8-retrieving-filesystem-information-with-osstatvfs)



The `stat` module in Python provides a portable way of using operating system-dependent functionality like reading or writing to the file system, and it includes functions that return information about files and directories. This module is particularly useful for understanding file properties such as permissions, last modification times, and more.

Here are several code examples that demonstrate how to interpret `stat()` results:

### Example 1: Basic Usage of `stat()`
```python
import os

# Define the path to a file
file_path = 'example.txt'

# Get the stat information for the file
stat_info = os.stat(file_path)

# Extract and print some useful information
print(f"File size (bytes): {stat_info.st_size}")
print(f"Last modified time: {stat_info.st_mtime}")
print(f"Permissions: {oct(stat_info.st_mode)}")
```

### Example 2: Using `os.path.getmtime()` for Modification Time
```python
import os

# Define the path to a file
file_path = 'example.txt'

# Use getmtime() to get the last modification time of the file
modification_time = os.path.getmtime(file_path)

# Print the formatted modification time
print(f"Last modified time: {modification_time}")
```

### Example 3: Extracting Permissions and Flags
```python
import stat

# Define the path to a directory
dir_path = '/path/to/directory'

# Get the stat information for the directory
stat_info = os.stat(dir_path)

# Extract permissions and flags
permissions = stat_info.st_mode
flags = stat_info.st_flags

print(f"Permissions: {oct(permissions)}")
print(f"Flags: {hex(flags)}")
```

### Example 4: Handling File Attributes with `os.lstat()` and `os.fstat()`
```python
import os

# Define the path to a symbolic link and a file
symbolic_link_path = 'symlink.txt'
file_path = 'example.txt'

# Use lstat() to get stat information for a symbolic link
link_stat_info = os.lstat(symbolic_link_path)
print(f"Symbolic Link Stat Info: {link_stat_info.st_mode}")

# Use fstat() to get stat information for an open file descriptor
with open(file_path, 'r') as file:
    file_stat_info = os.fstat(file.fileno())
print(f"File Stat Info (from file descriptor): {file_stat_info.st_mode}")
```

### Example 5: Checking File Types
```python
import os

# Define the path to a file and directory
file_path = 'example.txt'
dir_path = '/path/to/directory'

# Get stat information for the file and directory
file_stat_info = os.stat(file_path)
dir_stat_info = os.stat(dir_path)

# Check if they are files or directories
is_file = stat.S_ISREG(file_stat_info.st_mode)
is_dir = stat.S_ISDIR(dir_stat_info.st_mode)

print(f"Is {file_path} a file? {'Yes' if is_file else 'No'}")
print(f"Is {dir_path} a directory? {'Yes' if is_dir else 'No'}")
```

### Example 6: Accessing Extended Attributes with `os.listxattr()`
```python
import os

# Define the path to a file or directory
path = '/path/to/file'

# List extended attributes of the object
try:
    xattrs = os.listxattr(path)
    print(f"Extended attributes for {path}: {', '.join(xattrs)}")
except OSError as e:
    print(f"Error listing extended attributes: {e}")
```

### Example 7: Using `os.access()` to Check Permissions
```python
import os

# Define the path to a file and permissions
file_path = 'example.txt'
permissions_to_check = os.R_OK | os.W_OK

# Use access() to check if the current user has the specified permissions
if os.access(file_path, permissions_to_check):
    print(f"Current user has read/write permission for {file_path}")
else:
    print(f"Current user does not have read/write permission for {file_path}")
```

### Example 8: Retrieving Filesystem Information with `os.statvfs()`
```python
import os

# Define the path to a directory
directory_path = '/path/to/directory'

# Get filesystem statistics for the directory
statvfs_info = os.statvfs(directory_path)

print(f"Total space: {statvfs_info.f_blocks * statvfs_info.f_frsize} bytes")
print(f"Free space: {statvfs_info.f_bfree * statvfs_info.f_frsize} bytes")
print(f"Available space: {statvfs_info.f_bavail * statvfs_info.f_frsize} bytes")
```

These examples demonstrate how to use the `stat` module in Python to retrieve and interpret various file system properties. Each example includes comments explaining the purpose of each step and relevant functions used.
