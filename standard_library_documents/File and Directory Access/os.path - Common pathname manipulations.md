# os.path — Common pathname manipulations

**os.path Module**
====================

The `os.path` module provides a way of using operating system dependent functionality.

### Basic Operations

#### 1. Splitting Path Components

```python
import os

# original path
path = '/home/user/documents/file.txt'

# split the path into its components
dir_path, file_name = os.path.split(path)

print(f"Directory Path: {dir_path}")
print(f"File Name: {file_name}")

```

#### 2. Joining Path Components

```python
import os

# directory and file names
dir_name = 'my_dir'
file_name = 'my_file.txt'

# join the paths together
new_path = os.path.join(dir_name, file_name)

print(f"Joined Path: {new_path}")

```

#### 3. Removing Trailing Directory Separators

```python
import os

path = '/home/user//documents/file.txt'

# remove trailing directory separators
cleaned_path = os.path.normpath(path)

print(f"Cleanned Path: {cleaned_path}")
```

### File Name Functions

#### 1. Base Name of a File

```python
import os

path = '/home/user/documents/file.txt'

# get the base name of the file (file_name)
base_name = os.path.basename(path)

print(f"Base Name: {base_name}")

```

#### 2. Extension of a File

```python
import os

path = '/home/user/documents/file.txt'

# get the extension of the file (.txt)
extension = os.path.splitext(base_name)[1]

print(f"Extension: {extension}")
```

### Directory Functions

#### 1. Current Working Directory

```python
import os

# print current working directory
print(os.getcwd())

```

#### 2. Checking if a File or Directory Exists

```python
import os

file_path = '/home/user/documents/file.txt'

# check if file exists
if os.path.exists(file_path):
    print(f"File {file_path} exists")

dir_path = '/home/user/documents'
if os.path.isdir(dir_path):
    print(f"Directory {dir_path} is a directory")
```

#### 3. Getting a List of All Files in a Directory

```python
import os

dir_path = '/home/user/documents'

# get list of all files and directories in the directory
files_and_dirs = os.listdir(dir_path)

print(files_and_dirs)
```

### Path Functions

#### 1. Normalizing a Path

```python
import os

path = '/home//user//documents/file.txt'

# normalize the path (remove redundant separators and up-level references ..)
normalized_path = os.path.normpath(path)

print(f"Normalized Path: {normalized_path}")
```

#### 2. Relativizing a Path

```python
import os

root_dir = '/home/user'
file_path = '/home//user/documents/file.txt'

# relativize the path (get relative path from root directory to file)
rel_path = os.path.relpath(file_path, start=root_dir)

print(f"Relatifized Path: {rel_path}")
```

#### 3. Absolutizing a Path

```python
import os

dir_path = '/home/user/documents'
file_name = 'my_file.txt'

# absolutize the path (get absolute path from current working directory)
abs_path = os.path.abspath(os.path.join(dir_path, file_name))

print(f"Absolute Path: {abs_path}")
```

#### 4. Getting Absolute and Relative Paths

```python
import os

dir_path = '/home/user/documents'
file_name = 'my_file.txt'

# get both absolute and relative paths
abs_path = os.path.abspath(os.path.join(dir_path, file_name))
rel_path = os.path.relpath(abs_path)

print(f"Absolute Path: {abs_path}")
print(f"Relative Path: {rel_path}")

```
