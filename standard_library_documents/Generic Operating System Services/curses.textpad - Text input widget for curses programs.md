# curses.textpad - Text input widget for curses programs

The `curses` module in Python is a powerful library for creating text-based user interfaces, which can be used to build console applications that offer interactive functionality. The `textpad` sub-module provides several classes and functions to create text input widgets that are useful in such applications.

Below are comprehensive code examples for each of the functionalities provided by the `curses.textpad` module:

### 1. Creating a Simple Text Input Widget

```python
import curses
from curses import textpad

def main(stdscr):
    # Clear and refresh the screen to ensure that previous output doesn't remain
    stdscr.clear()
    stdscr.refresh()

    # Create a window for the input field
    height, width = 5, 20
    win = curses.newwin(height, width, 1, 1)
    win.keypad(True)  # Enable keypad

    # Set up text attributes
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)

    # Initialize the input field with some initial text
    message = "Enter your text:"
    input_win = textpad.Textbox(win, max_input=20)
    win.addstr(0, 0, message, curses.color_pair(1))
    win.refresh()

    # Capture user input
    user_input = input_win.edit()
    if user_input:
        win.addstr(height - 1, 1, "You entered: " + user_input)

    # End the session and clean up
    stdscr.keypad(False)
    curses.endwin()

if __name__ == "__main__":
    curses.wrapper(main)
```

### Explanation:

- **Initialization**: The `curses.wrapper` function is used to initialize and wrap the main function, handling terminal cleanup for you.
- **Window Creation**: A new window is created with a specified height and width. The keypad is enabled to capture arrow keys and other special keys.
- **Text Attributes**: Colors are defined using `curses.init_pair`.
- **Textbox Creation**: The `textpad.Textbox` class is used to create the input widget. It takes the window, maximum input length, and any additional options as arguments.
- **User Input**: The `edit()` method of the textbox waits for user input until a newline character is entered.
- **Cleanup**: The keypad is disabled and the terminal is cleaned up using `curses.endwin()`.

### 2. Adding Multiple Lines to the Text Input Widget

```python
import curses
from curses import textpad

def main(stdscr):
    # Clear and refresh the screen
    stdscr.clear()
    stdscr.refresh()

    # Create a window for the input field
    height, width = 10, 30
    win = curses.newwin(height, width, 1, 1)
    win.keypad(True)

    # Set up text attributes
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)

    # Initialize a list to store messages and their corresponding edit positions
    messages = ["Enter your first line:", "Enter your second line:"]
    lines = []
    max_input_length = 20

    for i, message in enumerate(messages):
        # Add the message to the window
        win.addstr(i + 1, 0, message, curses.color_pair(1))
        # Create a textbox for each line and append it to the list
        lines.append(textpad.Textbox(win, max_input_length=max_input_length))

    # Refresh the window to display the messages
    win.refresh()

    # Capture user input for each line
    for i in range(len(messages)):
        lines[i].edit()
        if lines[i].value():
            win.addstr(i + 2, 1, "Line {}: {}".format(i + 1, lines[i].value()))

    # End the session and clean up
    stdscr.keypad(False)
    curses.endwin()

if __name__ == "__main__":
    curses.wrapper(main)
```

### Explanation:

- **Multiple Lines**: A list of messages is created, and for each message, a textbox is added to the window.
- **User Input**: The `edit()` method captures input for each textbox.
- **Displaying Results**: After capturing input from all textboxes, their contents are displayed in the next row below each input field.

### 3. Handling Key Events

```python
import curses
from curses import textpad

def main(stdscr):
    # Clear and refresh the screen
    stdscr.clear()
    stdscr.refresh()

    # Create a window for the input field
    height, width = 6, 15
    win = curses.newwin(height, width, 1, 1)
    win.keypad(True)

    # Set up text attributes
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    # Initialize a textbox for user input
    message = "Enter some text:"
    input_win = textpad.Textbox(win, max_input_length=15)
    win.addstr(0, 0, message, curses.color_pair(1))
    win.refresh()

    # Capture user input
    user_input = input_win.edit()
    if user_input:
        win.addstr(height - 2, 1, "You entered: " + user_input)

    # Handle key events
    while True:
        key = stdscr.getch()
        if key == ord('q'):
            break
        elif key == curses.KEY_UP:
            win.addstr(0, 0, message, curses.color_pair(2))
            win.refresh()

    # End the session and clean up
    stdscr.keypad(False)
    curses.endwin()

if __name__ == "__main__":
    curses.wrapper(main)
```

### Explanation:

- **Key Events**: The `getch()` method is used to capture key events. In this example, pressing 'q' exits the program, and pressing the up arrow changes the text color.
- **Conditional Logic**: A while loop checks for specific key presses and modifies the display accordingly.

These examples demonstrate various functionalities of the `curses.textpad` module, from simple single-line input to handling multiple lines and key events. They are designed to be clear, concise, and follow best practices for inclusion in official documentation.
