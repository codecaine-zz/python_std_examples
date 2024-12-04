# venv — Creation of virtual environments

**Creating Virtual Environments with Python's `venv` Module**

The `venv` module is part of Python's standard library, which allows you to create isolated Python environments for your projects.

### Example Usage:

```python
import venv

# Create a new virtual environment in the current directory
venv.create('myenv')

# Activate the virtual environment (on Linux/Mac)
# source myenv/bin/activate

# Deactivate the virtual environment
# deactivate

# Get the path of the virtual environment
env_path = venv.create('myenv').location

print(env_path)  # Output: /path/to/myenv

# Get a list of all activated environments
import os
activated_envs = [env_path for env_path in os.environ['PATH'].split(':') if os.path.exists(env_path)]
print(activated_envs)
```

### Creating Virtual Environments with `venv.create()`:

```python
import venv

# Create a new virtual environment with the given name
env = venv.create('myenv')

# Set the Python interpreter to use in the virtual environment
env.python_interpreter = '/usr/bin/python3.9'

# Set the Python version to use in the virtual environment
env.python_version = '3.9'

# Get the path of the virtual environment
env_path = env.location

print(env_path)  # Output: /path/to/myenv

# Deactivate the virtual environment
env.deactivate()
```

### Activating and Deactivating Virtual Environments:

```python
import venv
import os

# Activate the virtual environment
if 'myenv' in os.environ.get('PATH', '').split(':'):
    print("Virtual environment is already activated.")
else:
    # source myenv/bin/activate (on Linux/Mac)
    os.system(f'bash -c "source {venv.create("myenv").location}/bin/activate"')

# Deactivate the virtual environment
os.system('deactivate')
```

### Getting Information About Virtual Environments:

```python
import venv

# Get a list of all activated environments
activated_envs = [env.location for env in venv.create('myenv').subpids()]
print(activated_envs)

# Get the number of subpids (i.e., child processes) in the virtual environment
num_subpids = len([pid for pid in venv.create('myenv').subpids() if pid])
print(num_subpids)
```

### Deleting Virtual Environments:

```python
import venv

# Delete the virtual environment with the given name
venv.create('myenv').delete()

# Check if the virtual environment has been deleted
if not os.path.exists(venv.create('myenv').location):
    print("Virtual environment has been deleted.")
```

Note: Make sure to run these commands in a terminal or command prompt, and that you have the necessary permissions to delete files and directories.
