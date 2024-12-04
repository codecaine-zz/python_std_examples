# venv - Creation of virtual environments

Creating a virtual environment in Python using `venv` is a straightforward process that allows you to manage dependencies for different projects independently without affecting each other. Below are comprehensive examples of how to use the `venv` module, including comments explaining each step.

### Example 1: Creating a Virtual Environment Manually

```python
import venv

# Specify the path where the virtual environment will be created
venv_path = '/path/to/your/project/env'

# Create the virtual environment
venv.create(venv_path)

print(f"Virtual environment created at {venv_path}")
```

### Example 2: Activating a Virtual Environment (on Windows)

```python
import subprocess

# Specify the path to the virtual environment's activate script
activate_script = f"{venv_path}\\Scripts\\activate"

# Run the activation command using subprocess
subprocess.run([activate_script])

print("Virtual environment activated. You can now use 'pip' and other commands.")
```

### Example 3: Activating a Virtual Environment (on macOS/Linux)

```python
import subprocess

# Specify the path to the virtual environment's activate script
activate_script = f"{venv_path}/bin/activate"

# Run the activation command using subprocess
subprocess.run(['source', activate_script], shell=True)

print("Virtual environment activated. You can now use 'pip' and other commands.")
```

### Example 4: Creating a Virtual Environment Automatically with `create` Method

```python
import venv

# Specify the path where the virtual environment will be created
venv_path = '/path/to/your/project/env'

# Create the virtual environment automatically
with venv.create(venv_path, with_pip=True) as env:
    print(f"Virtual environment created at {venv_path}")
```

### Example 5: Deactivating a Virtual Environment

```python
import sys

def deactivate():
    # Check if we are in an activated virtual environment
    if 'VIRTUAL_ENV' in os.environ:
        # Remove the VIRTUAL_ENV variable from the environment
        del os.environ['VIRTUAL_ENV']
        
        # Reassign sys.prefix and sys.executable to remove reference to the virtual environment
        sys.prefix = '/usr'  # or whatever is your default prefix
        sys.executable = '/usr/bin/python3.10'  # or whatever is your default Python executable
        
        print("Virtual environment deactivated.")
    else:
        print("Not in an activated virtual environment.")

# Call the deactivate function to exit the virtual environment
deactivate()
```

### Example 6: Using `pip` within a Virtual Environment

```python
import subprocess

# Specify the path to the virtual environment's bin directory
bin_dir = f"{venv_path}\\Scripts"

# Install a package using pip
subprocess.run([f'{bin_dir}\\pip', 'install', 'requests'])

print("Requests package installed in the virtual environment.")
```

### Example 7: Listing Installed Packages

```python
import subprocess

# Specify the path to the virtual environment's bin directory
bin_dir = f"{venv_path}\\Scripts"

# List all installed packages using pip list
subprocess.run([f'{bin_dir}\\pip', 'list'])

print("Installed packages listed.")
```

### Example 8: Checking Python Version in a Virtual Environment

```python
import sys

# Check the Python version within the virtual environment
if 'VIRTUAL_ENV' in os.environ:
    print(f"Python version in the virtual environment is {sys.version}")
else:
    print("Not in an activated virtual environment.")

# Output: Python version in the virtual environment is 3.12.x (or whatever your installed version is)
```

These examples demonstrate how to create, activate, and manage a virtual environment using Python's `venv` module. Each example includes comments explaining the purpose of the code snippet and how it interacts with the virtual environment.
