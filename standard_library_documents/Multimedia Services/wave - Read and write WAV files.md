# wave - Read and write WAV files

The `wave` module in Python provides a way to read from and write WAV files, which are a widely used format for storing audio data. Below are comprehensive examples demonstrating how to use various functionalities of the `wave` module. These examples include reading and writing basic audio files, handling stereo files, using different sample formats, and dealing with compression.

### Example 1: Reading and Writing Basic WAV Files

```python
import wave

# Function to read a WAV file
def read_wav(file_path):
    # Open the WAV file in read mode
    wav_file = wave.open(file_path, 'rb')
    
    # Read the WAV header information
    nchannels, sampwidth, framerate, nframes, comptype, compname = wav_file.getparams()
    
    # Read the audio data as bytes
    audio_data = wav_file.readframes(nframes)
    
    # Close the file
    wav_file.close()
    
    return nchannels, sampwidth, framerate, nframes, audio_data

# Function to write a WAV file
def write_wav(file_path, nchannels, sampwidth, framerate, nframes, audio_data):
    # Open the WAV file in write mode
    with wave.open(file_path, 'wb') as wav_file:
        # Write the WAV header information
        wav_file.setnchannels(nchannels)
        wav_file.setsampwidth(sampwidth)
        wav_file.setframerate(framerate)
        wav_file.writeframes(audio_data)

# Example usage
input_file = 'input.wav'
output_file = 'output.wav'

# Read the input WAV file
nchannels, sampwidth, framerate, nframes, audio_data = read_wav(input_file)

# Write the output WAV file with same parameters
write_wav(output_file, nchannels, sampwidth, framerate, nframes, audio_data)

print(f"Read and written {output_file}")
```

### Example 2: Reading and Writing Stereo WAV Files

```python
import wave

def read_wav(file_path):
    wav_file = wave.open(file_path, 'rb')
    nchannels, sampwidth, framerate, nframes, comptype, compname = wav_file.getparams()
    audio_data = wav_file.readframes(nframes)
    wav_file.close()
    return nchannels, sampwidth, framerate, nframes, audio_data

def write_wav(file_path, nchannels, sampwidth, framerate, nframes, audio_data):
    with wave.open(file_path, 'wb') as wav_file:
        wav_file.setnchannels(nchannels)
        wav_file.setsampwidth(sampwidth)
        wav_file.setframerate(framerate)
        wav_file.writeframes(audio_data)

# Example usage for stereo WAV file
input_stereo_file = 'input_stereo.wav'
output_stereo_file = 'output_stereo.wav'

# Read the input stereo WAV file
nchannels, sampwidth, framerate, nframes, audio_data = read_wav(input_stereo_file)

# Write the output stereo WAV file with same parameters
write_wav(output_stereo_file, nchannels, sampwidth, framerate, nframes, audio_data)

print(f"Read and written {output_stereo_file}")
```

### Example 3: Reading and Writing Files in Different Sample Formats

```python
import wave

def read_wav(file_path):
    wav_file = wave.open(file_path, 'rb')
    nchannels, sampwidth, framerate, nframes, comptype, compname = wav_file.getparams()
    audio_data = wav_file.readframes(nframes)
    wav_file.close()
    return nchannels, sampwidth, framerate, nframes, audio_data

def write_wav(file_path, nchannels, sampwidth, framerate, nframes, audio_data):
    with wave.open(file_path, 'wb') as wav_file:
        wav_file.setnchannels(nchannels)
        wav_file.setsampwidth(sampwidth)
        wav_file.setframerate(framerate)
        wav_file.writeframes(audio_data)

# Example usage for different sample formats (16-bit and 8-bit)
input_16bit_file = 'input_16bit.wav'
output_16bit_file = 'output_16bit.wav'

input_8bit_file = 'input_8bit.wav'
output_8bit_file = 'output_8bit.wav'

# Read the input 16-bit WAV file
nchannels, sampwidth_16bit, framerate, nframes_16bit, audio_data_16bit = read_wav(input_16bit_file)

# Write the output 16-bit WAV file with same parameters
write_wav(output_16bit_file, nchannels, sampwidth_16bit, framerate, nframes_16bit, audio_data_16bit)

print(f"Read and written {output_16bit_file}")

# Read the input 8-bit WAV file
nchannels, sampwidth_8bit, framerate, nframes_8bit, audio_data_8bit = read_wav(input_8bit_file)

# Write the output 8-bit WAV file with same parameters
write_wav(output_8bit_file, nchannels, sampwidth_8bit, framerate, nframes_8bit, audio_data_8bit)

print(f"Read and written {output_8bit_file}")
```

### Example 4: Handling Compression in WAV Files

```python
import wave

def read_wav(file_path):
    wav_file = wave.open(file_path, 'rb')
    nchannels, sampwidth, framerate, nframes, comptype, compname = wav_file.getparams()
    audio_data = wav_file.readframes(nframes)
    wav_file.close()
    return nchannels, sampwidth, framerate, nframes, audio_data

def write_wav(file_path, nchannels, sampwidth, framerate, nframes, audio_data):
    with wave.open(file_path, 'wb') as wav_file:
        wav_file.setnchannels(nchannels)
        wav_file.setsampwidth(sampwidth)
        wav_file.setframerate(framerate)
        wav_file.writeframes(audio_data)

# Example usage for compressed WAV file (e.g., using Compressed PCM)
input_compressed_file = 'compressed_input.wav'
output_compressed_file = 'compressed_output.wav'

# Read the input compressed WAV file
nchannels, sampwidth, framerate, nframes, comptype, compname = read_wav(input_compressed_file)

# Write the output compressed WAV file with same parameters
write_wav(output_compressed_file, nchannels, sampwidth, framerate, nframes, audio_data)

print(f"Read and written {output_compressed_file}")
```

These examples demonstrate basic operations for reading and writing WAV files using the `wave` module. You can extend these examples to handle more complex scenarios, such as multi-channel audio or different sample rates.
