# pathlib — Object-oriented filesystem paths

**Pathlib Module**
================

The `pathlib` module provides an object-oriented interface to the filesystem.

### Installation

You don't need to install any additional packages to use the `pathlib` module. It is part of the Python Standard Library.

### Basic Usage

```python
import pathlib

# Create a new Path object from a string
path = pathlib.Path("example.txt")

print(path)  # Output: Path('example.txt')

# Get the file name and extension
print(path.name)  # Output: example.txt
print(path.suffix)  # Output: .txt

# Get the parent directory
print(path.parent)  # Output: Path('/')

# Check if a file or directory exists
path.exists()  # Returns True if the path exists, False otherwise
```

### Creating Paths from Raw Strings

```python
import pathlib

path = pathlib.Path("/home/user/example.txt")

print(path)  # Output: Path('/home/user/example.txt')
```

### Working with Directories

```python
import pathlib

# Create a new Path object for the current working directory
cwd = pathlib.Path.cwd()

print(cwd)  # Output: Path('...')

# Create a new directory
new_dir = cwd.joinpath("my_new_directory")
new_dir.mkdir()

print(new_dir)  # Output: Path('/.../my_new_directory')
```

### Resolving Paths

```python
import pathlib

path = pathlib.Path("/home/user/example.txt")

resolved_path = path.resolve()
resolved_path  # Output: Path('/home/user/example.txt')

# Join two paths together
join_path = cwd.joinpath("subdir").joinpath("example.txt")
print(join_path)  # Output: Path('/.../subdir/example.txt')
```

### File Operations

```python
import pathlib

# Create a new Path object for the file
file_path = pathlib.Path("example.txt")

# Get the file size in bytes
print(file_path.stat().st_size)  # Output: int

# Read the contents of the file
with open(file_path, "r") as f:
    print(f.read())  # Output: str

# Write to the file
with open(file_path, "w") as f:
    f.write("New contents")

# Delete the file
file_path.unlink()
```

### Directory Operations

```python
import pathlib

# Create a new directory
new_dir = pathlib.Path("/home/user/my_new_directory")
new_dir.mkdir()

# Get the list of files and directories in the directory
print(list(new_dir.iterdir()))  # Output: [Path('...')]

# Delete the directory and all its contents
new_dir.rmdir()
```

### Path Manipulation

```python
import pathlib

path = pathlib.Path("example.txt")

# Split the path into components
components = path.split()
print(components)  # Output: ['..', 'home', 'user', 'example.txt']

# Join two paths together
join_path = pathlib.Path("/").joinpath(components[0]).joinpath(*components[1:])
print(join_path)  # Output: Path('/')
```

### Path Comparison

```python
import pathlib

path1 = pathlib.Path("example.txt")
path2 = pathlib.Path("example.txt")

# Compare the paths for equality
print(path1 == path2)  # Output: True

# Get the difference between two paths
diff = path1 / path2
print(diff)  # Output: Path('..')
```

### Path Operations

```python
import pathlib

path = pathlib.Path("example.txt")

# Rename the file
new_name = path.with_suffix(".txt")
path.rename(new_name)

# Copy the file
copy_path = new_name.copy()
copy_path.copy(path)

# Move the file
move_path = new_name.move(path)
```

Note: This is not an exhaustive list of all possible `pathlib` operations. For a more comprehensive reference, please see the official [Python `pathlib` documentation](https://docs.python.org/3/library/pathlib.html).
