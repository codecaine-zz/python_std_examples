# tty - Terminal control functions
## Table of Contents

1. [1. `tty.iflag`](#1-ttyiflag)
2. [2. `tty.oflag`](#2-ttyoflag)
3. [3. `tty.cflag`](#3-ttycflag)
4. [4. `tty.lflag`](#4-ttylflag)
5. [5. `tty.isatty`](#5-ttyisatty)
6. [6. `tty.getattr`](#6-ttygetattr)
7. [7. `tty.setattr`](#7-ttysetattr)
8. [8. `tty.cbreak`](#8-ttycbreak)
9. [9. `tty.raw`](#9-ttyraw)
10. [10. `tty.setraw`](#10-ttysetraw)



The `tty` module in Python provides a way to interact with terminal devices, allowing you to configure the input/output modes of a terminal. Here are comprehensive and well-documented examples of how to use each function available in this module:

### 1. `tty.iflag`
- **Description**: Controls input processing flags.
- **Functionality**: Sets or gets the input mode flags for a given file descriptor.

```python
import tty
import termios

# Open a terminal device
with open('/dev/tty', 'r+') as fd:
    # Get current termios settings
    old_attrs = termios.tcgetattr(fd)
    
    # Modify termios settings
    new_attrs = old_attrs[:]
    new_attrs[6][termios.VMIN] = 1  # Minimum number of characters to read
    new_attrs[6][termios.VTIME] = 0  # Time out in deciseconds
    
    # Apply modified termios settings
    termios.tcsetattr(fd, termios.TCSANOW, new_attrs)
    
    try:
        while True:
            # Read data with the new input mode settings
            data = fd.read(1)
            print(data, end='', flush=True)
    finally:
        # Restore original termios settings
        termios.tcsetattr(fd, termios.TCSANOW, old_attrs)


```

### 2. `tty.oflag`
- **Description**: Controls output processing flags.
- **Functionality**: Sets or gets the output mode flags for a given file descriptor.

```python
import tty

# Open a terminal device
with open('/dev/tty', 'r+') as fd:
    # Get current oflag settings
    old_oflag = tty.tcgetattr(fd)
    
    # Modify oflag settings
    new_oflag = old_oflag[:]
    new_oflag[tty.ONLCR] = False  # Disable newline translation
    
    # Apply modified oflag settings
    tty.tcsetattr(fd, tty.TCSANOW, new_oflag)
    
    try:
        while True:
            # Write data with the new output mode settings
            fd.write('Hello, World!\n')
    finally:
        # Restore original oflag settings
        tty.tcsetattr(fd, tty.TCSANOW, old_oflag)
```

### 3. `tty.cflag`
- **Description**: Controls control flags.
- **Functionality**: Sets or gets the control mode flags for a given file descriptor.

```python
import tty
import termios

# Open a terminal device
with open('/dev/tty', 'r+') as fd:
    # Get current termios settings
    old_attrs = termios.tcgetattr(fd)
    
    # Modify termios settings
    new_attrs = old_attrs[:]
    new_attrs[2] &= ~termios.CSIZE  # Clear current character size mask
    new_attrs[2] |= termios.CS8     # Set character size to 8 bits
    
    # Apply modified termios settings
    termios.tcsetattr(fd, termios.TCSANOW, new_attrs)
    
    try:
        while True:
            # Read data with the new control mode settings
            data = fd.read(1)
            print(data, end='', flush=True)
    finally:
        # Restore original termios settings
        termios.tcsetattr(fd, termios.TCSANOW, old_attrs)
```

### 4. `tty.lflag`
- **Description**: Controls local flags.
- **Functionality**: Sets or gets the local mode flags for a given file descriptor.

```python
import tty
import termios

# Open a terminal device
with open('/dev/tty', 'r+') as fd:
    # Get current lflag settings
    old_attrs = termios.tcgetattr(fd)
    
    # Modify lflag settings
    new_attrs = old_attrs[:]
    new_attrs[3] &= ~termios.ICANON  # Disable canonical mode
    
    # Apply modified lflag settings
    termios.tcsetattr(fd, termios.TCSANOW, new_attrs)
    
    try:
        while True:
            # Read data with the new local mode settings
            data = fd.read(1)
            print(data, end='', flush=True)
    finally:
        # Restore original lflag settings
        termios.tcsetattr(fd, termios.TCSANOW, old_attrs)
```

### 5. `tty.isatty`
- **Description**: Checks if a file descriptor is associated with a terminal device.
- **Functionality**: Determines whether the specified file descriptor corresponds to a terminal.

```python
import tty
import termios
import sys

# Open a terminal device
with open('/dev/tty', 'rb+') as fd:
    # Get current lflag settings
    old_attrs = termios.tcgetattr(fd)
    
    # Modify lflag settings
    new_attrs = old_attrs[:]
    new_attrs[3] &= ~termios.ICANON  # Disable canonical mode
    
    # Apply modified lflag settings
    termios.tcsetattr(fd, termios.TCSANOW, new_attrs)
    
    try:
        while True:
            # Read data with the new local mode settings
            data = sys.stdin.read(1)
            print(data, end='', flush=True)
    finally:
        # Restore original lflag settings
        termios.tcsetattr(fd, termios.TCSANOW, old_attrs)
```

### 6. `tty.getattr`
- **Description**: Retrieves the current attributes of a given file descriptor.
- **Functionality**: Returns a tuple containing the input, output, and control mode flags.

```python
import tty

# Open a terminal device
with open('/dev/tty', 'r+') as fd:
    # Retrieve the current attributes
    attrs = tty.tcgetattr(fd)
    
    print("Input Mode Flags:", attrs[tty.IFLAG])
    print("Output Mode Flags:", attrs[tty.OFLAG])
    print("Control Mode Flags:", attrs[tty.CFLAG])
    print("Local Mode Flags:", attrs[tty.LFLAG])

```

### 7. `tty.setattr`
- **Description**: Sets the attributes of a given file descriptor.
- **Functionality**: Modifies the input, output, and control mode flags for a terminal device.

```python
import tty

# Open a terminal device
with open('/dev/tty', 'r+') as fd:
    # Get current attributes
    old_attrs = tty.tcgetattr(fd)
    
    # Copy the entire old_attrs list to new_attrs
    new_attrs = old_attrs[:]
    
    # Modify the input mode flags (first element of the list)
    new_iflag = new_attrs[0]
    new_iflag |= tty.VMIN
    new_iflag |= tty.VTIME
    
    # Update the first element of new_attrs
    new_attrs[0] = new_iflag
    
    # Set the modified attributes
    tty.tcsetattr(fd, tty.TCSANOW, new_attrs)
    
    print("New Input Mode Flags:", new_iflag)
```

### 8. `tty.cbreak`
- **Description**: Enters cbreak mode.
- **Functionality**: Disables canonical and echo modes.

```python
import tty
import termios

# Open a terminal device
with open('/dev/tty', 'r+') as fd:
    # Save the original terminal settings
    original_settings = termios.tcgetattr(fd)
    
    # Enter cbreak mode
    tty.setcbreak(fd)
    
    try:
        while True:
            # Read data in cbreak mode
            data = fd.read(1)
            print(data, end='', flush=True)
    finally:
        # Restore the original terminal settings
        termios.tcsetattr(fd, termios.TCSADRAIN, original_settings)
```

### 9. `tty.raw`
- **Description**: Enters raw mode.
- **Functionality**: Disables canonical, echo, and other input processing modes.

```python
import tty
import termios

# Open a terminal device
with open('/dev/tty', 'r+') as fd:
    # Save the original terminal settings
    original_settings = termios.tcgetattr(fd)
    
    # Enter raw mode
    tty.setraw(fd)
    
    try:
        while True:
            # Read data in raw mode
            data = fd.read(1)
            print(data, end='', flush=True)
    finally:
        # Restore the original terminal settings
        termios.tcsetattr(fd, termios.TCSADRAIN, original_settings)
```

### 10. `tty.setraw`
- **Description**: Sets the terminal to raw mode.
- **Functionality**: Modifies the input, output, and control mode flags for raw mode.

```python
import tty
import termios
import sys

# Open a terminal device
with open('/dev/tty', 'r+') as fd:
    # Set the terminal to raw mode
    old_attrs = termios.tcgetattr(fd)
    new_attrs = termios.tcgetattr(fd)
    new_attrs[3] = new_attrs[3] & ~(termios.ICANON | termios.ECHO)
    termios.tcsetattr(fd, termios.TCSANOW, new_attrs)

    try:
        while True:
            # Read data in raw mode
            data = fd.read(1)
            print(data, end='', flush=True)
    finally:
        # Restore original attributes
        termios.tcsetattr(fd, termios.TCSANOW, old_attrs)
```

### 11. `tty.reset`
- **Description**: Resets the terminal to a default state.
- **Functionality**: Restores all input, output, and control mode flags to their default values.

```python
import tty
import termios

# Open a terminal device
with open('/dev/tty', 'r+') as fd:
    # Reset the terminal to a default state
    old_attrs = termios.tcgetattr(fd)
    new_attrs = old_attrs[:]
    new_attrs[tty.LFLAG] |= (termios.ICANON | termios.ECHO)
    termios.tcsetattr(fd, termios.TCSANOW, new_attrs)

    try:
        while True:
            # Read data in default state
            data = fd.read(1)
            print(data, end='', flush=True)
    finally:
        # Restore original attributes
        termios.tcsetattr(fd, termios.TCSANOW, old_attrs)
```

These examples demonstrate various functionalities of the `tty` module, including setting and modifying input/output modes, checking if a file descriptor is associated with a terminal, and resetting the terminal to its default state. Each example includes comments for clarity and ensures that the terminal attributes are restored after operations are completed. Additionally, examples are provided to handle both cbreak and raw mode using `tty.cbreak()` and `tty.raw()`.
