# tkinter.ttk — Tk themed widgets

Here are some examples of using the `ttk` module from the `tkinter` package:

```python
import tkinter as tk
from tkinter import ttk

# Create a Tkinter window
root = tk.Tk()
root.title("TTK Widgets")

# Create a Frame widget with TTK theme
frame = ttk.Frame(root, padding="10 10 10 10")
frame.pack(fill=tk.X)

# Add some buttons to the frame
button1 = ttk.Button(frame, text="Button 1", command=lambda: print("Button 1 clicked"))
button2 = ttk.Button(frame, text="Button 2", command=lambda: print("Button 2 clicked"))

button1.pack(side=tk.LEFT)
button2.pack(side=tk.LEFT)

# Create a Notebook widget
notebook = ttk.Notebook(root)
notebook.pack(fill=tk.BOTH, expand=True)

# Add two tabs to the notebook
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)

notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")

# Create a Treeview widget
tree = ttk.Treeview(root)

# Define columns for the treeview
tree["columns"] = ("Name", "Age")

# Format the columns
tree.column("#0", width=200)
tree.column("Name", anchor=tk.W, width=150)
tree.column("Age", anchor=tk.E, width=100)

# Create headings for the treeview
tree.heading("#0", text="Full Name", anchor=tk.W)
tree.heading("Name", text="First Name")
tree.heading("Age", text="Age")

# Insert some data into the treeview
for i in range(5):
    tree.insert("", "end", values=(f"John {i}", i))

# Pack the treeview widget
tree.pack(fill=tk.BOTH, expand=True)

# Create a Checkbutton widget
checkbutton = ttk.Checkbutton(root, text="Check me")
checkbutton.pack()

# Create a OptionMenu widget
option = ttk.OptionMenu(root, None, "Option 1", "Option 2", "Option 3")
option.pack()

root.mainloop()
```

This code creates a window with several TTK widgets:

*   A frame with two buttons
*   A notebook with two tabs
*   A treeview widget with columns and data
*   A checkbutton widget
*   An option menu widget

Each of these examples demonstrates how to use the corresponding TTK class or function in a `tkinter` application.
