# msvcrt — Useful routines from the MS VC++ runtime

Here are some example code snippets for the `msvcrt` module:

```python
# Importing the msvcrt module
import msvcrt

# 1. Getting the current cursor position
def get_cursor_position():
    # Use the caret positioning function to get the current cursor position
    x, y = msvcrt.getyx()
    return (x, y)

print(get_cursor_position())

# 2. Handling keyboard input
def handle_keyboard_input():
    # Use a loop to continuously read from standard input until Ctrl+Z is pressed
    while True:
        try:
            key = msvcrt.getche().decode('utf-8')
            print(f"Key pressed: {key}")
        except EOFError:
            break

handle_keyboard_input()

# 3. Getting the current cursor position using getyx() function
def get_cursor_position_yx():
    # Use the caret positioning function to get the current cursor position
    x, y = msvcrt.getyx()
    return f"Cursor Position (X, Y): ({x}, {y})"

print(get_cursor_position_yx())

# 4. Getting the terminal size
def get_terminal_size():
    # Use the cbreak() function to disable line buffering and ensure that the program receives the correct character count from the read() method
    msvcrt.cbreak()
    # Get the terminal size using the getyx() function
    x, y = msvcrt.getyx()
    # Return the terminal size as a tuple (width, height)
    return (x, y)

print(get_terminal_size())

# 5. Disabling cbreak mode
def disable_cbreak_mode():
    # Use the nodelay() function to enable line buffering and set the read timeout to -1
    msvcrt.nodelay(0, True)  # Set timeout to 0 seconds

disable_cbreak_mode()
```

These examples demonstrate various functions provided by the `msvcrt` module in Python, including handling keyboard input, getting cursor positions, terminal size, and more.
