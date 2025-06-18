# curses - Terminal handling for character-cell displays
## Table of Contents

1. [Example 1: Basic Terminal Screen Manipulation](#example-1-basic-terminal-screen-manipulation)
2. [Example 2: Handling Keyboard Input](#example-2-handling-keyboard-input)
3. [Example 3: Color Support](#example-3-color-support)
4. [Example 4: Handling Mouse Events](#example-4-handling-mouse-events)
5. [Example 5: Creating a Simple Menu](#example-5-creating-a-simple-menu)



The `curses` module in Python provides a way to write text-based user interfaces in a terminal. It allows you to create interactive programs that can respond to keyboard input, provide color support, and handle mouse events.

Below are comprehensive examples demonstrating various functionalities of the `curses` module:

### Example 1: Basic Terminal Screen Manipulation

```python
import curses

def main(stdscr):
    # Clear the screen
    stdscr.clear()

    # Set the cursor position to (0, 0)
    stdscr.move(0, 0)

    # Display a message on the terminal
    stdscr.addstr("Welcome to curses world!")

    # Refresh the screen to show the changes
    stdscr.refresh()

    # Wait for user input before exiting
    stdscr.getch()

# Start the application and run the `main` function
curses.wrapper(main)
```

**Explanation:**
- The `curses.wrapper()` function is used to initialize and clean up the curses environment. It takes a callable as an argument, which in this case is the `main` function.
- Inside `main`, we first clear the screen using `stdscr.clear()`.
- We then set the cursor position to (0, 0) using `stdscr.move(0, 0)`.
- The message "Welcome to curses world!" is added to the screen using `stdscr.addstr()`.
- `stdscr.refresh()` updates the display on the terminal.
- Finally, we wait for user input using `stdscr.getch()` before exiting the program.

### Example 2: Handling Keyboard Input

```python
import curses

def main(stdscr):
    # Clear the screen
    stdscr.clear()

    while True:
        # Wait for a key press
        ch = stdscr.getch()
        
        if ch == ord('q'):
            break
        
        # Display the pressed key
        stdscr.addstr("You pressed: " + chr(ch) + "\n")
        
        # Refresh the screen to show the changes
        stdscr.refresh()

# Start the application and run the `main` function
curses.wrapper(main)
```

**Explanation:**
- The program waits for a key press using `stdscr.getch()`.
- If 'q' is pressed, it breaks out of the loop.
- The pressed character (converted to its ASCII representation) is displayed on the screen.
- The screen is refreshed after each character is printed.

### Example 3: Color Support

```python
import curses

def main(stdscr):
    # Initialize color support
    if not curses.has_colors():
        stdscr.addstr("Your terminal does not support colors.")
        stdscr.refresh()
        stdscr.getch()
        return
    
    curses.start_color()
    
    # Define colors (0 for black, 14 for bright green)
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    
    # Clear the screen
    stdscr.clear()

    while True:
        # Move the cursor to a specific position
        stdscr.move(0, 5)
        
        # Display text with color
        stdscr.addstr("This is green text!", curses.color_pair(1))
        
        # Refresh the screen to show the changes
        stdscr.refresh()
        
        # Wait for a key press
        ch = stdscr.getch()

# Start the application and run the `main` function
curses.wrapper(main)
```

**Explanation:**
- Color support is enabled using `curses.start_color()`.
- We define a color pair where 14 is bright green on black using `curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)`.
- The cursor moves to position (0, 5), and the text "This is green text!" is displayed with the defined color.
- The screen is refreshed after each update, and the program waits for a key press before exiting.

### Example 4: Handling Mouse Events

```python
import curses


def main(stdscr):
    # Initialize mouse support
    stdscr.keypad(True)
    curses.mousemask(curses.ALL_MOUSE_EVENTS)

    while True:
        # Wait for a mouse event
        event = stdscr.getch()
        if event == curses.KEY_MOUSE:
            _, x, y, _, _ = curses.getmouse()

            # Clear the screen
            stdscr.clear()

            # Print the coordinates of the mouse click
            stdscr.addstr("Mouse clicked at: ({}, {})".format(x, y))

            # Refresh the screen to show the changes
            stdscr.refresh()


# Start the application and run the `main` function
curses.wrapper(main)
```

**Explanation:**
- Mouse support is enabled by setting the keypad and mouse mask.
- The program waits for a mouse event using `stdscr.getmouse()`.
- Once an event occurs, the coordinates of the mouse click are retrieved.
- These coordinates are printed on the screen.
- The screen is refreshed after each update.

### Example 5: Creating a Simple Menu

```python
import curses

def main(stdscr):
    # Clear the screen
    stdscr.clear()

    # Create a window for the menu
    win = curses.newwin(10, 20, 3, 5)
    win.box()
    win.refresh()

    while True:
        # Display menu options
        win.addstr(2, 2, "1. Option 1")
        win.addstr(4, 2, "2. Option 2")
        win.addstr(6, 2, "3. Exit")

        # Get user input
        ch = win.getch()

        if ch == ord('1'):
            stdscr.addstr(0, 0, "Option 1 selected")
        elif ch == ord('2'):
            stdscr.addstr(0, 0, "Option 2 selected")
        elif ch == ord('3'):
            break

        # Clear the menu after selection
        win.clear()
        win.box()
        win.refresh()
        stdscr.refresh()

# Start the application and run the `main` function
curses.wrapper(main)
```

**Explanation:**
- A new window is created using `curses.newwin()` with dimensions 10x20 starting at position (3, 5).
- The window is framed with a box.
- The menu options are displayed on this window.
- User input is captured from the user using `win.getch()`.
- If 'q' is pressed, the loop breaks and the program exits.
- After an option is selected, the menu is cleared before displaying it again.

These examples demonstrate basic usage of the `curses` module, covering terminal screen manipulation, keyboard input handling, color support, mouse events, and creating a simple menu. You can expand upon these examples to build more complex applications using the powerful features provided by the `curses` module.
