# curses.textpad — Text input widget for curses programs

**Curses Textpad Module**
=========================

The `curses.textpad` module provides a widget that can be used to create a text input area in a curses program.

**Example Usage**
-----------------

```python
import curses
from curses import textpad

def main(stdscr):
    # Create a new textpad object
    tp = textpad.TextioWidget(stdscr, 10, 30)

    # Use the cursor position to scroll and edit the input
    while True:
        stdscr.clear()
        tp.draw()
        stdscr.addstr(15, 0, "Enter your message:")
        stdscr.refresh()

        # Get user input
        c = stdscr.getch()
        if c == ord('\n'):
            break
        elif c != -1:  # Check for key press
            tp.move(0, 0)
            tp.delete(0, curses.CURSOR)
            tp.addstr(c)

    # Output the final input
    print(tp.get_value())

curses.wrapper(main)
```

**API Documentation**
--------------------

### `textpad.TextioWidget(stdscr, height, width)`

Creates a new text input widget.

*   `stdscr`: The curses standard screen object.
*   `height`: The initial height of the text input area in lines.
*   `width`: The initial width of the text input area in columns.

### `tp.move(row, col)`

Moves the cursor to the specified row and column.

*   `row`: The new y-coordinate (0-`height - 1`) of the cursor.
*   `col`: The new x-coordinate (0-`width - 1`) of the cursor.

### `tp.delete(pos, len)`

Deletes text from the widget starting at the specified position.

*   `pos`: The first character to delete (0-`len - 1`).
*   `len`: The number of characters to delete.

### `tp.addstr(strng)`

Adds a string to the end of the current value in the widget.

*   `strng`: The string to add.

### `tp.get_value()`

Returns the final input value as a string.

**Explanation**
---------------

This example demonstrates how to create a text input area using the `curses.textpad` module. We first import the necessary modules and define the main function, which takes the curses standard screen object as an argument.

Inside the main function, we create a new text input widget with a height of 10 lines and a width of 30 columns. Then, we enter an infinite loop where we clear the screen, draw the current value in the textpad widget, refresh the screen, and get user input using `stdscr.getch()`. If the user presses Enter (`c == ord('\n')`), we break out of the loop.

After breaking out of the loop, we output the final input value by calling `tp.get_value()`.

Finally, we call `curses.wrapper(main)` to initialize and run the curses library.
