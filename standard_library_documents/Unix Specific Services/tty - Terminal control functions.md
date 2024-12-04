# tty - Terminal control functions

The `tty` module in Python provides a way to interact with terminal devices, allowing you to configure the input/output modes of a terminal. Here are comprehensive and well-documented examples of how to use each function available in this module:

### 1. `tty.iflag`
- **Description**: Controls input processing flags.
- **Functionality**: Sets or gets the input mode flags for a given file descriptor.

```python
import tty

# Open a terminal device
with open('/dev/tty', 'r+') as fd:
    # Get current iflag settings
    old_iflag = tty.tcgetattr(fd)
    
    # Modify iflag settings
    new_iflag = old_iflag[:]
    new_iflag[tty.VMIN] = 1  # Minimum number of characters to read
    new_iflag[tty.VTIME] = 0   # Time out in deciseconds
    
    # Apply modified iflag settings
    tty.tcsetattr(fd, tty.TCSANOW, new_iflag)
    
    try:
        while True:
            # Read data with the new input mode settings
            data = fd.read(1)
            print(data, end='', flush=True)
    finally:
        # Restore original iflag settings
        tty.tcsetattr(fd, tty.TCSANOW, old_iflag)

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

# Open a terminal device
with open('/dev/tty', 'r+') as fd:
    # Get current cflag settings
    old_cflag = tty.tcgetattr(fd)
    
    # Modify cflag settings
    new_cflag = old_cflag[:]
    new_cflag[tty.CSIZE] = tty.B8  # Set character size to 8 bits
    
    # Apply modified cflag settings
    tty.tcsetattr(fd, tty.TCSANOW, new_cflag)
    
    try:
        while True:
            # Read data with the new control mode settings
            data = fd.read(1)
            print(data, end='', flush=True)
    finally:
        # Restore original cflag settings
        tty.tcsetattr(fd, tty.TCSANOW, old_cflag)

```

### 4. `tty.lflag`
- **Description**: Controls local flags.
- **Functionality**: Sets or gets the local mode flags for a given file descriptor.

```python
import tty

# Open a terminal device
with open('/dev/tty', 'r+') as fd:
    # Get current lflag settings
    old_lflag = tty.tcgetattr(fd)
    
    # Modify lflag settings
    new_lflag = old_lflag[:]
    new_lflag[tty.ICANON] = False  # Disable canonical mode
    
    # Apply modified lflag settings
    tty.tcsetattr(fd, tty.TCSANOW, new_lflag)
    
    try:
        while True:
            # Read data with the new local mode settings
            data = fd.read(1)
            print(data, end='', flush=True)
    finally:
        # Restore original lflag settings
        tty.tcsetattr(fd, tty.TCSANOW, old_lflag)

```

### 5. `tty.isatty`
- **Description**: Checks if a file descriptor is associated with a terminal device.
- **Functionality**: Determines whether the specified file descriptor corresponds to a terminal.

```python
import tty

# Open a terminal device
fd = open('/dev/tty', 'r+')

try:
    # Check if the file descriptor is a terminal
    if tty.isatty(fd.fileno()):
        print("The file descriptor is associated with a terminal.")
    else:
        print("The file descriptor is not associated with a terminal.")
finally:
    fd.close()
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
    
    # Modify the input mode flags
    new_iflag = old_attrs[:]
    new_iflag[tty.VMIN] = 1
    new_iflag[tty.VTIME] = 0
    
    # Set the modified attributes
    tty.tcsetattr(fd, tty.TCSANOW, new_iflag)
    
    print("New Input Mode Flags:", new_iflag)

```

### 8. `tty.cbreak`
- **Description**: Enters cbreak mode.
- **Functionality**: Disables canonical and echo modes.

```python
import tty

# Open a terminal device
with open('/dev/tty', 'r+') as fd:
    # Enter cbreak mode
    tty.cbreak(fd)
    
    try:
        while True:
            # Read data in cbreak mode
            data = fd.read(1)
            print(data, end='', flush=True)
    finally:
        # Exit cbreak mode
        tty.raw(fd)

```

### 9. `tty.raw`
- **Description**: Enters raw mode.
- **Functionality**: Disables canonical, echo, and other input processing modes.

```python
import tty

# Open a terminal device
with open('/dev/tty', 'r+') as fd:
    # Enter raw mode
    tty.raw(fd)
    
    try:
        while True:
            # Read data in raw mode
            data = fd.read(1)
            print(data, end='', flush=True)
    finally:
        # Exit raw mode
        tty.cbreak(fd)

```

### 10. `tty.setraw`
- **Description**: Sets the terminal to raw mode.
- **Functionality**: Modifies the input, output, and control mode flags for raw mode.

```python
import tty

# Open a terminal device
with open('/dev/tty', 'r+') as fd:
    # Set the terminal to raw mode
    old_attrs = tty.tcgetattr(fd)
    new_iflag = old_attrs[:]
    new_iflag[tty.ICANON] = False
    new_iflag[tty.ECHO] = False
    tty.tcsetattr(fd, tty.TCSANOW, new_iflag)

try:
    while True:
        # Read data in raw mode
        data = fd.read(1)
        print(data, end='', flush=True)
finally:
    # Restore original attributes
    tty.tcsetattr(fd, tty.TCSANOW, old_attrs)
```

### 11. `tty.reset`
- **Description**: Resets the terminal to a default state.
- **Functionality**: Restores all input, output, and control mode flags to their default values.

```python
import tty

# Open a terminal device
with open('/dev/tty', 'r+') as fd:
    # Reset the terminal to a default state
    old_attrs = tty.tcgetattr(fd)
    new_iflag = old_attrs[:]
    new_iflag[tty.ICANON] = True
    new_iflag[tty.ECHO] = True
    tty.tcsetattr(fd, tty.TCSANOW, new_iflag)

try:
    while True:
        # Read data in default state
        data = fd.read(1)
        print(data, end='', flush=True)
finally:
    # Restore original attributes
    tty.tcsetattr(fd, tty.TCSANOW, old_attrs)
```

These examples demonstrate various functionalities of the `tty` module, including setting and modifying input/output modes, checking if a file descriptor is associated with a terminal, and resetting the terminal to its default state. Each example includes comments for clarity and ensures that the terminal attributes are restored after operations are completed. Additionally, examples are provided to handle both cbreak and raw mode using `tty.cbreak()` and `tty.raw()`.
