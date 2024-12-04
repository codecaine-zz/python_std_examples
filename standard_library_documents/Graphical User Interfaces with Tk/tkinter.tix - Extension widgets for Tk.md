# tkinter.tix - Extension widgets for Tk

The `tkinter.tix` module provides extension widgets that are not part of the core Tkinter toolkit but add functionality like dialog boxes, progress bars, and more. Below are comprehensive and well-documented code examples for each feature in the `tkinter.tix` module.

### 1. Progress Bar

```python
import tkinter as tk
from tkinter import ttk

def update_progress():
    current = int(progress_var.get())
    if current >= 100:
        progress_var.set(0)
    else:
        progress_var.set(current + 5)

root = tk.Tk()
root.title("Progress Bar Example")

# Create a variable to hold the progress value
progress_var = tk.IntVar(value=0)

# Create a progress bar widget
progress_bar = ttk.Progressbar(root, orient='horizontal', mode='determinate', length=200, variable=progress_var)
progress_bar.pack(pady=10)

# Create a button to update the progress
update_button = ttk.Button(root, text="Update Progress", command=update_progress)
update_button.pack()

root.mainloop()
```

### 2. Dialog Boxes

#### Example: Message Box

```python
import tkinter as tk
from tkinter import messagebox

def show_message():
    # Display a message box with an OK button
    response = messagebox.showinfo("Information", "This is a simple information message.")
    
    # You can also use other types like warning, error, etc.
    if response == 'ok':
        print("OK button clicked.")

root = tk.Tk()
root.title("Message Box Example")

# Create a button to show the message box
show_button = ttk.Button(root, text="Show Message", command=show_message)
show_button.pack(pady=10)

root.mainloop()
```

#### Example: Entry Dialog

```python
import tkinter as tk
from tkinter import simpledialog

def get_name():
    # Get input from a dialog box with an OK and Cancel button
    name = simpledialog.askstring("Input", "Please enter your name:")
    
    if name:
        print(f"Hello, {name}!")

root = tk.Tk()
root.title("Entry Dialog Example")

# Create a button to show the entry dialog
show_button = ttk.Button(root, text="Get Name", command=get_name)
show_button.pack(pady=10)

root.mainloop()
```

### 3. Listbox

```python
import tkinter as tk
from tkinter import scrolledtext

def add_item():
    item = listbox.get(listbox.curselection())
    if item:
        print(f"Item added: {item}")

def remove_item():
    item = listbox.get(listbox.curselection())
    if item:
        listbox.delete(listbox.curselection())

root = tk.Tk()
root.title("Listbox Example")

# Create a scrolled text area for the listbox
scrolled_text = scrolledtext.ScrolledText(root, width=40, height=10)
scrolled_text.pack(pady=10)

# Create a listbox widget
listbox = tk.Listbox(scrolled_text)
listbox.insert(tk.END, "Item 1", "Item 2", "Item 3")
listbox.pack()

# Create buttons to add and remove items from the listbox
add_button = ttk.Button(root, text="Add Selected Item", command=add_item)
add_button.pack(pady=5)

remove_button = ttk.Button(root, text="Remove Selected Item", command=remove_item)
remove_button.pack(pady=5)

root.mainloop()
```

### 4. Treeview

```python
import tkinter as tk
from tkinter import scrolledtext

def select_item(event):
    item = tree.selection()[0]
    print(f"Selected item: {item}")

def add_item():
    item = listbox.get(listbox.curselection())
    if item:
        tree.insert("", "end", text=item)

root = tk.Tk()
root.title("Treeview Example")

# Create a scrolled text area for the treeview
scrolled_text = scrolledtext.ScrolledText(root, width=40, height=10)
scrolled_text.pack(pady=10)

# Create a listbox widget to select items from
listbox = tk.Listbox(scrolled_text)
listbox.insert(tk.END, "Item 1", "Item 2", "Item 3")
listbox.pack()

# Create a treeview widget
tree = ttk.Treeview(scrolled_text, columns=("column1",))
tree.heading("#0", text="Items")
tree.column("column1", width=100)
tree.insert("", "end", text="Root Node")
scrolled_text.window_create("end", tree)

# Bind the selection event to a function
tree.bind("<<TreeviewSelect>>", select_item)

# Create buttons to add items to the treeview and select from the listbox
add_button = ttk.Button(root, text="Add Selected Item", command=add_item)
add_button.pack(pady=5)

root.mainloop()
```

### 5. Scrolled Text Area

```python
import tkinter as tk
from tkinter import scrolledtext

def clear_text():
    text.delete("1.0", "end")

def insert_text(event):
    text.insert(tk.END, event.char)

root = tk.Tk()
root.title("Scrolled Text Area Example")

# Create a scrolled text area widget
text = scrolledtext.ScrolledText(root, width=40, height=10)
text.pack(pady=10)

# Bind the key press event to a function
text.bind("<Key>", insert_text)

# Create a button to clear the text in the scrolled text area
clear_button = ttk.Button(root, text="Clear Text", command=clear_text)
clear_button.pack(pady=5)

root.mainloop()
```

### 6. Dialog Box with Entry

```python
import tkinter as tk
from tkinter import simpledialog

def get_email():
    # Get input from a dialog box with an OK and Cancel button
    email = simpledialog.askstring("Input", "Please enter your email:")
    
    if email:
        print(f"Email entered: {email}")

root = tk.Tk()
root.title("Dialog Box with Entry Example")

# Create a button to show the entry dialog
show_button = ttk.Button(root, text="Get Email", command=get_email)
show_button.pack(pady=10)

root.mainloop()
```

### 7. Option Menu

```python
import tkinter as tk
from tkinter import ttk

def on_option_change(option):
    print(f"Option selected: {option}")

root = tk.Tk()
root.title("Option Menu Example")

# Create a variable to hold the selected option
selected_option = tk.StringVar()

# Create an option menu widget with options 'Apple', 'Banana', and 'Cherry'
option_menu = ttk.OptionMenu(root, selected_option, "Apple", "Banana", "Cherry")
option_menu.pack(pady=10)

# Bind a function to the selection event
option_menu.bind("<<ComboboxSelected>>", lambda event: on_option_change(selected_option.get()))

root.mainloop()
```

These examples demonstrate various functionalities provided by the `tkinter.tix` module, including progress bars, dialog boxes, listboxes, treeviews, scrolled text areas, and more. Each example is designed to be clear, concise, and follows best practices for Tkinter development.
