# wave — Read and write WAV files

**Wave Module Code Examples**
=====================================

The `wave` module provides functions to read and write WAV (Waveform Audio File Format) files.

### Importing the Wave Module
```python
import wave
```

### Creating a New WAV File
```python
# Open a new file in write binary mode
with open('new_file.wav', 'wb') as wav_file:
    # Create a WAV header with specific parameters
    wav_header = b'RIFF'
    wav_header += len(wav_file).to_bytes(4, byteorder='little')
    wav_header += b'WAVE'
    wav_header += b-format
    wav_header += b'data'
    
    # Write the header to the file
    wav_file.write(wav_header)
    
    # Create a sample audio data block
    for i in range(1000):
        data = (i * 10).to_bytes(2, byteorder='little')
        # Write the data to the file
        wav_file.write(data)
```

### Reading a WAV File
```python
# Open an existing file in read binary mode
with open('existing_file.wav', 'rb') as wav_file:
    # Read the header from the file
    wav_header = wav_file.read(36)
    
    # Check if it's a valid WAV header
    if len(wav_header) < 36 or wav_header[:4] != b'RIFF':
        raise ValueError('Invalid WAV header')
    
    # Extract audio data parameters from the header
    format = wav_header[6:10].decode()
    num_channels = int.from_bytes(wav_header[10:14], byteorder='little')
    sample_width = int.from_bytes(wav_header[14:18], byteorder='little')
    frame_rate = int.from_bytes(wav_header[18:24], byteorder='little')
    num_frames = int.from_bytes(wav_header[24:28], byteorder='little')
    
    # Read audio data from the file
    wav_data = wav_file.read()
```

### Playing a WAV File
```python
import pyaudio

# Open a new file in read binary mode
wav_file = open('file.wav', 'rb')

# Create a PyAudio object
p = pyaudio.PyAudio()

# Open a stream for playback
stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=44100,
                output=True)

# Read audio data from the file and write it to the stream
data = wav_file.read()
while len(data) > 0:
    # Write the audio data to the stream
    stream.write(data)
    
    # Clear the buffer for the next frame
    data = b''

# Close the stream and PyAudio object
stream.stop_stream()
stream.close()
p.terminate()

# Close the WAV file
wav_file.close()
```

### Writing a Multi-Channel WAV File
```python
import numpy as np

# Create a sample audio data block with multiple channels
data = np.random.rand(1000, 3).astype(np.int16)

# Open a new file in write binary mode
with open('multi_channel_file.wav', 'wb') as wav_file:
    # Write the header to the file
    wav_header = b'RIFF'
    wav_header += len(wav_file).to_bytes(4, byteorder='little')
    wav_header += b'WAVE'
    wav_header += b'fmt '
    wav_header += '36'.encode()
    wav_header += b'data'
    
    # Write the header to the file
    wav_file.write(wav_header)
    
    # Write audio data to the file for each channel
    for channel in range(3):
        # Calculate sample width based on the number of channels
        if channel == 0:
            sample_width = 2
        elif channel == 1:
            sample_width = 4
        else:
            sample_width = 8
        
        # Write audio data to the file for this channel
        wav_data = data.channel(channel).tobytes()
        wav_file.write(wav_data)
```

Note: The above examples are just a selection of the many things you can do with the `wave` module. This module provides functions for reading and writing WAV files, including support for multiple channels, stereo audio, and other features.
