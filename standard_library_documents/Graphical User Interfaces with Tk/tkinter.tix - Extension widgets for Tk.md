# tkinter.tix — Extension widgets for Tk

Here's an example of using tkinter.Tix extension widgets:

```python
import tkinter as tk
from tkinter import tix

# Create main window
root = tk.Tk()
root.title("TIX Extension Widgets")

# Tix Label
tix_label = tix.Label(root, text="This is a TIX Label")
tix_label.pack()

# Tix Text Widget
tix_text = tix.Text(root)
tix_text.insert(tk.END, "This is a TIX Text widget\n")
tix_text.insert(tk.END, "You can use multiple lines of text.")
tix_text.pack()

# Tix Notebook (Note: Tix Notebook was removed in Tk 8.5, but we can emulate it)
def create_notebook():
    notebook = tix.Notebook(root)
    notebook.pack(fill="both", expand=True)

    # Create tabs
    tab1 = tix.Frame(notebook, text="Tab 1")
    tab2 = tix.Frame(notebook, text="Tab 2")

    # Add tabs to notebook
    notebook.add(tab1, text="Tab 1")
    notebook.add(tab2, text="Tab 2")

create_notebook()

# Tix Dialog (Note: Tix Dialog was removed in Tk 8.5, but we can use tkinter's built-in dialog box)
def create_dialog():
    def say_hello(name):
        print(f"Hello, {name}!")

    tix.Toplevel(root).title("TIX Dialog")
    label = tix.Label(tix.Toplevel(root), text="What is your name?")
    label.pack()
    entry = tix.Entry(tix.Toplevel(root))
    entry.pack()
    button = tix.Button(tix.Toplevel(root), text="Say Hello", command=lambda: say_hello(entry.get()))
    button.pack()

create_dialog()

# Tix Treeview
def create_treeview():
    treeview = tix.Treeview(root)
    treeview["columns"] = ("Name", "Age")
    treeview.column("#0", width=100)
    treeview.column("Name", anchor=tk.W, width=200)
    treeview.column("Age", anchor=tk.W, width=50)

    # Create headers
    treeview.heading("#0", text="Name", anchor=tk.W)
    treeview.heading("Name", text="Name", anchor=tk.W)
    treeview.heading("Age", text="Age", anchor=tk.W)

    # Insert data into treeview
    for i in range(5):
        treeview.insert("", tk.END, values=(f"Person {i}", f"{i}"))

create_treeview()

# Tix Note (Note: Tix Note was removed in Tk 8.5)
def create_note():
    tix.Notebook(root).pack(fill="both", expand=True)

create_note()

root.mainloop()
```

This example shows how to use some of the TIX extension widgets, including `Label`, `Text`, `Notebook` (emulated), `Dialog`, and `Treeview`.
