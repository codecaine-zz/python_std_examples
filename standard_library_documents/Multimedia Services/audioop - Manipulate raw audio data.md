# audioop - Manipulate raw audio data
## Table of Contents

1. [Example 1: Reading Audio Data from a File](#example-1-reading-audio-data-from-a-file)
2. [Example 2: Converting Audio Data to Different Formats](#example-2-converting-audio-data-to-different-formats)
3. [Example 3: Calculating the RMS (Root Mean Square) of Audio Data](#example-3-calculating-the-rms-root-mean-square-of-audio-data)
4. [Example 4: Applying a Volume Adjustment to Audio Data](#example-4-applying-a-volume-adjustment-to-audio-data)
5. [Example 5: Writing Audio Data to a File](#example-5-writing-audio-data-to-a-file)
6. [Explanation](#explanation)



The `audioop` module in Python provides functions to manipulate raw audio data, such as converting between different sample formats and performing various operations on audio samples. Below are comprehensive examples of how to use these functions, along with explanations for each step.

### Example 1: Reading Audio Data from a File

```python
import wave

def read_audio_data(filename):
    """
    Reads audio data from a WAV file and returns the sample rate, number of channels,
    and audio frames as a list of bytes.
    """
    with wave.open(filename, 'rb') as wav_file:
        # Get the parameters (sample rate, number of channels, bits per sample)
        params = wav_file.getparams()
        
        # Read all the audio data
        audio_frames = wav_file.readframes(params.nframes)
        
        return params.samplerate, params.nchannels, audio_frames

# Example usage
sample_rate, num_channels, audio_data = read_audio_data('example.wav')
print(f"Sample Rate: {sample_rate} Hz")
print(f"Number of Channels: {num_channels}")
```

### Example 2: Converting Audio Data to Different Formats

```python
import wave
import audioop

def convert_to_int16(audio_frames):
    """
    Converts a sequence of bytes representing audio frames into signed 16-bit integers.
    Assumes the input is in unsigned 8-bit format.
    """
    # Convert to signed 16-bit using audioop.lin2lin()
    converted_audio = audioop.lin2lin(audio_frames, 'U', 'S')
    return converted_audio

# Example usage
sample_rate, num_channels, audio_data = read_audio_data('example.wav')
converted_audio = convert_to_int16(audio_data)
```

### Example 3: Calculating the RMS (Root Mean Square) of Audio Data

```python
import wave
import audioop

def calculate_rms(audio_frames):
    """
    Calculates the root mean square (RMS) of a sequence of bytes representing audio frames.
    Assumes the input is in signed 16-bit format.
    """
    # Calculate RMS using audioop.rms()
    rms = audioop.rms(audio_frames, 2)
    return rms

# Example usage
sample_rate, num_channels, audio_data = read_audio_data('example.wav')
converted_audio = convert_to_int16(audio_data)
rms_value = calculate_rms(converted_audio)
print(f"RMS Value: {rms_value}")
```

### Example 4: Applying a Volume Adjustment to Audio Data

```python
import wave
import audioop

def apply_volume_adjustment(audio_frames, volume_factor):
    """
    Applies a volume adjustment to a sequence of bytes representing audio frames.
    Assumes the input is in signed 16-bit format.
    """
    # Apply volume adjustment using audioop.mul()
    adjusted_audio = audioop.mul(audio_frames, 2, volume_factor)
    return adjusted_audio

# Example usage
sample_rate, num_channels, audio_data = read_audio_data('example.wav')
converted_audio = convert_to_int16(audio_data)
volume_adjusted_audio = apply_volume_adjustment(converted_audio, 0.5)  # Half the original volume
```

### Example 5: Writing Audio Data to a File

```python
import wave

def write_audio_data(filename, sample_rate, num_channels, audio_frames):
    """
    Writes raw audio data to a WAV file.
    """
    with wave.open(filename, 'wb') as wav_file:
        # Write the parameters (sample rate, number of channels, bits per sample)
        wav_file.setnchannels(num_channels)
        wav_file.setsampwidth(2)  # Signed 16-bit
        wav_file.setframerate(sample_rate)
        
        # Write all the audio data
        wav_file.writeframes(audio_frames)

# Example usage
sample_rate = 44100
num_channels = 2
audio_data = converted_audio  # Use converted data from previous example
write_audio_data('output.wav', sample_rate, num_channels, audio_data)
```

### Explanation

- **Reading Audio Data**: The `wave` module is used to open and read audio files. The `getparams()` method retrieves the format parameters (sample rate, number of channels, bits per sample), and `readframes()` reads all the frames.
  
- **Converting Formats**: The `audioop.lin2lin()` function converts between different linear sample formats.

- **Calculating RMS**: The `audioop.rms()` function calculates the root mean square of audio data, which is a measure of its power or loudness.

- **Volume Adjustment**: The `audioop.mul()` function multiplies each sample in the audio data by a volume factor, effectively changing the volume level.

- **Writing Audio Data**: The `wave` module is used to write audio data back to a file with specified parameters and frames.

These examples demonstrate how to manipulate audio data using the `audioop` module in Python. Each function is thoroughly documented to ensure clarity and ease of use in real-world applications.
