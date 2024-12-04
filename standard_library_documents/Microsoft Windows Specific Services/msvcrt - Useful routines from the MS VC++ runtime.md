# msvcrt - Useful routines from the MS VC++ runtime

The `msvcrt` module is a part of the Python Standard Library that provides access to some low-level functions similar to those found in Microsoft's Visual C++ runtime. This module is primarily used for applications that need to interact directly with the operating system, particularly when dealing with console input and output.

Below are comprehensive code examples for each function available in the `msvcrt` module:

```python
import msvcrt

# Function: getch()
# Description: Waits for a single character from the keyboard.
# Returns: A byte string containing the pressed key.

def example_getch():
    """
    Example of using getch() to read a single character from the console.
    """
    print("Press any key followed by Enter:")
    char = msvcrt.getch()
    print(f"You pressed: {char}")

example_getch()

# Function: kbhit()
# Description: Checks if a keyboard input has been received without blocking.
# Returns: True if a key is available, False otherwise.

def example_kbhit():
    """
    Example of using kbhit() to check for keyboard input before reading it.
    """
    print("Press Enter to continue...")
    while not msvcrt.kbhit():
        pass
    msvcrt.getch()
    print("Key detected!")

example_kbhit()

# Function: putch()
# Description: Sends a single character to the console output buffer.

def example_putch():
    """
    Example of using putch() to write a single character to the console.
    """
    print("Example of using putch() to print a character.")
    msvcrt.putch(b'A')
    print('A has been printed to the console.')

example_putch()

# Function: openfilecon()
# Description: Opens a file connection to the console device.

def example_openfilecon():
    """
    Example of using openfilecon() to open a file handle for the console.
    """
    import os
    print("Opening a file connection to the console...")
    fh = msvcrt.openfilecon('CONOUT$')
    print(f"File handle: {fh}")

example_openfilecon()

# Function: lseek()
# Description: Moves the current position in a file.

def example_lseek():
    """
    Example of using lseek() to move the cursor position in the console.
    """
    import os
    print("Moving the cursor position...")
    fh = msvcrt.openfilecon('CONOUT$')
    offset, whence = 5, 0  # Move by 5 bytes from the start of the file
    new_position = os.lseek(fh.fileno(), offset, whence)
    print(f"Cursor position moved to: {new_position}")

example_lseek()

# Function: getconioerror()
# Description: Retrieves the last error code associated with console input.

def example_getconioerror():
    """
    Example of using getconioerror() to retrieve and display the last error code.
    """
    print("Getting the last error code...")
    err_code = msvcrt.getconioerror()
    print(f"Last error code: {err_code}")

example_getconioerror()

# Function: setmode()
# Description: Sets the mode of a file descriptor to binary or text.

def example_setmode():
    """
    Example of using setmode() to change the mode of the console file handle.
    """
    import os
    print("Changing the mode of the console...")
    fh = msvcrt.openfilecon('CONOUT$')
    # Set the mode to text (default)
    os.setmode(fh.fileno(), os.O_TEXT)
    print(f"Mode set to: {os.getmode(fh.fileno())}")

example_setmode()

# Function: ctrlchandler()
# Description: Sets a handler for Ctrl+C input.

def example_ctrlchandler(handler):
    """
    Example of using ctrlchandler() to set a custom control C handler.
    """
    def my_handler(signum, frame):
        print("Ctrl+C has been detected!")
        return True

    original_handler = msvcrt.ctrlchandler(my_handler)
    try:
        while True:
            pass
    finally:
        # Restore the original handler
        msvcrt.ctrlchandler(original_handler)

example_ctrlchandler(msvcrt.CTRL_C_EVENT)
```

### Explanation:

1. **`getch()`**: This function waits for a single character from the keyboard and returns it as a byte string.

2. **`kbhit()`**: Checks if there is any input waiting to be read from the console without blocking.

3. **`putch()`**: Sends a single character to the console output buffer, which is useful for quick console updates.

4. **`openfilecon()`**: Opens a file connection to the console device using `os.open()` and returns a file handle.

5. **`lseek()`**: Moves the current position in the console by adjusting the cursor position using `os.lseek()`.

6. **`getconioerror()`**: Retrieves and prints the last error code associated with console input, which can be useful for debugging issues related to reading from the console.

7. **`setmode()`**: Changes the mode of the console file handle to either binary or text using `os.setmode()`, which is particularly important for handling newline characters in text mode.

8. **`ctrlchandler()`**: Sets a handler function for Ctrl+C input, allowing you to define custom behavior when Ctrl+C is detected.

These examples provide a comprehensive overview of how to use each function in the `msvcrt` module, covering common console I/O operations and error handling.
