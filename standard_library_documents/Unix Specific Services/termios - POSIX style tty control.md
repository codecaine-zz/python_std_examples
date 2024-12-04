# termios — POSIX style tty control

**Termios Module: POSIX Style TTY Control**
=====================================================

The `termios` module provides an interface to access and modify the terminal I/O settings.

**Importing the Termios Module**
-------------------------------

```python
import termios
```

**Getting the Current Terminal Settings**
-----------------------------------------

You can get the current terminal settings using the `tcgetattr()` function, which returns a new file descriptor set containing the current settings.

```python
# Get the current terminal settings
try:
    # Create a copy of the current terminal settings
    current_settings = termios.tcgetattr(sys.stdout)
except OSError as e:
    print(f"Error: {e}")
```

**Setting Terminal Settings**
---------------------------

You can set the terminal settings using the `tcsetattr()` function, which takes two arguments: the file descriptor to be modified and a new terminal settings.

```python
# Set terminal settings for standard output (sys.stdout)
try:
    # Create a copy of the current terminal settings
    new_settings = termios.tcgetattr(sys.stdout)

    # Modify the settings as needed
    # For example, set the terminal speed to 9600 baud and 8 bits per character
    new_settings[5] = termios.B9600 | termios.CLOCAL | termios.CREAD
    new_settings[6] = termios.O_NONBLOCK

    # Apply the new settings
    sys.stdout.write("\x1B[" + str(new_settings[2]) + "A")
except OSError as e:
    print(f"Error: {e}")
```

**Special Values for Terminal Settings**
---------------------------------------

The `termios` module defines several special values that can be used to modify the terminal settings.

*   `termios.TCSANOW`: Use the new setting immediately.
*   `termios.TCSAFLUSH`: Flush the output buffer before applying the new setting.
*   `termios.VMIN`: Minimum number of bytes required for input.
*   `termios.VTIME`: Time in hundredths of a second to wait for input.

```python
# Set terminal settings with special values
try:
    # Create a copy of the current terminal settings
    new_settings = termios.tcgetattr(sys.stdout)

    # Modify the settings as needed
    new_settings[5] = termios.B9600 | termios.CLOCAL | termios.CREAD
    new_settings[6] = 0x1f80

    # Apply the new settings with TCSANOW and VMIN=1, VTIME=100
    sys.stdout.write("\x1B[" + str(new_settings[2]) + "A")
except OSError as e:
    print(f"Error: {e}")
```

**Example Use Cases**
--------------------

*   Set terminal speed to 9600 baud and 8 bits per character.
*   Set the minimum number of bytes required for input to 1.
*   Set the time in hundredths of a second to wait for input to 100.

```python
# Example usage:
try:
    # Create a copy of the current terminal settings
    new_settings = termios.tcgetattr(sys.stdout)

    # Modify the settings as needed
    new_settings[5] = termios.B9600 | termios.CLOCAL | termios.CREAD
    new_settings[6] = 0x1f80

    # Apply the new settings with TCSANOW and VMIN=1, VTIME=100
except OSError as e:
    print(f"Error: {e}")
```

**Best Practices**
------------------

*   Always handle exceptions when working with terminal settings.
*   Use the `tcgetattr()` function to get a copy of the current terminal settings before modifying them.
*   Use special values such as `TCSANOW` and `TCFLUSH` to apply changes immediately or flush the output buffer, respectively.

```python
# Best practice:
try:
    # Get a copy of the current terminal settings
    new_settings = termios.tcgetattr(sys.stdout)

    # Modify the settings as needed
    new_settings[5] = termios.B9600 | termios.CLOCAL | termios.CREAD

    # Apply the new setting immediately with TCSANOW
except OSError as e:
    print(f"Error: {e}")
```

```python
# Best practice for flushing output buffer:
try:
    # Get a copy of the current terminal settings
    new_settings = termios.tcgetattr(sys.stdout)

    # Modify the settings as needed
    new_settings[5] = termios.B9600 | termios.CLOCAL | termios.CREAD

    # Apply the new setting immediately with TCSFLUSH and flush output buffer
except OSError as e:
    print(f"Error: {e}")
```

```python
# Best practice for waiting for input:
try:
    # Get a copy of the current terminal settings
    new_settings = termios.tcgetattr(sys.stdout)

    # Modify the settings as needed
    new_settings[5] = termios.B9600 | termios.CLOCAL | termios.CREAD

    # Apply the new setting with VTIME=100 and wait for input
except OSError as e:
    print(f"Error: {e}")
```
