# msvcrt - Useful routines from the MS VC++ runtime

Here are some useful code examples using the `msvcrt` module from the Python Standard Library.

**Getting User Input**
```python
import msvcrt

# Get user input without echoing to the console
input_str = msvcrt.getch().decode('utf-8').strip()
print("You entered:", input_str)
```

**Checking for Keyboard Presses**
```python
import msvcrt

while True:
    # Check if a key is pressed
    if msvcrt.kbhit():
        # Get the pressed key
        key = msvcrt.getche().decode('utf-8').strip()
        print("Key pressed:", key)
```

**Getting Character from Keyboard without Echoing**
```python
import msvcrt

char = msvcrt.getch().decode('utf-8')
print("You entered character:", char)
```

**Reading a Whole Line from Keyboard without Echoing**
```python
import msvcrt

line = msvcrt.getwcha()
print("You entered line:", line.decode('utf-8'))
```

**Waiting for Enter Key Press**
```python
import msvcrt
import time

# Wait for the enter key press
input("Press Enter to continue...")

# Check if a key is pressed
if msvcrt.kbhit():
    # Get the pressed key
    key = msvcrt.getche().decode('utf-8').strip()
    print("Key pressed:", key)
```

**Clearing Screen**
```python
import os
import msvcrt

# Clear the screen
os.system('cls' if os.name == 'nt' else 'clear')

# Print some text to clear the screen
print("Press Enter to continue...")
msvcrt.getch()
```
Please note that `msvcrt` is not a part of Python's standard library, it's included in Windows API. If you are using a non-Windows operating system, you will need to use alternative libraries or implement these functionalities manually.

This examples demonstrate how the `msvcrt` module can be used for various tasks related to keyboard input and output on Windows platforms.
