# termios - POSIX style tty control
## Table of Contents

1. [Example 1: Setting Terminal Modes](#example-1-setting-terminal-modes)
2. [Example 2: Changing Line Discipline](#example-2-changing-line-discipline)
3. [Example 3: Reading and Writing Terminal Input](#example-3-reading-and-writing-terminal-input)
4. [Example 4: Querying Terminal Attributes](#example-4-querying-terminal-attributes)
5. [Example 5: Setting Special Character Sets](#example-5-setting-special-character-sets)
6. [Example 6: Changing Input Modes](#example-6-changing-input-modes)



The `termios` module in Python provides a way to manipulate terminal-related information, such as input modes, output modes, line discipline settings, and more. This module allows you to interact directly with terminal devices using the POSIX interface.

Here are some comprehensive code examples that demonstrate various functionalities of the `termios` module:

### Example 1: Setting Terminal Modes

This example shows how to set the terminal modes for raw input, disabling echo, and turning off canonical mode (which is typically enabled by default in interactive shells).

```python
import termios
import tty
import sys

def set_raw_mode(fd):
    """Set the terminal into raw mode."""
    try:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        new_settings = old_settings.copy()

        # Disable canonical mode and echo
        new_settings[0] &= ~(termios.IGNBRK | termios.BRKINT | termios.PARMRK |
                                termios.ISTRIP | termios.INLCR | termios. IGNCR |
                                termios.ICRNL | termios.IMAXBEL)
        new_settings[1] &= ~termios.ECHO
        new_settings[2] &= ~(termios.OPOST)

        termios.tcsetattr(fd, termios.TCSANOW, new_settings)
    except Exception as e:
        print(f"Error setting raw mode: {e}")

def main():
    try:
        set_raw_mode(sys.stdin.fileno())
        print("Terminal set to raw mode. Press any key to exit.")

        # Read a character
        input_char = sys.stdin.read(1)
        print(f"You pressed: {input_char}")
    finally:
        # Restore the original terminal settings
        termios.tcsetattr(sys.stdin.fileno(), termios.TCSANOW, termios.tcgetattr(sys.stdin.fileno()))

if __name__ == "__main__":
    main()
```

### Example 2: Changing Line Discipline

This example demonstrates how to change the line discipline of a terminal. For instance, you can set it to `NLDISC_MINIMAL` which is useful for terminals that do not require any special handling of newlines.

```python
import termios
import tty
import sys

def set_line_discipline(fd, discipline):
    """Set the terminal's line discipline."""
    try:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        new_settings = old_settings.copy()

        # Set the line discipline
        new_settings[6] = discipline

        termios.tcsetattr(fd, termios.TCSANOW, new_settings)
    except Exception as e:
        print(f"Error setting line discipline: {e}")

def main():
    try:
        set_line_discipline(sys.stdin.fileno(), termios.NLDISC_MINIMAL)
        print("Line discipline set to MINIMAL.")
    finally:
        # Restore the original terminal settings
        termios.tcsetattr(sys.stdin.fileno(), termios.TCSANOW, termios.tcgetattr(sys.stdin.fileno()))

if __name__ == "__main__":
    main()
```

### Example 3: Reading and Writing Terminal Input

This example shows how to read input from a terminal in raw mode and write output back to it.

```python
import termios
import tty
import sys

def set_raw_mode(fd):
    """Set the terminal into raw mode."""
    try:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        new_settings = old_settings.copy()

        # Disable canonical mode and echo
        new_settings[0] &= ~(termios.IGNBRK | termios.BRKINT | termios.PARMRK |
                                termios.ISTRIP | termios.INLCR | termios. IGNCR |
                                termios.ICRNL | termios.IMAXBEL)
        new_settings[1] &= ~termios.ECHO
        new_settings[2] &= ~(termios.OPOST)

        termios.tcsetattr(fd, termios.TCSANOW, new_settings)
    except Exception as e:
        print(f"Error setting raw mode: {e}")

def main():
    try:
        set_raw_mode(sys.stdin.fileno())
        print("Terminal set to raw mode. Press a key followed by 'Enter'.")

        # Read input
        input_line = sys.stdin.readline().strip()
        print(f"You entered: {input_line}")
    finally:
        # Restore the original terminal settings
        termios.tcsetattr(sys.stdin.fileno(), termios.TCSANOW, termios.tcgetattr(sys.stdin.fileno()))

if __name__ == "__main__":
    main()
```

### Example 4: Querying Terminal Attributes

This example shows how to query and print various attributes of the terminal.

```python
import termios
import sys

def get_terminal_attributes(fd):
    """Retrieve and print terminal attributes."""
    try:
        fd = sys.stdin.fileno()
        settings = termios.tcgetattr(fd)

        # Print input modes
        print(f"Input Modes: {settings[0]}")

        # Print output modes
        print(f"Output Modes: {settings[1]}")

        # Print local flags
        print(f"Local Flags: {settings[2]}")

        # Print control characters
        print(f"Control Characters: {settings[3]}")

        # Print special character sets
        print(f"Special Character Sets: {settings[4]}")

        # Print current line discipline
        print(f"Current Line Discipline: {settings[5]}")
    except Exception as e:
        print(f"Error querying terminal attributes: {e}")

def main():
    try:
        get_terminal_attributes(sys.stdin.fileno())
    finally:
        pass

if __name__ == "__main__":
    main()
```

### Example 5: Setting Special Character Sets

This example demonstrates how to set special character sets in the terminal, which can be useful for configuring certain types of terminals or emulators.

```python
import termios
import tty
import sys

def set_special_character_sets(fd):
    """Set special character sets."""
    try:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        new_settings = old_settings.copy()

        # Set a specific special character set (e.g., ASCII 0x81 for IBM PC compatibility)
        new_settings[4] = bytearray([2])  # Byte to represent the special character set

        termios.tcsetattr(fd, termios.TCSANOW, new_settings)
    except Exception as e:
        print(f"Error setting special character sets: {e}")

def main():
    try:
        set_special_character_sets(sys.stdin.fileno())
        print("Special character sets set.")
    finally:
        # Restore the original terminal settings
        termios.tcsetattr(sys.stdin.fileno(), termios.TCSANOW, termios.tcgetattr(sys.stdin.fileno()))

if __name__ == "__main__":
    main()
```

### Example 6: Changing Input Modes

This example shows how to change the input modes of the terminal. For instance, you can disable canonical mode and enable canonical mode.

```python
import termios
import tty
import sys

def set_input_mode(fd, mode):
    """Set the terminal's input mode."""
    try:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        new_settings = old_settings.copy()

        # Set the input mode
        new_settings[0] |= mode  # Enable or disable canonical mode

        termios.tcsetattr(fd, termios.TCSANOW, new_settings)
    except Exception as e:
        print(f"Error setting input mode: {e}")

def main():
    try:
        set_input_mode(sys.stdin.fileno(), termios.ICANON)  # Enable canonical mode
        print("Input mode set to CANON.")
    finally:
        # Restore the original terminal settings
        termios.tcsetattr(sys.stdin.fileno(), termios.TCSANOW, termios.tcgetattr(sys.stdin.fileno()))

if __name__ == "__main__":
    main()
```

These examples cover a range of functionalities in the `termios` module, from setting basic terminal modes to querying and modifying various aspects of terminal attributes. Each example is designed to be clear and self-contained, providing a practical demonstration of how to use the `termios` module for controlling terminal behavior in Python applications.
