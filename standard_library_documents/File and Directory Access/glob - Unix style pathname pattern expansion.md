# glob — Unix style pathname pattern expansion

**Glob Module**
===============

The `glob` module provides utilities for expanding Unix shell-style pathname patterns.

**Example Code**
----------------

```python
import glob

# Match all files with a `.txt` extension in the current directory
matched_files = glob.glob('*.txt')
print(matched_files)  # Output: ['file1.txt', 'file2.txt']

# Match all directories with names containing `data`
matched_dirs = glob.glob('data*/')
print(matched_dirs)  # Output: ['/path/to/data/dir', '/another/path/data/dir']

# Match all files with a `.txt` extension in the current working directory
matched_files_cwd = glob.glob('./*.txt')
print(matched_files_cwd)  # Output: ['file1.txt', 'file2.txt']

# Match all patterns, including the full pattern and relative paths
matched_patterns = glob.glob('**/*')
print(matched_patterns)  # Output: ['/path/to/file1.txt', '/another/path/file2.txt', ...]

# Use `glob.iglob` for iterator-based expansion (more memory-efficient)
file_iterator = glob.iglob('*.txt')
for file in file_iterator:
    print(file)

# Use `glob.os_path_matches` to check if a pattern matches the current path
import os
if glob.os_path_matches(os.getcwd(), 'my_directory'):
    print("Current directory is 'my_directory'")

# Use `glob.os_pathnormpath` to normalize a path for pattern matching
normalized_path = glob.os_pathnormpath('/path/to/directory')
print(normalized_path)  # Output: '/path/to/directory'
```

**Common Functions**
--------------------

*   `glob.glob(pattern[, recursive][, strict])`: Expand the file name pattern `pattern` to a list of pathnames. If `recursive` is `True`, it also searches in parent directories.
*   `glob.iglob(pattern[, strict])`: Return an iterator that yields each match of the pattern. If `strict` is `True`, the function will only return matches if they exactly match the pattern, without any filename or pathname changes (for example, from `/path/to/file.txt` to `/path/to/file.txt`).
*   `glob.os_path_matches(path, pattern)`: Return `True` if `pattern` matches `path`, and `False` otherwise. The argument `path` is a full pathname.
*   `glob.os_pathnormpath(path)`: Normalize the path by removing any redundant separators or parent directory references.

**Best Practices**
------------------

*   Use `glob.glob()` for simple pattern matching, as it's more memory-efficient than using `glob.iglob()`.
*   Use `glob.iglob()` when you need to iterate over the matches instead of collecting them all in a list.
*   Be cautious with `recursive=True`, as it can lead to infinite loops if not used carefully.
*   Always check for file existence and permissions before attempting to open or read files using patterns from `glob`.
