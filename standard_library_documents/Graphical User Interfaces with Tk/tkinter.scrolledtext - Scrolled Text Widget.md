# tkinter.scrolledtext - Scrolled Text Widget

The `scrolledtext` module in Python's standard library provides a `ScrolledText` widget, which is similar to the `Text` widget but with added support for scrolling. This widget is particularly useful when you need a text entry area that can handle large amounts of text and provide easy navigation through it.

Below are comprehensive examples for each functionality provided by the `scrolledtext` module:

### Example 1: Basic Scrolled Text Widget

```python
import tkinter as tk
from tkinter import scrolledtext

def create_scrolled_text_window():
    # Create the main window
    root = tk.Tk()
    root.title("Basic Scrolled Text Widget")

    # Create a ScrolledText widget with fixed width and height
    st = scrolledtext.ScrolledText(root, width=40, height=10)
    st.pack(padx=10, pady=10)

    # Insert some initial text into the widget
    st.insert(tk.INSERT, "This is a basic example of a ScrolledText widget.")

    # Start the GUI event loop
    root.mainloop()

# Call the function to create and display the window
create_scrolled_text_window()
```

### Example 2: Customizing Scrollbar Appearance

```python
import tkinter as tk
from tkinter import scrolledtext

def customize_scrollbar():
    # Create the main window
    root = tk.Tk()
    root.title("Customized Scrolled Text Widget")

    # Configure the appearance of the scrollbar
    custom_scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL)
    custom_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Use the scrollbar with a ScrolledText widget
    st = scrolledtext.ScrolledText(root, width=40, height=10, yscrollcommand=custom_scrollbar.set)
    st.pack(padx=10, pady=10)

    # Insert some initial text into the widget
    st.insert(tk.INSERT, "This example demonstrates how to customize the scrollbar appearance.")

    # Configure the scrolling command for the scrollbar
    custom_scrollbar.config(command=st.yview)

    # Start the GUI event loop
    root.mainloop()

# Call the function to create and display the window
customize_scrollbar()
```

### Example 3: Handling Text Events

```python
import tkinter as tk
from tkinter import scrolledtext, messagebox

def handle_text_events():
    # Create the main window
    root = tk.Tk()
    root.title("Text Event Handling")

    # Create a ScrolledText widget with a simple text event handler
    st = scrolledtext.ScrolledText(root, width=40, height=10)
    st.pack(padx=10, pady=10)

    # Define an event handler function
    def on_text_change(event):
        messagebox.showinfo("Event Details", f"Changed at position: {event.x}, {event.y}")

    # Bind the text change event to the ScrolledText widget
    st.bind("<KeyRelease>", on_text_change)

    # Insert some initial text into the widget
    st.insert(tk.INSERT, "This example demonstrates how to handle text events.")

    # Start the GUI event loop
    root.mainloop()

# Call the function to create and display the window
handle_text_events()
```

### Example 4: Configuring Text Formatting

```python
import tkinter as tk
from tkinter import scrolledtext, messagebox

def configure_text_formatting():
    # Create the main window
    root = tk.Tk()
    root.title("Text Formatting")

    # Create a ScrolledText widget with formatting options
    st = scrolledtext.ScrolledText(root, width=40, height=10)
    st.pack(padx=10, pady=10)

    # Define functions to apply different formatting styles
    def bold_text():
        st.tag_add("bold", "sel.first", "sel.last")

    def italic_text():
        st.tag_add("italic", "sel.first", "sel.last")

    def set_font(font_family, font_size):
        st.tag_config("customfont", font=(font_family, font_size))

    # Create buttons to apply formatting
    bold_button = tk.Button(root, text="Bold", command=bold_text)
    bold_button.pack(side=tk.LEFT, padx=5)

    italic_button = tk.Button(root, text="Italic", command=italic_text)
    italic_button.pack(side=tk.LEFT, padx=5)

    font_family_label = tk.Label(root, text="Font Family:")
    font_family_label.pack(side=tk.LEFT, padx=5)

    font_family_entry = tk.Entry(root, width=10)
    font_family_entry.pack(side=tk.LEFT, padx=5)

    font_size_label = tk.Label(root, text="Font Size:")
    font_size_label.pack(side=tk.LEFT, padx=5)

    font_size_entry = tk.Entry(root, width=5)
    font_size_entry.pack(side=tk.LEFT, padx=5)

    set_font_button = tk.Button(root, text="Set Font", command=lambda: set_font(font_family_entry.get(), int(font_size_entry.get())))
    set_font_button.pack(side=tk.LEFT, padx=5)

    # Insert some initial text into the widget
    st.insert(tk.INSERT, "This example demonstrates how to configure text formatting.")

    # Start the GUI event loop
    root.mainloop()

# Call the function to create and display the window
configure_text_formatting()
```

### Example 5: Customizing Text Colors

```python
import tkinter as tk
from tkinter import scrolledtext, messagebox

def customize_text_colors():
    # Create the main window
    root = tk.Tk()
    root.title("Custom Text Colors")

    # Create a ScrolledText widget with color customization
    st = scrolledtext.ScrolledText(root, width=40, height=10)
    st.pack(padx=10, pady=10)

    # Define functions to change text colors
    def set_red_color():
        st.tag_config("red", foreground="red")

    def set_green_color():
        st.tag_config("green", foreground="green")

    def set_blue_color():
        st.tag_config("blue", foreground="blue")

    # Create buttons to apply color changes
    red_button = tk.Button(root, text="Red", command=set_red_color)
    red_button.pack(side=tk.LEFT, padx=5)

    green_button = tk.Button(root, text="Green", command=set_green_color)
    green_button.pack(side=tk.LEFT, padx=5)

    blue_button = tk.Button(root, text="Blue", command=set_blue_color)
    blue_button.pack(side=tk.LEFT, padx=5)

    # Insert some initial text into the widget
    st.insert(tk.INSERT, "This example demonstrates how to customize text colors.")

    # Start the GUI event loop
    root.mainloop()

# Call the function to create and display the window
customize_text_colors()
```

### Example 6: Handling Text Selection

```python
import tkinter as tk
from tkinter import scrolledtext, messagebox

def handle_text_selection():
    # Create the main window
    root = tk.Tk()
    root.title("Text Selection")

    # Create a ScrolledText widget with selection handling
    st = scrolledtext.ScrolledText(root, width=40, height=10)
    st.pack(padx=10, pady=10)

    # Define functions to handle text selections
    def select_text():
        selected_text = st.get("sel.first", "sel.last")
        messagebox.showinfo("Selected Text", f"Selected text: {selected_text}")

    # Create a button to select text
    select_button = tk.Button(root, text="Select Text", command=select_text)
    select_button.pack(side=tk.LEFT, padx=5)

    # Insert some initial text into the widget
    st.insert(tk.INSERT, "This example demonstrates how to handle text selections.")

    # Start the GUI event loop
    root.mainloop()

# Call the function to create and display the window
handle_text_selection()
```

These examples cover various functionalities of the `scrolledtext` module, including basic usage, customizing widget appearance, handling text events, configuring text formatting, customizing text colors, and managing text selections. Each example is designed to be self-contained and can be run independently as a standalone script.
