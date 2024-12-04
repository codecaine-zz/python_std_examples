# posix — The most common POSIX system calls

Here's an example of how you can use some common functions from the `posix` module:

```python
import posix

# Define constants
POSIX_CONSTANT_1 = posix.constants.PATH_MAX  # Maximum length of a path in characters
POSIX_CONSTANT_2 = posix.constants.O_RDONLY  # Open file for reading only
POSIX_CONSTANT_3 = posix.constants.S_IRUSR  # Read permission for the owner

# Get current working directory
import os
current_dir = os.getcwd()
print("Current working directory:", current_dir)

# Set current working directory
os.chdir("/path/to/new/directory")

# Create a new file
file_name = "test.txt"
with open(file_name, "w") as f:
    # Write to the file
    f.write("Hello, world!")

# Open an existing file for reading and writing
with open("/path/to/existing/file", "r+") as f:
    # Read from the file
    print(f.read())
    # Append to the file
    f.seek(0)
    f.write("New content")
    f.truncate()

# Create a new directory
import os
new_dir_name = "test_directory"
try:
    os.mkdir(new_dir_name)
except FileExistsError:
    print(f"A directory with this name already exists: {new_dir_name}")

# Remove the newly created directory
os.rmdir(new_dir_name)

# Get file statistics (owner, group, size, etc.)
import stat
file_name = "test.txt"
try:
    # Get file stats
    stats = os.stat(file_name)
    print(f"Owner ID: {stats.st_uid}")
    print(f"Group ID: {stats.st_gid}")
    print(f"Size in bytes: {stats.st_size}")
except FileNotFoundError:
    print("File not found.")

# Check if a process is running
import psutil
try:
    # Get the PID of the process we want to check
    pid = 1234
    process = psutil.Process(pid)
    # Check if the process is running
    if process.is_running():
        print(f"Process {pid} is running.")
    else:
        print(f"Process {pid} is not running.")
except psutil.NoSuchProcess:
    print("No such process.")

# Convert a path to an absolute path
import posix
file_name = "/path/torelative/file"
abs_file_path = posix.path.abspath(file_name)
print(f"Absolute path: {abs_file_path}")

# Split a path into its components
posix_path = posix.path.split(abs_file_path)
print("Path components:")
for component in posix_path:
    print(component)

# Join multiple path components together
components = ["path", "to", "join"]
joined_path = posix.path.join(*components)
print(f"Joined path: {joined_path}")

# Get the current process ID
import pidns
pid = pidns.getpid()
print(f"Current PID: {pid}")
```

This example shows some common functions and constants from the `posix` module. However, please note that not all of these functions are necessary for a typical use case.

**Constants:**

*   `POSIX_CONSTANT_1`: The maximum length of a path in characters.
*   `POSIX_CONSTANT_2`: A flag to open a file for reading only.
*   `POSIX_CONSTANT_3`: A permission mask to grant read access to the owner.

**Functions:**

*   `os.getcwd()`: Returns the current working directory as a string.
*   `os.chdir(directory)`: Changes the current working directory to the specified path.
*   `open(file, mode)`: Opens a file in the specified mode. The mode can be `'r'`, `'w'`, `'a'`, etc.
*   `stat(file_name)`: Returns information about the specified file as a `stat_result` object.
*   `os.stat(file_name)`: Returns information about the specified file as a `stat_result` object.

**Functions from psutil:**

*   `psutil.Process(pid)`: Returns a process object with the specified PID.
*   `process.is_running()`: Returns True if the process is running, False otherwise.
