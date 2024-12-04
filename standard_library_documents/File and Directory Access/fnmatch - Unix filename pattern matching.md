# fnmatch — Unix filename pattern matching

**Functionality Overview:**

The `fnmatch` module provides a way to match filenames against Unix shell-style wildcards.

**Example Use Cases:**

*   Matching files with a specific extension
*   Matching files in a directory with a wildcard pattern
*   Checking if a file exists and has a certain attribute (e.g., size, mode)

**Code Generation:**

```python
# Import the fnmatch module
import fnmatch

def match_files_with_extension(directory, extension):
    """
    Match all files with the specified extension in the given directory.

    Args:
        directory (str): The path to the directory to search.
        extension (str): The file extension to match.

    Returns:
        list: A list of paths to files matching the specified extension.
    """
    # Use fnmatch.fnmatch to find all files with the specified extension
    return [path for path in os.listdir(directory) if fnmatch.fnmatch(path, f"*.{extension}")]

def get_files_in_directory(directory):
    """
    Get a list of all files and directories in the given directory.

    Args:
        directory (str): The path to the directory to search.

    Returns:
        list: A list of paths to files and directories.
    """
    # Use os.listdir to get a list of all files and directories
    return [path for path in os.listdir(directory)]

def check_file_attributes(directory, pattern, attr):
    """
    Check if any file in the given directory matches the specified wildcard pattern.

    Args:
        directory (str): The path to the directory to search.
        pattern (str): The Unix shell-style wildcard pattern to match.
        attr (str): The attribute to check (e.g., size, mode).

    Returns:
        bool: True if a file matches the pattern and has the specified attribute; False otherwise.
    """
    # Use os.path.exists and os.stat to get a list of all files
    files = [path for path in os.listdir(directory) if os.path.exists(os.path.join(directory, path))]

    # Iterate over each file and check if it matches the pattern and has the specified attribute
    for file in files:
        if fnmatch.fnmatch(file, pattern):
            try:
                stat = os.stat(os.path.join(directory, file))
                # Check if the file's size or mode match the specified attribute
                if attr == "size" and stat.st_size > 0:
                    return True
                elif attr == "mode" and stat.st_mode != -1:
                    return True
            except OSError:
                pass

    return False

# Example usage:

if __name__ == "__main__":
    import os

    directory = "."  # Search for files in the current directory
    extension = "*.txt"  # Match all .txt files
    pattern = "*.txt"  # Match all .txt files
    attr = "size"  # Check if any file has a non-zero size

    print(match_files_with_extension(directory, extension))  # Get all .txt files
    print(get_files_in_directory(directory))  # Get all files and directories
    print(check_file_attributes(directory, pattern, attr))  # Check if any file is a .txt file with a non-zero size
```

This code includes the following functions:

*   `match_files_with_extension`: Returns a list of paths to files matching the specified extension.
*   `get_files_in_directory`: Returns a list of paths to all files and directories in the given directory.
*   `check_file_attributes`: Returns True if any file matches the pattern and has the specified attribute, and False otherwise.

These functions demonstrate how you can use the `fnmatch` module to perform various operations on files in a directory.
