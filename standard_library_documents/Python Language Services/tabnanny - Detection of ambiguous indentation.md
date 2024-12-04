# tabnanny — Detection of ambiguous indentation

**TabNanny Code Generator**
=====================================

The `tabnanny` module is part of the Python standard library, and it provides a function to detect ambiguous indentation in Python source code.

**Usage:**

```python
import tabnanny

# Create an instance of TabNanny with default settings
tab_nanny = tabnanny.TabNanny()

# Check if the given source code has any ambiguous indentation
if not tab_nanny.check(file_content):
    print("Ambiguous indentation detected.")
else:
    print("No ambiguous indentation detected.")

# Check if a specific line has ambiguous indentation
line_number = 10  # Line numbers are 1-indexed
if not tab_nanny.check_line(line_number, file_content):
    print(f"Ambiguous indentation detected on line {line_number}.")
else:
    print(f"No ambiguity detected on line {line_number}.")

# Customizable settings for TabNanny
tab_nanny.settings = {
    # Enable or disable specific features
    "ignore_implicit_as": True,
    "enforce_indentation": False,
    "max_line_length": 100,
}

if not tab_nanny.check(file_content):
    print("Ambiguous indentation detected with custom settings.")
else:
    print("No ambiguous indentation detected with custom settings.")

```

**API Documentation:**

### `TabNanny()`

*   Initializes a new instance of the `TabNanny` class.

### `check(source_code)`

*   Checks if the given source code has any ambiguous indentation.
*   Returns `True` if there is no ambiguity, and `False` otherwise.

### `check_line(line_number, source_code)`

*   Checks if a specific line in the source code has ambiguous indentation.
*   Returns `True` if there is an ambiguity, and `False` otherwise.

### `settings`

*   A dictionary of custom settings for the `TabNanny` instance. The keys are feature names, and the values are booleans indicating whether to enable or disable that feature. Other keys can be used to set additional options, such as `max_line_length`.

**Example Output:**

```python
# Source code with ambiguous indentation
file_content = """
if True:
    # This line should have 4 spaces of indentation,
    # but Python has a bug and it's only 2.
    print('Hello')
"""

tab_nanny = tabnanny.TabNanny()
if not tab_nanny.check(file_content):
    print("Ambiguous indentation detected.")
else:
    print("No ambiguous indentation detected.")

# Output: Ambiguous indentation detected.

```
