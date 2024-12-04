# zipapp - Manage executable Python zip archives

The `zipapp` module in Python is used to create standalone executables from Python applications by embedding the interpreter into a ZIP archive. This allows you to distribute your application without requiring a separate Python installation, which can be useful for distributing small projects or for creating installable packages.

Here are some code examples that demonstrate various functionalities of the `zipapp` module:

### Example 1: Creating an Executable from a Script

Suppose you have a simple script named `my_script.py`:
```python
# my_script.py
def main():
    print("Hello, world!")

if __name__ == "__main__":
    main()
```

You can use the `zipapp.create_archive` function to create an executable from this script:

```python
import zipapp

# Create a ZIP file containing the script and the Python interpreter
with open('my_script.zip', 'wb') as f:
    z = zipapp.create_archive(
        # Path to the entry point of the script (main module)
        'my_script.py',
        out_file=f,
        root_dir='.',
        strip_top_level=True  # Remove top-level directory from ZIP archive
    )
```

This command will create a standalone executable named `my_script.zip` that can be run without Python installed on the target system.

### Example 2: Executing an Executable

To execute the created executable:

```python
import subprocess

# Execute the created executable
subprocess.run(['./my_script.zip'])
```

This command will invoke the script embedded in `my_script.zip`.

### Example 3: Installing the Executable as a Command-Line Tool

You can install the executable as a system command by creating an alias or by adding the directory containing the executable to your PATH environment variable. For simplicity, let's assume you want to add the executable to a specific directory:

```python
import shutil
from pathlib import Path

# Specify the destination directory for the executable
destination = Path('/usr/local/bin')

# Ensure the destination exists
if not destination.exists():
    destination.mkdir(parents=True)

# Copy the executable from the zip file to the destination directory
shutil.copy('my_script.zip', destination / 'my_script')
```

Now, you can run `my_script` from anywhere in your system:

```bash
$ my_script
Hello, world!
```

### Example 4: Running a Script with Specific Python Interpreter

If you want to specify a particular Python interpreter when running the script, you can use the `-m` option with the `subprocess.run` function:

```python
import subprocess

# Run the script using a specific Python interpreter
subprocess.run(['python3', './my_script.zip'])
```

This command will ensure that the specified Python version is used to execute the script.

### Example 5: Managing Dependencies

If your application has dependencies, you can include them in the ZIP archive by adding them to the root directory of the ZIP file. For example, if `my_module.py` also depends on another module:

```python
# my_script.py
import my_module

def main():
    print("Hello, world!")
    my_module.main()

if __name__ == "__main__":
    main()
```

And include `my_module.py` in the ZIP file:

```python
import zipapp

with open('my_script.zip', 'wb') as f:
    z = zipapp.create_archive(
        'my_script.py',
        out_file=f,
        root_dir='.',
        strip_top_level=True,
        include=['my_module.py']  # Include additional files in the ZIP
    )
```

This approach allows you to bundle all necessary components into a single, portable executable.

### Example 6: Using `zipapp.run_script`

The `zipapp.run_script` function is another way to execute scripts directly from a zip archive without creating an executable file:

```python
import zipapp

# Run the script directly from the ZIP archive
zipapp.run_script(
    'my_script.zip',
    # Command-line arguments passed to the script
    ['arg1', 'arg2']
)
```

This command will execute `my_script.py` with the specified arguments.

These examples provide a comprehensive overview of how you can use the `zipapp` module to create, manage, and run standalone Python applications. You can modify these examples based on your specific requirements and project structure.
