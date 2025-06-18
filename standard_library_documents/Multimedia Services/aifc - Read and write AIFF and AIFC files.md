# aifc - Read and write AIFF and AIFC files
## Table of Contents

1. [Example 1: Writing an AIFF Audio File](#example-1-writing-an-aiff-audio-file)
2. [Example 2: Reading an AIFF Audio File](#example-2-reading-an-aiff-audio-file)
3. [Example 3: Writing an AIFF-C Audio File](#example-3-writing-an-aiff-c-audio-file)
4. [Example 4: Reading an AIFF-C Audio File](#example-4-reading-an-aiff-c-audio-file)
5. [Example 5: Handling Different Sample Widths](#example-5-handling-different-sample-widths)
6. [Example 6: Handling Different Compression Types](#example-6-handling-different-compression-types)



The `aifc` module in Python is used to read and write AIFF (Audio Interchange File Format) and AIFC (AIFF-C, which stands for Audio Interchange File Format with Compression) audio files. These formats are commonly used for digital music files and are widely supported across various platforms.

Below are comprehensive code examples for common tasks related to reading and writing AIFF/AIFC files using the `aifc` module:

### Example 1: Writing an AIFF Audio File

```python
import aifc

def write_aiff_file(filename, frames, sample_rate, channels):
    """
    Write audio data to an AIFF file.

    Parameters:
    - filename (str): The name of the output AIFF file.
    - frames (array-like): The audio data in the form of a sequence of samples.
    - sample_rate (int): The sampling rate of the audio data in Hz.
    - channels (int): The number of channels (1 for mono, 2 for stereo).
    """
    with aifc.open(filename, 'wb') as wavf:
        # Set the parameters
        wavf.setnchannels(channels)
        wavf.setsampwidth(2)  # 16-bit samples
        wavf.setframerate(sample_rate)

        # Write the audio frames to the file
        wavf.writeframes(frames.tobytes())

# Example usage
audio_data = np.array([32768, 0, -32768, 0], dtype=np.int16)  # 4 samples at 16-bit resolution
write_aiff_file('output.aif', audio_data, sample_rate=44100, channels=1)
```

### Example 2: Reading an AIFF Audio File

```python
import aifc
import numpy as np

def read_aiff_file(filename):
    """
    Read audio data from an AIFF file.

    Parameters:
    - filename (str): The name of the input AIFF file.

    Returns:
    - tuple: A tuple containing the audio data, sampling rate, and number of channels.
    """
    with aifc.open(filename, 'rb') as wavf:
        # Read the parameters
        nchannels = wavf.getnchannels()
        sampwidth = wavf.getsampwidth()
        sample_rate = wavf.getframerate()

        # Read all frames and convert to numpy array
        audio_data = np.frombuffer(wavf.readframes(-1), dtype=np.int16)

    return audio_data, sample_rate, nchannels

# Example usage
audio_data, sample_rate, channels = read_aiff_file('input.aif')
print(f"Audio Data: {audio_data}")
print(f"Sample Rate: {sample_rate} Hz")
print(f"Number of Channels: {channels}")
```

### Example 3: Writing an AIFF-C Audio File

AIFF-C is a compressed version of the AIFF format. It uses either the u-law or A-LAW compression schemes for audio data.

```python
import aifc
import numpy as np

def write_aiff_c_file(filename, frames, sample_rate, channels, compression_type='u-law'):
    """
    Write audio data to an AIFF-C file with specified compression type.

    Parameters:
    - filename (str): The name of the output AIFF-C file.
    - frames (array-like): The audio data in the form of a sequence of samples.
    - sample_rate (int): The sampling rate of the audio data in Hz.
    - channels (int): The number of channels (1 for mono, 2 for stereo).
    - compression_type (str): The compression type ('u-law' or 'a-law').
    """
    with aifc.open(filename, 'wb') as wavf:
        # Set the parameters
        wavf.setnchannels(channels)
        wavf.setsampwidth(1)  # 8-bit samples
        wavf.setframerate(sample_rate)

        if compression_type == 'u-law':
            wavf.setcomptype('ULAW')
        elif compression_type == 'a-law':
            wavf.setcomptype('A-LAW')
        else:
            raise ValueError("Unsupported compression type. Use 'u-law' or 'a-law'.")

        # Write the audio frames to the file
        wavf.writeframes(frames.tobytes())

# Example usage
audio_data = np.array([32, 0, -16, 0], dtype=np.int8)  # 4 samples at 8-bit resolution
write_aiff_c_file('output.aifc', audio_data, sample_rate=44100, channels=1, compression_type='u-law')
```

### Example 4: Reading an AIFF-C Audio File

```python
import aifc
import numpy as np

def read_aiff_c_file(filename):
    """
    Read audio data from an AIFF-C file.

    Parameters:
    - filename (str): The name of the input AIFF-C file.

    Returns:
    - tuple: A tuple containing the audio data, sampling rate, and number of channels.
    """
    with aifc.open(filename, 'rb') as wavf:
        # Read the parameters
        nchannels = wavf.getnchannels()
        sampwidth = wavf.getsampwidth()
        sample_rate = wavf.getframerate()

        # Determine compression type
        if wavf.getcomptype() == 'ULAW':
            dtype = np.int8  # u-law samples are stored as 8-bit integers
        elif wavf.getcomptype() == 'A-LAW':
            dtype = np.int8  # a-law samples are stored as 8-bit integers
        else:
            raise ValueError("Unsupported compression type. Use 'u-law' or 'a-law'.")

        # Read all frames and convert to numpy array
        audio_data = np.frombuffer(wavf.readframes(-1), dtype=dtype)

    return audio_data, sample_rate, nchannels

# Example usage
audio_data, sample_rate, channels = read_aiff_c_file('input.aifc')
print(f"Audio Data: {audio_data}")
print(f"Sample Rate: {sample_rate} Hz")
print(f"Number of Channels: {channels}")
```

### Example 5: Handling Different Sample Widths

The `aifc` module can handle different sample widths, which are specified using the `setsampwidth` method. This allows you to work with audio data in various bit depths.

```python
import aifc
import numpy as np

def write_custom_aiff_file(filename, frames, sample_rate, channels, sample_width):
    """
    Write audio data to an AIFF file with a specified sample width.

    Parameters:
    - filename (str): The name of the output AIFF file.
    - frames (array-like): The audio data in the form of a sequence of samples.
    - sample_rate (int): The sampling rate of the audio data in Hz.
    - channels (int): The number of channels (1 for mono, 2 for stereo).
    - sample_width (int): The sample width in bytes (e.g., 1 for 8-bit, 2 for 16-bit).
    """
    with aifc.open(filename, 'wb') as wavf:
        # Set the parameters
        wavf.setnchannels(channels)
        wavf.setsampwidth(sample_width)
        wavf.setframerate(sample_rate)

        # Write the audio frames to the file
        wavf.writeframes(frames.tobytes())

# Example usage
audio_data = np.array([32, 0, -16, 0], dtype=np.int8)  # 4 samples at 8-bit resolution
write_custom_aiff_file('output_custom.aif', audio_data, sample_rate=44100, channels=1, sample_width=1)
```

### Example 6: Handling Different Compression Types

AIFF-C supports compression types like U-LAW and A-LAW. These are set using the `setcomptype` method.

```python
import aifc
import numpy as np

def write_custom_aiff_c_file(filename, frames, sample_rate, channels, compression_type='u-law'):
    """
    Write audio data to an AIFF-C file with a specified compression type.

    Parameters:
    - filename (str): The name of the output AIFF-C file.
    - frames (array-like): The audio data in the form of a sequence of samples.
    - sample_rate (int): The sampling rate of the audio data in Hz.
    - channels (int): The number of channels (1 for mono, 2 for stereo).
    - compression_type (str): The compression type ('u-law' or 'a-law').
    """
    with aifc.open(filename, 'wb') as wavf:
        # Set the parameters
        wavf.setnchannels(channels)
        wavf.setsampwidth(1)  # 8-bit samples
        wavf.setframerate(sample_rate)

        if compression_type == 'u-law':
            wavf.setcomptype('ULAW')
        elif compression_type == 'a-law':
            wavf.setcomptype('A-LAW')
        else:
            raise ValueError("Unsupported compression type. Use 'u-law' or 'a-law'.")

        # Write the audio frames to the file
        wavf.writeframes(frames.tobytes())

# Example usage
audio_data = np.array([32, 0, -16, 0], dtype=np.int8)  # 4 samples at 8-bit resolution
write_custom_aiff_c_file('output_custom.aifc', audio_data, sample_rate=44100, channels=1, compression_type='u-law')
```

These examples demonstrate how to use the `aifc` module to create and read AIFF and AIFF-C files with different sample widths, compression types, and formats. The code is designed to be clear and self-contained, allowing you to easily integrate audio handling into your applications.
