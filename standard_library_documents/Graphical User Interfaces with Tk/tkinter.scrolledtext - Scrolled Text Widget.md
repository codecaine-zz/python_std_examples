# tkinter.scrolledtext — Scrolled Text Widget

**Scrolled Text Widget (tkinter.scrolledtext)**
====================================================

The `tkinter.scrolledtext` module provides a widget that allows for editing of text, with additional functionality for scrolling.

### Example Use Cases:

1. Creating a scrolled text area for displaying log messages or error logs.
2. Building an email client interface with a large text area for composing and viewing emails.

### Code Examples:
```python
import tkinter as tk
from tkinter import scrolledtext

# Create the main window
root = tk.Tk()
root.title("Scrolled Text Widget")

# Create a frame to hold the widget
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Create a scrolled text area with a fixed width and height
text_area = scrolledtext.ScrolledText(frame,
                                    width=60,
                                    height=20,
                                    wrap=tk.WORD)
text_area.pack()

# Add some sample text to the widget
sample_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
text_area.insert(tk.INSERT, sample_text)

# Create a button to insert new text into the widget
def insert_new_text():
    new_text = input("Enter new text: ")
    text_area.insert(tk.END, new_text)

button = tk.Button(frame, text="Insert New Text", command=insert_new_text)
button.pack()

# Run the application
root.mainloop()
```

### Usage:

1. Import the `scrolledtext` module from the `tkinter` library.
2. Create a `ScrolledText` widget by passing the required arguments (width, height, and wrap mode) to its constructor.
3. Use the `insert` method to add text to the widget at the specified location.
4. Use the `delete` method to delete text from the widget.

### Methods:

*   `insert(location, text)`: Inserts the given text at the specified location in the widget.
*   `delete(start, stop)`: Deletes the text between the start and stop indices in the widget.
*   `get(from_idx, to_idx)`: Returns the text contained within the specified range of indices.

### Attributes:

*   `width` (int): The width of the widget's text area.
*   `height` (int): The height of the widget's text area.
*   `wrap` (tkinter.WORD | tkinter.NONE | tkinter.ALL): Specifies how to wrap the text in the widget. Can be set to `tkinter.WORD`, `tkinter.NONE`, or `tkinter.ALL`.

### Event-Driven Programming:

The `ScrolledText` widget raises several events when the user interacts with it, including:

*   `key_press`: Raised when a key is pressed while focusing on the widget.
*   `key_release`: Raised when a key is released while focusing on the widget.
*   `focus_in`: Raised when the widget receives focus.
*   `focus_out`: Raised when the widget loses focus.
