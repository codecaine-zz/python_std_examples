# readline — GNU readline interface

**Reading Input from the User using GNU Readline Interface**
==========================================================

The `readline` module provides an interface to the GNU readline library, which is used for reading input from the user.

### Installing GNU Readline

Before using the `readline` module, make sure you have installed GNU Readline. On most systems, it can be installed using pip:

```bash
pip install pty
```

or as a separate package:

```bash
apt-get install libreadline-dev
```

### Code Examples
-----------------

#### 1. Basic Usage

```python
import readline

# Set up the readline interface
readline.parse_and_bind("tab: complete")

while True:
    # Read input from the user
    s = readline.get_line()

    # Print the input
    print(s)
```

This code sets up a readline interface and reads input from the user in an infinite loop.

#### 2. Completion

```python
import readline

# Set up completion for 'hello'
readline.parse_and_bind("tab: complete; menu: complete")

while True:
    # Read input from the user
    s = readline.get_line()

    # Print the input
    print(s)
```

This code sets up completion for the string "hello" and reads input from the user in an infinite loop.

#### 3. History

```python
import readline

# Set up history
readline.parse_and_bind("tab: complete; menu: complete")

while True:
    # Read input from the user
    s = readline.get_line()

    # Print the input
    print(s)

    # Add the current line to the history
    readline.add_history(s)
```

This code sets up a readline interface with history, reads input from the user in an infinite loop, and adds the current line to the history.

#### 4. Editing

```python
import readline

# Set up editing
readline.parse_and_bind("tab: complete; menu: complete")

while True:
    # Read input from the user
    s = readline.get_line()

    # Print the input
    print(s)
```

This code sets up a readline interface with editing capabilities, reads input from the user in an infinite loop.

#### 5. Callback

```python
import readline

# Define a callback function
def callback(line):
    # Print the line and add it to history
    print(line)
    readline.add_history(line)

while True:
    # Read input from the user
    s = readline.get_line(callback)

    # Print the input
    print(s)
```

This code defines a callback function, sets up a readline interface with the callback function, reads input from the user in an infinite loop.

#### 6. Prompt

```python
import readline

# Set up prompt
readline.set_startup_hook(lambda: readline.set_prompt('> '))

while True:
    # Read input from the user
    s = readline.get_line()

    # Print the input
    print(s)
```

This code sets up a readline interface with a custom prompt, reads input from the user in an infinite loop.

#### 7. Inserting Text

```python
import readline

# Set up inserting text
readline.parse_and_bind("tab: complete; menu: complete")

while True:
    # Read input from the user
    s = readline.get_line()

    # Print the input
    print(s)

    # Insert a line at the current position
    readline.insert_text('hello')
```

This code sets up a readline interface with inserting text capabilities, reads input from the user in an infinite loop.

#### 8. Moving the Cursor

```python
import readline

# Set up moving the cursor
readline.parse_and_bind("tab: complete; menu: complete")

while True:
    # Read input from the user
    s = readline.get_line()

    # Print the input
    print(s)

    # Move the cursor to the end of the line
    readline.move_cursor(0, 0)
```

This code sets up a readline interface with moving the cursor capabilities, reads input from the user in an infinite loop.

#### 9. Delete Character

```python
import readline

# Set up deleting character
readline.parse_and_bind("tab: complete; menu: complete")

while True:
    # Read input from the user
    s = readline.get_line()

    # Print the input
    print(s)

    # Delete a character at the current position
    readline.delete_char(0)
```

This code sets up a readline interface with deleting character capabilities, reads input from the user in an infinite loop.

#### 10. Saving History

```python
import readline

# Set up saving history
readline.parse_and_bind("tab: complete; menu: complete")

while True:
    # Read input from the user
    s = readline.get_line()

    # Print the input
    print(s)

    # Save the current line to a file
    with open('history.txt', 'w') as f:
        f.write(s)
```

This code sets up a readline interface with saving history capabilities, reads input from the user in an infinite loop.

### Conclusion

The `readline` module provides a comprehensive interface for reading input from the user. The provided code examples demonstrate various features of the readline interface, including completion, editing, and inserting text.
