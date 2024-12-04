# curses — Terminal handling for character-cell displays

Here's an example of using the `curses` module in Python:

**installing curses**
```bash
pip install py-curses
```
or 
```bash
sudo apt-get install libncurses5-dev
```

**Example Code:**

```python
import curses

def main(stdscr):
    # Clear the screen and move to the top-left corner
    stdscr.clear()
    stdscr.move(0, 0)

    # Print a message to the screen
    stdscr.addstr("Welcome to the Curses tutorial!")

    # Refresh the screen to show the new text
    stdscr.refresh()

    # Wait for the user to press a key
    c = stdscr.getch()
    if c != -1:
        print(f"You pressed {c}")
    else:
        print("Press 'q' to quit")

# Call the main function when the program starts
if __name__ == "__main__":
    curses.wrapper(main)
```

**Explanation:**

*   We import the `curses` module.
*   The `curses.wrapper` function is used to initialize and clean up after the `main` function. It takes our `main` function as an argument, which will be executed with a fresh curses screen.
*   Inside the `main` function:
    *   We clear the screen by calling `stdscr.clear()` and move the cursor to the top-left corner using `stdscr.move(0, 0)`.
    *   We print a message to the screen using `stdscr.addstr()`. The string is printed at the current cursor position.
    *   After printing the message, we refresh the screen with `stdscr.refresh()` so that the new text becomes visible.
    *   Finally, we wait for the user to press a key using `stdscr.getch()`. If the user presses a key, it's stored in the variable `c`, and its value is printed. If the user presses 'q', the program exits.

**Example Use Cases:**

*   Creating menus or navigation systems
*   Building text-based games or adventures
*   Developing command-line interfaces (CLI)
*   Creating interactive terminal applications

**Additional Functions:**

Some additional functions you can use in `curses` include:

*   `stdscr.addstr(y, x, str)`: Add a string to the screen at position (y,x).
*   `stdscr.move(y, x)`: Move the cursor to position (y,x).
*   `stdscr.clear()`: Clear the entire screen.
*   `stdscr.refresh()`: Refresh the entire screen with the new text.
*   `stdscr.getch()`: Wait for the user to press a key and return its value.
