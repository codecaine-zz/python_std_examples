# winsound — Sound-playing interface for Windows

**winsound Module Code Examples**
=====================================

The `winsound` module provides an interface for playing sounds on Windows.

### Importing the Winsound Module

```python
import winsound
```

### Playing a Beep

You can play a beep by calling the `Beep` function. The first argument is the frequency and the second argument is the duration of the sound in milliseconds.

```python
# Play a 2500 Hz beep for 500 ms
winsound.Beep(2500, 500)
```

### Playing a Wave File

You can play a wave file by calling the `PlaySound` function. The first argument is the filename of the wave file and the second argument is a flag indicating whether to wait for the sound to finish playing.

```python
import winsound
import os

# Define the path to the wave file
wave_file = "path_to_your_wave_file.wav"

# Play the wave file with a delay after it finishes
winsound.PlaySound(wave_file, winsound.SND_FILENAME)
```

### Playing a Beep with Different Modes

You can play a beep in different modes by using the following flags:

*   `SND_ASYNC`: The sound plays asynchronously.
*   `SND_WAITFINISH`: The function waits for the sound to finish playing.
*   `SND_NOREMOVE`: No error is returned if the file does not exist.

```python
# Play a 2500 Hz beep with synchronous mode and wait for it to finish
winsound.Beep(2500, 500, winsound.SND_WAITFINISH)

# Play a 2500 Hz beep with asynchronous mode
winsound.Beep(2500, 500, winsound.SND_ASYNC)
```

### Playing a Beep Without Removing Error

You can play a beep without removing the error by using the `SND_NOREMOVE` flag.

```python
# Play a 2500 Hz beep with no remove error
winsound.Beep(2500, 500, winsound.SND_NOREMOVE)
```

### Playing a Beep With Multiple Frequencies

You can play a beep with multiple frequencies by using the `Beep` function multiple times.

```python
# Play a 2000 Hz and 3000 Hz beep for 100 ms each
winsound.Beep(2000, 100)
winsound.Beep(3000, 100)
```

### Playing a Beep Without Delay

You can play a beep without delay by using the `PlaySound` function.

```python
import winsound
import os

# Define the path to the wave file
wave_file = "path_to_your_wave_file.wav"

# Play the wave file without delay
winsound.PlaySound(wave_file, 0)
```

### Playing a Beep With Volume Control

You can play a beep with volume control by using the `SetVolume` function.

```python
import winsound
import ctypes

# Get the handle to the sound device
handle = ctypes.windll.mmxctrl.mmOpenDevice(0)

# Set the initial volume to 100%
volume = winsound.SetVolume(handle, 100)

# Play a 2500 Hz beep with a volume of 50%
winsound.Beep(2500, 500, volume)
```
