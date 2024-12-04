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

# Define a pattern to match files with ".txt" or ".md" extensions
pattern = "*.txt|*.md"

# Use fnmatch.filter() to find filenames that match the pattern
matched_filenames = fnmatch.filter(filenames, pattern)

# Print the matched filenames
print("Matched filenames:", matched_filenames)
```

### Explanation:
- **Importing `fnmatch`:** The `fnmatch` module provides a function `filter()` that can be used to filter a list of filenames based on a given pattern.
- **Pattern Definition:** The pattern `"*.txt|*.md"` matches any file name ending with `.txt` or `.md`.
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

# Define a case-insensitive pattern to match files ending with ".txt" or ".md"
pattern = "*.txt|*.md"

# Convert the pattern to a case-insensitive version
case_insensitive_pattern = fnmatch.translate(pattern)

# Use fnmatch.filter() with the translated pattern for case-insensitive matching
matched_filenames = fnmatch.filter(filenames, case_insensitive_pattern)

# Print the matched filenames
print("Matched filenames:", matched_filenames)
```

### Explanation:
- **Case Insensitivity:** The `fnmatch.translate()` function is used to convert a pattern into a form that is suitable for case-insensitive matching.
- **Pattern Translation:** The pattern `"*.txt|*.md"` becomes `r'(?i)(\.txt|\.md)'` after translation, which matches filenames with `.TXT`, `.TEXT`, etc., as well as `.txt` and `.md`.
- **Function Call:** `fnmatch.filter(filenames, case_insensitive_pattern)` returns a list of filenames that match the case-insensitive pattern.
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

# Define a pattern to match files ending with ".txt" or ".docx"
pattern = "*.txt|*.docx"

# Use fnmatch.filter() to find filenames that match the pattern
matched_filenames = fnmatch.filter(filenames, pattern)

# Print the matched filenames
print("Matched filenames:", matched_filenames)
```

### Explanation:
- **Wildcard Usage:** The pattern `"*.txt|*.docx"` matches any file name ending with `.txt` or `.docx`.
- **Function Call:** `fnmatch.filter(filenames, pattern)` returns a list of filenames that match the specified pattern.
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
matched_filenames = [fnmatch.filter(filenames, p) for p in patterns]

# Print the matched filenames for each pattern
for i, matched in enumerate(matched_filenames):
    print("Matched filenames for pattern '{}':".format(patterns[i]))
    print(matched)
```

### Explanation:
- **Multiple Patterns:** The list `["*.txt", "*.docx", "*.pdf"]` contains multiple patterns.
- **List Comprehension:** A list comprehension is used to apply `fnmatch.filter()` to each pattern in the list, resulting in a list of lists where each sublist contains filenames that match the corresponding pattern.
- **Output:** The matched filenames for each pattern are printed.

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
