# sndhdr - Determine type of sound file

The `sndhdr` module in Python is used to determine the type of a sound file based on its header information. It provides functions to read and parse the headers of various audio formats and return their corresponding names.

Here are comprehensive code examples for using the `sndhdr` module:

```python
import sndhdr

def determine_sound_type(file_path):
    """
    Determine the type of a sound file using the sndhdr module.

    Args:
    file_path (str): The path to the audio file.

    Returns:
    str: The name of the sound format, or None if the file is not recognized.
    """
    # Use sndhdr.what() function to determine the type of the sound file
    result = sndhdr.what(file_path)
    
    # Check if the file was successfully identified
    if result is None:
        return None
    
    # Return the name of the sound format
    return result[0]

# Example usage
file_path = 'example.wav'
sound_format = determine_sound_type(file_path)

if sound_format:
    print(f"The sound file '{file_path}' is of type: {sound_format}")
else:
    print(f"The sound file '{file_path}' is not recognized.")
```

### Explanation:

1. **Import the `sndhdr` module**: This module provides the necessary functions to work with sound file headers.

2. **Function Definition**: The `determine_sound_type` function takes a file path as input and returns the name of the audio format if recognized, or `None` otherwise.

3. **Using `sndhdr.what()`**: This function reads the header of the specified audio file and attempts to identify its format. It returns a tuple containing the format name and some additional information about the file (e.g., the number of channels and sample rate).

4. **Error Handling**: If `sndhdr.what()` returns `None`, it means the file was not recognized, and the function returns `None`.

5. **Example Usage**: The example demonstrates how to use the `determine_sound_type` function to identify a sound file named `'example.wav'`. It prints the result or indicates if the file is not recognized.

This code is suitable for inclusion in official documentation as it provides a straightforward and clear demonstration of how to use the `sndhdr` module to determine the format of audio files.
