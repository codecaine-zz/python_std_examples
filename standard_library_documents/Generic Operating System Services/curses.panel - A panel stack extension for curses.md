# curses.panel - A panel stack extension for curses

The `curses.panel` module provides a set of functions to create, manipulate, and manage panels within a curses window. Panels are useful for organizing multiple windows on the screen and allowing them to be stacked on top of each other with z-order management. Below are comprehensive code examples demonstrating various functionalities provided by the `curses.panel` module.

### Example 1: Creating and Displaying Multiple Panels

```python
import curses
from curses import panel as p

def main(stdscr):
    # Initialize the screen
    stdscr.clear()
    stdscr.refresh()

    # Create a new window
    win1 = curses.newwin(5, 10, 2, 5)
    win2 = curses.newwin(3, 8, 7, 3)

    # Create panels for each window
    p1 = p.new_panel(win1)
    p2 = p.new_panel(win2)

    # Update the stack to bring panel1 to the front
    p.update_panels()

    # Refresh the screen with all panels
    stdscr.refresh()

    # Add some content to win1 and win2
    stdscr.addstr(3, 6, "Panel 1")
    stdscr.addstr(5, 7, "Panel 2")

    # Get user input to change panel order
    key = stdscr.getch()
    
    if key == ord('1'):
        p.update_panels()  # Bring win1 to the front
        stdscr.refresh()
    elif key == ord('2'):
        p.update_panels()  # Bring win2 to the front
        stdscr.refresh()

curses.wrapper(main)
```

### Example 2: Moving a Panel

```python
import curses
from curses import panel as p

def main(stdscr):
    # Initialize the screen
    stdscr.clear()
    stdscr.refresh()

    # Create two windows and their panels
    win1 = curses.newwin(5, 10, 2, 5)
    win2 = curses.newwin(3, 8, 7, 3)

    p1 = p.new_panel(win1)
    p2 = p.new_panel(win2)

    # Update the stack to bring panel1 to the front
    p.update_panels()
    stdscr.refresh()

    # Move win1 below win2 by swapping their positions in the panel stack
    p.swapwin(p1, p2)
    p.update_panels()
    stdscr.refresh()

curses.wrapper(main)
```

### Example 3: Hiding and Showing Panels

```python
import curses
from curses import panel as p

def main(stdscr):
    # Initialize the screen
    stdscr.clear()
    stdscr.refresh()

    # Create two windows and their panels
    win1 = curses.newwin(5, 10, 2, 5)
    win2 = curses.newwin(3, 8, 7, 3)

    p1 = p.new_panel(win1)
    p2 = p.new_panel(win2)

    # Update the stack to bring panel1 to the front
    p.update_panels()
    stdscr.refresh()

    # Hide win2 by calling hide()
    p.hide(p2)
    p.update_panels()

    # Display win2 by calling show()
    p.show(p2)
    p.update_panels()

curses.wrapper(main)
```

### Example 4: Deleting a Panel

```python
import curses
from curses import panel as p

def main(stdscr):
    # Initialize the screen
    stdscr.clear()
    stdscr.refresh()

    # Create two windows and their panels
    win1 = curses.newwin(5, 10, 2, 5)
    win2 = curses.newwin(3, 8, 7, 3)

    p1 = p.new_panel(win1)
    p2 = p.new_panel(win2)

    # Update the stack to bring panel1 to the front
    p.update_panels()
    stdscr.refresh()

    # Delete win2 by calling delete_panel()
    p.delete_panel(p2)
    p.update_panels()

curses.wrapper(main)
```

### Example 5: Getting and Setting Panel Attributes

```python
import curses
from curses import panel as p

def main(stdscr):
    # Initialize the screen
    stdscr.clear()
    stdscr.refresh()

    # Create two windows and their panels
    win1 = curses.newwin(5, 10, 2, 5)
    win2 = curses.newwin(3, 8, 7, 3)

    p1 = p.new_panel(win1)
    p2 = p.new_panel(win2)

    # Update the stack to bring panel1 to the front
    p.update_panels()
    stdscr.refresh()

    # Get and print the attributes of win1
    attrs = p.get_attr(p1)
    print(f"Attributes of win1: {attrs}")

    # Set new attributes for win2 (e.g., curses.A_REVERSE)
    p.set_attr(p2, curses.A_REVERSE)
    p.update_panels()
    stdscr.refresh()

curses.wrapper(main)
```

### Explanation

- **Initialization and Setup**: The examples start by initializing the screen using `curses.wrapper`, which ensures proper cleanup after the main function exits.
- **Panel Creation**: Each window is created using `curses.newwin` and then wrapped in a panel with `p.new_panel`.
- **Stack Management**: Panels are updated using `p.update_panels()` to reorder them according to their stacking order.
- **User Input Handling**: Examples demonstrate how to change the stack by getting user input and using `p.swapwin`, `p.hide`, `p.show`, and `p.delete_panel`.
- **Attribute Manipulation**: Panels can have attributes set and retrieved using `p.set_attr` and `p.get_attr`.

These examples cover the basic functionalities of managing panels in a curses application, from creating and showing them to managing their stacking order and attributes.
