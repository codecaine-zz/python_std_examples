# ossaudiodev - Access to OSS-compatible audio devices
## Table of Contents

1. [Key Points:](#key-points)



The `ossaudiodev` module in Python provides low-level access to OSS (Open Sound System) compatible audio devices. OSS is a Unix-like sound system that has been used on many Linux distributions, as well as other systems like FreeBSD and Solaris.

Below are comprehensive code examples for the `ossaudiodev` module, covering various functionalities such as opening a device, setting parameters, playing and recording audio, and closing the device:

```python
import ossaudiodev

# Example 1: Open an OSS audio device for output (e.g., ALSA)
def open_audio_output():
    """
    Opens an OSS audio device for output.
    
    Returns:
        file-like object: A file-like object that can be used to write audio data.
    """
    try:
        # Open a file in binary mode
        out_device = ossaudiodev.open('w', -1)
        
        # Set the number of channels (e.g., 2 for stereo)
        out_device.setchannels(2)
        
        # Set the sample rate (e.g., 44100 Hz)
        out_device.setrate(44100)
        
        # Set the format (e.g., 8-bit mono, 16-bit stereo)
        out_device.setformat(ossaudiodev.AFMT_S16_LE)  # or AFMT_U8 for 8-bit
        
        return out_device
    except Exception as e:
        print(f"Error opening audio output device: {e}")
        return None

# Example 2: Open an OSS audio device for input (e.g., ALSA)
def open_audio_input():
    """
    Opens an OSS audio device for input.
    
    Returns:
        file-like object: A file-like object that can be used to read audio data.
    """
    try:
        # Open a file in binary mode
        in_device = ossaudiodev.open('r', -1)
        
        # Set the number of channels (e.g., 2 for stereo)
        in_device.setchannels(2)
        
        # Set the sample rate (e.g., 44100 Hz)
        in_device.setrate(44100)
        
        # Set the format (e.g., 8-bit mono, 16-bit stereo)
        in_device.setformat(ossaudiodev.AFMT_S16_LE)  # or AFMT_U8 for 8-bit
        
        return in_device
    except Exception as e:
        print(f"Error opening audio input device: {e}")
        return None

# Example 3: Play an audio file using open_audio_output
def play_audio_file(filename, out_device):
    """
    Plays an audio file using the provided output device.
    
    Args:
        filename (str): The path to the audio file.
        out_device (file-like object): An OSS audio device opened for output.
    """
    try:
        with open(filename, 'rb') as infile:
            data = infile.read()
            while data:
                out_device.write(data)
                data = infile.read()
        print("Audio playback complete.")
    except Exception as e:
        print(f"Error playing audio file: {e}")

# Example 4: Record an audio file using open_audio_input
def record_audio_file(filename, in_device):
    """
    Records an audio file from the provided input device.
    
    Args:
        filename (str): The path to save the recorded audio file.
        in_device (file-like object): An OSS audio device opened for input.
    """
    try:
        with open(filename, 'wb') as outfile:
            while True:
                data = in_device.read(1024)
                if not data:
                    break
                outfile.write(data)
        print("Audio recording complete.")
    except Exception as e:
        print(f"Error recording audio file: {e}")

# Example 5: Close the OSS audio devices
def close_audio_devices(out_device, in_device):
    """
    Closes the provided OSS audio devices.
    
    Args:
        out_device (file-like object): The output device to close.
        in_device (file-like object): The input device to close.
    """
    try:
        if out_device:
            out_device.close()
        if in_device:
            in_device.close()
        print("Audio devices closed.")
    except Exception as e:
        print(f"Error closing audio devices: {e}")

# Example usage
if __name__ == "__main__":
    # Open an output device for playback
    out_device = open_audio_output()
    
    # Play a sample audio file
    play_audio_file('path_to_sample.wav', out_device)
    
    # Close the output device
    close_audio_devices(out_device, None)

    # Optionally, open an input device and record an audio file
    in_device = open_audio_input()
    if in_device:
        record_audio_file('recorded_audio.wav', in_device)
        close_audio_devices(None, in_device)
```

### Key Points:

1. **Device Open**: The `open` function is used to open a device for either output or input. It takes two arguments: the mode ('w' for write, 'r' for read) and an index (usually `-1` for default).

2. **Parameters**: Functions like `setchannels`, `setrate`, and `setformat` are used to set the number of channels, sample rate, and audio format respectively.

3. **File-like Operations**: The device is treated as a file object, allowing you to write or read data using standard I/O operations (`write` and `read`).

4. **Error Handling**: Basic error handling is included to catch and print exceptions that may occur during device opening or operations.

5. **Closing Devices**: Always close the devices after use to free up resources and ensure proper cleanup.

These examples provide a comprehensive introduction to using the `ossaudiodev` module for audio processing tasks in Python.
