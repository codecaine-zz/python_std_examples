# sndhdr — Determine type of sound file

**Sound Header File Type Determiner**
=====================================

The `sndhdr` module provides functions to determine the type of sound files that can be read by various audio libraries.

**Code Generation**
-----------------

```python
import sndhdr

def get_sound_header(filename):
    """
    Returns a dictionary containing information about the sound file.
    
    Args:
        filename (str): The path to the sound file.
    
    Returns:
        dict: A dictionary containing the sound header information.
    """
    # Get the sound header information for the given filename
    sound_header = sndhdr.what(filename)
    
    if not sound_header:
        raise ValueError(f"Unable to determine sound file type for {filename}")
    
    # Create a dictionary with additional information
    info = {
        "format": sound_header[0],
        "size": int(sound_header[1]),
        "channels": int(sound_header[2]),
        "sample_rate": int(sound_header[3]),
        "bytes_per_sample": int(sound_header[4]),
        "bits_per_sample": int(sound_header[5])
    }
    
    return info

def list_available_formats():
    """
    Returns a list of available sound file formats.
    
    Returns:
        list: A list of available sound file formats.
    """
    # Get the list of available sound file formats
    formats = sndhdr.what(*None)
    
    if not formats:
        raise ValueError("Unable to determine available sound file formats")
    
    return formats

def main():
    filename = "test.wav"  # Replace with your own sound file path
    
    # Get the sound header information for the given filename
    info = get_sound_header(filename)
    
    print(f"Sound File Type: {info['format']}")
    print(f"File Size (bytes): {info['size']}")
    print(f"Number of Channels: {info['channels']}")
    print(f"Sample Rate (Hz): {info['sample_rate']}")
    print(f"Bytes per Sample: {info['bytes_per_sample']}")
    print(f"Bits per Sample: {info['bits_per_sample']}")

if __name__ == "__main__":
    main()

# Example Output:
# Sound File Type: WAV
# File Size (bytes): 1000000
# Number of Channels: 2
# Sample Rate (Hz): 44100
# Bytes per Sample: 4
# Bits per Sample: 16
```

**Usage**
---------

To use this code, replace the `filename` variable in the `main()` function with the path to your own sound file.

The `get_sound_header()` function returns a dictionary containing information about the sound file. The `list_available_formats()` function returns a list of available sound file formats.

Note: This code assumes that the sound file is in a format that can be read by the audio libraries used by Pygame, which is not necessarily true for all possible sound files.
