# fcntl - The fcntl and ioctl system calls

The `fcntl` module in Python provides a way to manipulate file descriptor properties using the `fcntl` system call, which is part of the POSIX API. This module allows you to perform operations on file descriptors such as locking, non-blocking I/O, and more.

Here are some comprehensive code examples for each functionality provided by the `fcntl` module:

### 1. Locking a File

```python
import fcntl
import os

# Open a file in read-only mode
fd = open('example.txt', 'r')

# Define lock flags (e.g., LOCK_EX for exclusive lock)
flags = fcntl.LOCK_EX | fcntl.LOCK_NB  # Non-blocking exclusive lock

try:
    # Apply the lock to the file descriptor
    fcntl.flock(fd, flags)

    print("File is locked.")
except BlockingIOError:
    print("Lock could not be acquired due to non-blocking flag.")

# Release the lock when done
fcntl.flock(fd, fcntl.LOCK_UN)
fd.close()
```

### 2. Non-blocking I/O

```python
import os
import fcntl

# Open a file in read-only mode
fd = open('example.txt', 'r')

# Set non-blocking mode using fcntl
flags = os.O_NONBLOCK
fcntl.fcntl(fd, fcntl.F_SETFL, flags)

try:
    # Attempt to read from the file without blocking
    data = fd.read(10)
    print(f"Data read: {data.decode()}")
except BlockingIOError:
    print("Reading from the file would block.")

# Close the file
fd.close()
```

### 3. Changing File Descriptor Properties

```python
import fcntl
import os

# Open a file in read-only mode
fd = open('example.txt', 'r')

# Get the current flags for the file descriptor
flags = fcntl.fcntl(fd, fcntl.F_GETFL)

print(f"Current flags: {flags}")

# Set a new flag (e.g., O_APPEND)
new_flags = flags | os.O_APPEND

# Apply the new flags to the file descriptor
fcntl.fcntl(fd, fcntl.F_SETFL, new_flags)

print("File descriptor flags updated.")

# Close the file
fd.close()
```

### 4. Using ioctl for Device Control

```python
import fcntl
import struct

# Open a device file
fd = open('/dev/ttyS0', 'r+')

# Define the ioctl command and argument (e.g., TIOCGSERIAL for serial port settings)
command = 0x80003F2C  # Example IOCTL command for getting serial port settings
arg = struct.pack('h', 9600)  # Example baud rate

try:
    # Perform the ioctl call
    result = fcntl.ioctl(fd, command, arg)
    print(f"Serial port settings: {result}")
except OSError as e:
    print(f"ioctl failed with error: {e}")

# Close the file
fd.close()
```

### 5. Setting File Descriptor Options

```python
import fcntl
import os

# Open a file in read-only mode
fd = open('example.txt', 'r')

# Define options to set (e.g., O_DSYNC for data synchronization)
options = os.O_DSYNC

# Apply the options to the file descriptor
fcntl.fcntl(fd, fcntl.F_SETFD, options)

print("File descriptor options updated.")

# Close the file
fd.close()
```

### 6. Getting File Descriptor Attributes

```python
import fcntl

# Open a file in read-only mode
fd = open('example.txt', 'r')

# Get the file status using F_GETSTAT
stat_buf = fcntl.fstat(fd)

print(f"File size: {stat_buf.st_size} bytes")

# Close the file
fd.close()
```

### 7. Getting File Descriptor Information

```python
import fcntl

# Open a file in read-only mode
fd = open('example.txt', 'r')

# Get the file descriptor information using F_GETFD
flags = fcntl.fcntl(fd, fcntl.F_GETFD)

print(f"File descriptor flags: {flags}")

# Close the file
fd.close()
```

### 8. Getting File Descriptor Lock Information

```python
import fcntl

# Open a file in read-only mode
fd = open('example.txt', 'r')

# Get the lock information using F_GETLK
lock_info = struct.pack('llll', 0, 0, 0, 0)  # Format: start, length, pid, type
fcntl.fcntl(fd, fcntl.F_GETLK, lock_info)

print(f"Lock information: {lock_info}")

# Close the file
fd.close()
```

These examples demonstrate various uses of the `fcntl` module to manipulate file descriptors and perform operations that are typically handled by lower-level system calls. Each example includes comments explaining the purpose and functionality of each code snippet, making it easy to understand and integrate into larger applications or documentation.
