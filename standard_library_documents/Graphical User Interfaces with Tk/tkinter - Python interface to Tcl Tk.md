# tkinter - Python interface to Tcl/Tk

**Tkinter Module Code Examples**
=====================================

### Importing Tkinter

```python
# Importing Tkinter module
import tkinter as tk

# Creating a new Tk instance
root = tk.Tk()

# Setting the window title
root.title("My Tkinter App")

# Setting the window size
root.geometry("500x300")
```

### Creating Widgets

#### Labels

```python
# Creating a label widget
label = tk.Label(root, text="Hello, World!")

# Adding the label to the window
label.pack()

# Configuring the label's font and color
label.config(font=("Arial", 24), fg="blue")
```

#### Buttons

```python
# Creating a button widget
button = tk.Button(root, text="Click Me!", command=lambda: print("Button clicked!"))

# Adding the button to the window
button.pack()

# Configuring the button's font and color
button.config(font=("Arial", 18), fg="red")
```

#### Text Boxes

```python
# Creating a text box widget
text_box = tk.Text(root, height=10, width=30)

# Adding the text box to the window
text_box.pack()

# Writing some text into the text box
text_box.insert(tk.END, "Hello, World!")
```

#### Checkboxes

```python
# Creating a checkbox widget
checkbox_var = tk.BooleanVar()
checkbox = tk.Checkbutton(root, variable=checkbox_var)

# Adding the checkbox to the window
checkbox.pack()

# Configuring the checkbox's text and font
checkbox.config(text="Check me!", font=("Arial", 16))
```

#### Radio Buttons

```python
# Creating radio button widgets
radio_var = tk.StringVar()
radio1 = tk.Radiobutton(root, variable=radio_var, value="Option 1")
radio2 = tk.Radiobutton(root, variable=radio_var, value="Option 2")

# Adding the radio buttons to the window
radio1.pack()
radio2.pack()

# Configuring the radio buttons' text and font
radio1.config(text="Option 1", font=("Arial", 16))
radio2.config(text="Option 2", font=("Arial", 16))
```

### Event Handling

```python
# Binding an event to a button widget
def on_button_click():
    print("Button clicked!")

button = tk.Button(root, text="Click Me!", command=on_button_click)
```

### Layout Management

```python
# Using the grid layout manager
label = tk.Label(root, text="Hello, World!")
label.grid(row=0, column=0)

button = tk.Button(root, text="Click Me!")
button.grid(row=1, column=0)
```

### Frame and Pack Methods

```python
# Creating a frame widget
frame = tk.Frame(root)

# Adding widgets to the frame
label = tk.Label(frame, text="Hello, World!")
label.pack()

button = tk.Button(frame, text="Click Me!")
button.pack()

# Adding the frame to the window
frame.pack()
```

### Message Box

```python
# Importing messagebox module
import tkinter.messagebox as mb

# Showing a message box with an OK button
mb.showinfo("Hello", "World!")

# Showing a message box with cancel and OK buttons
mb.askokcancel("Hello", "World!")
```

### Window Closing

```python
# Binding the window close event to a function
def on_close():
    print("Window closed!")

root.protocol("WM_DELETE_WINDOW", on_close)

# Running the application's main loop
root.mainloop()
```

**Full Code Example:**

```python
import tkinter as tk
from tkinter import messagebox

def on_button_click():
    print("Button clicked!")

def on_close():
    print("Window closed!")

root = tk.Tk()

label = tk.Label(root, text="Hello, World!")
label.pack()

button = tk.Button(root, text="Click Me!", command=on_button_click)
button.pack()

checkbox_var = tk.BooleanVar()
checkbox = tk.Checkbutton(root, variable=checkbox_var)
checkbox.pack()

radio_var = tk.StringVar()
radio1 = tk.Radiobutton(root, variable=radio_var, value="Option 1")
radio2 = tk.Radiobutton(root, variable=radio_var, value="Option 2")

root.title("My Tkinter App")
root.geometry("500x300")

frame = tk.Frame(root)
label_frame = tk.Label(frame, text="Hello, World!")
label_frame.pack()

button_frame = tk.Button(frame, text="Click Me!", command=lambda: print("Button clicked!"))
button_frame.pack()

checkbox_frame = tk.Checkbutton(frame, variable=checkbox_var)
checkbox_frame.pack()

radio_frame = tk.Frame(root)
radio1.pack()
radio2.pack()

frame.pack()

def show_message():
    messagebox.showinfo("Hello", "World!")

root.protocol("WM_DELETE_WINDOW", on_close)

root.mainloop()
```

This example demonstrates various aspects of the Tkinter module, including creating widgets, event handling, layout management, and more.
