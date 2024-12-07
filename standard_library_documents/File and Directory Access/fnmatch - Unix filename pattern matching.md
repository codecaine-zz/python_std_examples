# fnmatch - Unix filename pattern matching

The `fnmatch` module is used to perform shell-style pattern matching on filenames, which is particularly useful for applications that need to handle file paths and patterns according to common Unix/Linux conventions. Below are comprehensive code examples demonstrating various functionalities of the `fnmatch` module.

### Example 1: Basic Pattern Matching

```python
import fnmatch

# Define a list of filenames
filenames = [
    "document.txt",
    "images.png",
    "notes.pdf",
    "backup.tar.gz",
    "README.md"
]

# Define patterns to match files with ".txt" or ".md" extensions
patterns = ["*.txt", "*.md"]

# Use fnmatch.filter() to find filenames that match the patterns
matched_filenames = []
for pattern in patterns:
    matched_filenames.extend(fnmatch.filter(filenames, pattern))

# Print the matched filenames
print("Matched filenames:", matched_filenames)
```

### Explanation:
- **Importing `fnmatch`:** The `fnmatch` module provides a function `filter()` that can be used to filter a list of filenames based on a given pattern.
- **Pattern Definition:** The patterns `["*.txt", "*.md"]` match any file name ending with `.txt` or `.md`.
- **Function Call:** `fnmatch.filter(filenames, pattern)` returns a list of filenames that match the specified pattern.
- **Output:** The matched filenames are printed.

### Example 2: Case Insensitive Matching

```python
import fnmatch

# Define a list of filenames with mixed cases
filenames = [
    "Document.txt",
    "Images.png",
    "Notes.pdf",
    "BACKUP.tar.gz",
    "README.md"
]

# Define case-insensitive patterns to match files ending with ".txt" or ".md"
patterns = ["*.txt", "*.md"]

# Convert the patterns to case-insensitive versions
case_insensitive_patterns = [fnmatch.translate(pattern) for pattern in patterns]

# Use fnmatch.filter() with the translated patterns for case-insensitive matching
matched_filenames = []
for pattern in case_insensitive_patterns:
    matched_filenames.extend(fnmatch.filter(filenames, pattern))

# Print the matched filenames
print("Matched filenames:", matched_filenames)
```

### Explanation:
- **Case Insensitivity:** The `fnmatch.translate()` function is used to convert patterns into forms that are suitable for case-insensitive matching.
- **Pattern Translation:** The patterns `["*.txt", "*.md"]` become case-insensitive after translation.
- **Function Call:** `fnmatch.filter(filenames, case_insensitive_pattern)` returns a list of filenames that match the case-insensitive patterns.
- **Output:** The matched filenames are printed.

### Example 3: Using Wildcards in Patterns

```python
import fnmatch

# Define a list of filenames with different extensions
filenames = [
    "file1.txt",
    "file2.docx",
    "file3.pdf",
    "file4.xlsx",
    "file5.jpg"
]

# Define patterns to match files ending with ".txt" or ".docx"
patterns = ["*.txt", "*.docx"]

# Use fnmatch.filter() to find filenames that match the patterns
matched_filenames = []
for pattern in patterns:
    matched_filenames.extend(fnmatch.filter(filenames, pattern))

# Print the matched filenames
print("Matched filenames:", matched_filenames)
```

### Explanation:
- **Wildcard Usage:** The patterns `["*.txt", "*.docx"]` match any file name ending with `.txt` or `.docx`.
- **Function Call:** `fnmatch.filter(filenames, pattern)` returns a list of filenames that match the specified patterns.
- **Output:** The matched filenames are printed.

### Example 4: Matching Multiple Patterns

```python
import fnmatch

# Define a list of filenames
filenames = [
    "file1.txt",
    "file2.docx",
    "file3.pdf",
    "file4.xlsx",
    "file5.jpg"
]

# Define multiple patterns to match files ending with ".txt", ".docx", or ".pdf"
patterns = ["*.txt", "*.docx", "*.pdf"]

# Use fnmatch.filter() with each pattern in the list
matched_filenames = []
for pattern in patterns:
    matched_filenames.extend(fnmatch.filter(filenames, pattern))

# Print the matched filenames
print("Matched filenames:", matched_filenames)
```

### Explanation:
- **Multiple Patterns:** The list `["*.txt", "*.docx", "*.pdf"]` contains multiple patterns.
- **Function Call:** `fnmatch.filter(filenames, pattern)` returns a list of filenames that match the specified patterns.
- **Output:** The matched filenames are printed.

### Example 5: Using Regular Expressions for More Complex Patterns

```python
import fnmatch

# Define a list of filenames
filenames = [
    "file1.txt",
    "file2.docx",
    "file3.pdf",
    "file4.xlsx",
    "file5.jpg"
]

# Define a regular expression pattern to match files ending with ".txt", ".docx", or ".pdf"
pattern = r'\.(txt|docx|pdf)$'

# Use fnmatch.filter() with the regular expression pattern
matched_filenames = fnmatch.filter(filenames, pattern)

# Print the matched filenames
print("Matched filenames:", matched_filenames)
```

### Explanation:
- **Regular Expression Pattern:** The pattern `r'\.(txt|docx|pdf)$'` matches any file name that ends with `.txt`, `.docx`, or `.pdf`.
  - `\.` matches the literal dot (`.`) before the extension.
  - `(txt|docx|pdf)` is a group of alternatives, matching any of these extensions.
  - `$` asserts the position at the end of the string, ensuring that only filenames ending with the specified extensions are matched.
- **Function Call:** `fnmatch.filter(filenames, pattern)` returns a list of filenames that match the regular expression pattern.
- **Output:** The matched filenames are printed.

### Conclusion
The `fnmatch` module provides flexible and powerful tools for matching filenames according to Unix/Linux conventions. By understanding how to define patterns and use them with various functions like `filter()`, you can effectively manage file paths in your Python applications.
