# tkinter.ttk - Tk themed widgets

The `ttk` (Themed Tk) module in the Python standard library provides a collection of high-level themed widgets that are designed to look and feel like those found in modern desktop applications. These widgets are based on the ttk toolkit, which is included with many window managers such as GTK+ and Qt. Below are comprehensive examples for each functionality available in the `ttk` module.

### 1. Creating a Basic Toplevel Window

```python
import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Basic Toplevel Window")

# Create and pack a label widget
label = ttk.Label(root, text="Welcome to Tk themed widgets!")
label.pack(pady=10)

# Start the Tk event loop
root.mainloop()
```

### 2. Adding Buttons

```python
import tkinter as tk
from tkinter import ttk

def button_click():
    print("Button was clicked!")

# Create the main window
root = tk.Tk()
root.title("Buttons Example")

# Create and pack a button widget
button = ttk.Button(root, text="Click Me", command=button_click)
button.pack(pady=10)

# Start the Tk event loop
root.mainloop()
```

### 3. Creating Entry Widgets

```python
import tkinter as tk
from tkinter import ttk

def get_entry_value():
    value = entry.get()
    print(f"Entry Value: {value}")

# Create the main window
root = tk.Tk()
root.title("Entry Widget Example")

# Create and pack an entry widget
entry = ttk.Entry(root, width=30)
entry.pack(pady=10)

# Create a button to trigger the entry value retrieval
button = ttk.Button(root, text="Get Value", command=get_entry_value)
button.pack(pady=10)

# Start the Tk event loop
root.mainloop()
```

### 4. Using Checkbuttons

```python
import tkinter as tk
from tkinter import ttk

def check_button_state():
    state = check_var.get()
    print(f"Check button is {'checked' if state else 'unchecked'}.")

# Create the main window
root = tk.Tk()
root.title("Checkbutton Example")

# Define a variable to store the checkbutton state
check_var = tk.BooleanVar()

# Create and pack a checkbutton widget
check_button = ttk.Checkbutton(root, text="Enable Functionality", variable=check_var)
check_button.pack(pady=10)

# Create a button to trigger the state retrieval
button = ttk.Button(root, text="Get State", command=check_button_state)
button.pack(pady=10)

# Start the Tk event loop
root.mainloop()
```

### 5. Using Radiobuttons

```python
import tkinter as tk
from tkinter import ttk

def radio_button_click(value):
    print(f"Selected value: {value}")

# Create the main window
root = tk.Tk()
root.title("Radiobutton Example")

# Define variables to store the selected values
var = tk.StringVar()

# Create and pack radiobutton widgets
radio1 = ttk.Radiobutton(root, text="Option 1", variable=var, value="option1")
radio1.pack(pady=5)

radio2 = ttk.Radiobutton(root, text="Option 2", variable=var, value="option2")
radio2.pack(pady=5)

# Create a button to trigger the selected value retrieval
button = ttk.Button(root, text="Get Selection", command=lambda: radio_button_click(var.get()))
button.pack(pady=10)

# Start the Tk event loop
root.mainloop()
```

### 6. Using Comboboxes

```python
import tkinter as tk
from tkinter import ttk

def combobox_select(event):
    selected_value = combobox.get()
    print(f"Selected value: {selected_value}")

# Create the main window
root = tk.Tk()
root.title("Combobox Example")

# Define options for the combobox
options = ["Option 1", "Option 2", "Option 3"]

# Create and pack a combobox widget
combobox = ttk.Combobox(root, values=options)
combobox.pack(pady=10)

# Bind an event to handle selection changes
combobox.bind("<<ComboboxSelected>>", combobox_select)

# Start the Tk event loop
root.mainloop()
```

### 7. Using Progress Bars

```python
import tkinter as tk
from tkinter import ttk

def update_progress():
    progress_var.set(progress_var.get() + 10)
    if progress_var.get() >= 100:
        progress_bar.stop()

# Create the main window
root = tk.Tk()
root.title("Progress Bar Example")

# Define variables to store the progress bar value and state
progress_var = tk.IntVar(value=0)

# Create and pack a progress bar widget
progress_bar = ttk.Progressbar(root, orient=tk.HORIZONTAL, length=200, variable=progress_var)
progress_bar.pack(pady=10)

# Start the update function to simulate progress
root.after(500, update_progress)

# Start the Tk event loop
root.mainloop()
```

### 8. Using Scrolled Text Widgets

```python
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext  # Add this import

def add_text():
    text.insert(tk.END, "This is some additional text.\n")

# Create the main window
root = tk.Tk()
root.title("Scrolled Text Example")

# Define a frame to hold the scrolled text widget
frame = ttk.Frame(root)
frame.pack(pady=10)

# Create and pack a scrolledtext widget
text = scrolledtext.ScrolledText(frame, width=40, height=5)
text.insert(tk.END, "Hello, Tk themed widgets!\n")
text.pack(pady=10)

# Create a button to add more text
button = ttk.Button(root, text="Add Text", command=add_text)
button.pack(pady=10)

# Start the Tk event loop
root.mainloop()
```

### 9. Using Combobox with Multiple Selection

```python
import tkinter as tk
from tkinter import ttk

def combo_select(event):
    selected_values = [var.get() for var in checkbox_vars if var.get()]
    print(f"Selected values: {selected_values}")

# Create the main window
root = tk.Tk()
root.title("Combobox with Multiple Selection Example")

# Define options for the combobox
options = ["Option 1", "Option 2", "Option 3"]

# Create and pack radiobuttons (checkboxes) corresponding to each option
checkbox_vars = [tk.BooleanVar() for _ in options]
for i, option in enumerate(options):
    ttk.Checkbutton(root, text=option, variable=checkbox_vars[i]).pack(pady=5)

# Create a combobox widget
combobox = ttk.Combobox(root, values=options)
combobox.pack(pady=10)

# Bind an event to handle selection changes
combobox.bind("<<ComboboxSelected>>", combo_select)

# Start the Tk event loop
root.mainloop()
```

### 10. Using Menus

```python
import tkinter as tk
from tkinter import ttk

def menu_item_click(item):
    print(f"Menu item clicked: {item}")

# Create the main window
root = tk.Tk()
root.title("Menu Example")

# Define a function to create and configure menus
def create_menu():
    menubar = tk.Menu(root)
    root.config(menu=menubar)

    # File menu
    file_menu = tk.Menu(menubar, tearoff=0)
    file_menu.add_command(label="Open", command=lambda: menu_item_click("Open"))
    file_menu.add_command(label="Save", command=lambda: menu_item_click("Save"))
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=file_menu)

    # Edit menu
    edit_menu = tk.Menu(menubar, tearoff=0)
    edit_menu.add_command(label="Cut", command=lambda: menu_item_click("Cut"))
    edit_menu.add_command(label="Copy", command=lambda: menu_item_click("Copy"))
    edit_menu.add_command(label="Paste", command=lambda: menu_item_click("Paste"))
    menubar.add_cascade(label="Edit", menu=edit_menu)

# Call the function to create and configure menus
create_menu()

# Start the Tk event loop
root.mainloop()
```

These examples demonstrate various functionalities of the `ttk` module, including creating basic widgets like buttons, entry fields, checkboxes, radio buttons, comboboxes, progress bars, scrolled text widgets, and more. Each example includes comments to explain each step for clarity and is suitable for inclusion in official documentation or tutorials.
