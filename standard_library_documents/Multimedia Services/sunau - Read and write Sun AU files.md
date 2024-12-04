# sunau - Read and write Sun AU files

Below is a comprehensive set of code examples for the `sunau` module, which allows reading and writing Sun AU (Audio AUdio) files in Python. Each example includes comments to explain each step.

```python
# Importing the necessary module
import sunau
import wave

def read_sunau_file(file_path):
    """
    Reads a Sun AU file and returns a SoundFile object.

    Parameters:
    - file_path (str): The path to the Sun AU file.

    Returns:
    - soundfile: A SoundFile object containing the audio data.
    """
    # Open the Sun AU file in read mode
    with sunau.open(file_path, 'r') as audio_file:
        # Read all frames from the file
        frames = audio_file.readframes(-1)
        
        # Create a SoundFile object using the read frames and sample rate
        soundfile = wave.Wave_read(audio_file.framerate, frames)
    
    return soundfile

def write_sunau_file(file_path, frames, samplerate):
    """
    Writes audio frames to a Sun AU file.

    Parameters:
    - file_path (str): The path where the Sun AU file will be saved.
    - frames: An iterable of audio frames.
    - samplerate (int): The sample rate of the audio data.
    """
    # Open the Sun AU file in write mode
    with sunau.open(file_path, 'w') as audio_file:
        # Write all frames to the file
        audio_file.writeframes(frames)
    
    print(f"Audio written to {file_path}")

# Example usage

if __name__ == "__main__":
    # Read a Sun AU file
    read_sunau_example = read_sunau_file('example.au')
    print(read_sunau_example.get_params())

    # Write audio frames to a Sun AU file
    write_sunau_example = b'...'  # This should be the actual bytes of your audio data
    write_sunau_file('output.au', write_sunau_example, 44100)
```

### Explanation:

1. **Reading a Sun AU File:**
   - The `read_sunau_file` function opens a Sun AU file in read mode.
   - It reads all frames from the file using the `readframes` method of the `sunau` object.
   - A `wave.Wave_read` object is created using the sample rate and frames read.

2. **Writing a Sun AU File:**
   - The `write_sunau_file` function opens a Sun AU file in write mode.
   - It writes all frames to the file using the `writeframes` method of the `sunau` object.

3. **Example Usage:**
   - The example usage demonstrates how to read and write a Sun AU file using the functions defined above.
   - The actual audio data should be provided as bytes in the `write_sunau_file` function.

This code provides a basic framework for working with Sun AU files, including reading and writing them. You can extend these examples by adding error handling, more complex audio processing, or additional features as needed.
