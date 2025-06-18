# mimetypes - Map filenames to MIME types
## Table of Contents

1. [Explanation:](#explanation)



Here is a comprehensive set of code examples for using the `mimetypes` module in Python, including comments that explain each step:

```python
import mimetypes

# Function to guess the MIME type of a file based on its extension
def get_mime_type(file_path):
    """
    Given a file path, this function uses the mimetypes module to guess the MIME type.
    
    Parameters:
    - file_path (str): The path to the file whose MIME type is to be guessed.

    Returns:
    - str: The MIME type of the file, or 'application/octet-stream' if it cannot be determined.
    """
    # Guess the MIME type based on the file extension
    mime_type, _ = mimetypes.guess_type(file_path)
    
    return mime_type

# Example usage of get_mime_type function
if __name__ == "__main__":
    file_path = 'example.txt'
    mime_type = get_mime_type(file_path)
    print(f"The MIME type of {file_path} is: {mime_type}")

# Function to register a new MIME type and its corresponding extension(s)
def register_new_mimetype(mime_type, extensions):
    """
    Registers a new MIME type with the mimetypes module. This allows customizing how the
    mimetypes module handles files with specific extensions.

    Parameters:
    - mime_type (str): The MIME type to be registered.
    - extensions (list of str): A list of file extensions associated with this MIME type.
    """
    # Register the new MIME type and its extensions
    mimetypes.add_type(mime_type, *extensions)

# Example usage of register_new_mimetype function
if __name__ == "__main__":
    new_mime_type = 'application/custom'
    new_extensions = ['custom', '.cst']
    register_new_mimetype(new_mime_type, new_extensions)
    print(f"New MIME type '{new_mime_type}' registered for extensions: {new_extensions}")

# Function to display all known MIME types and their associated file extensions
def list_mime_types():
    """
    Lists all MIME types registered in the mimetypes module along with their associated file extensions.
    """
    # Retrieve a dictionary of all MIME types and their file extensions
    mime_map = mimetypes.types_map
    
    # Print each MIME type and its extensions
    for mime_type, extensions in mime_map.items():
        print(f"{mime_type}: {extensions}")

# Example usage of list_mime_types function
if __name__ == "__main__":
    list_mime_types()
```

### Explanation:

1. **`get_mime_type(file_path)`**: This function uses `mimetypes.guess_type()` to determine the MIME type of a file based on its extension. It returns the MIME type or `'application/octet-stream'` if the type cannot be determined.

2. **`register_new_mimetype(mime_type, extensions)`**: This function allows you to register a new MIME type and associate it with specific file extensions. It uses `mimetypes.add_type()` to add the mapping.

3. **`list_mime_types()`**: This function retrieves all registered MIME types and their associated file extensions from `mimetypes.types_map` and prints them out.

These examples demonstrate how to use the `mimetypes` module for basic tasks such as guessing MIME types, registering new MIME types, and listing all known MIME types. The code is designed to be clear and reusable, making it suitable for inclusion in documentation or as a standalone script.
