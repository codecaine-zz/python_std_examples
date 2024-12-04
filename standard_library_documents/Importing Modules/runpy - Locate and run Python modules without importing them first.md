# runpy - Locate and run Python modules without importing them first

The `runpy` module in Python provides functions to locate and execute Python scripts or modules, similar to how you would use the `python -m` command from the command line. This is particularly useful for running standalone scripts that are not imported as modules into other programs.

Here are some code examples demonstrating how to use the `runpy` module:

### Example 1: Running a standalone Python script

Suppose you have a simple Python script named `my_script.py` with the following content:
```python
# my_script.py
print("Hello, from my_script!")
```

You can run this script using `runpy` like this:

```python
import runpy

# Run the standalone script
runpy.run_path('my_script.py')
```

### Example 2: Running a module with command-line arguments

If your script uses command-line arguments, you can pass them to `runpy` using the `args` parameter:

```python
import sys
import runpy

# Define the arguments to be passed to the script
args = ['my_script.py', '--arg1', 'value1']

# Run the module with command-line arguments
result = runpy.run_path('my_script.py', args=args)
print(result)
```

### Example 3: Running a module with custom sys.argv

You can also customize the `sys.argv` list before running the script:

```python
import sys
import runpy

# Original sys.argv
original_argv = sys.argv[:]

# Set new arguments for sys.argv
new_args = ['my_script.py', '--arg1', 'value1']

# Replace the original sys.argv with new ones
sys.argv = new_args

# Run the module
result = runpy.run_path('my_script.py')
print(result)

# Restore the original sys.argv
sys.argv = original_argv
```

### Example 4: Running a script in a different working directory

You can change the current working directory before running the script:

```python
import os
import runpy

# Original working directory
original_dir = os.getcwd()

# Set new working directory
new_dir = '/path/to/new/directory'
os.chdir(new_dir)

# Run the script
result = runpy.run_path('my_script.py')
print(result)

# Restore the original working directory
os.chdir(original_dir)
```

### Example 5: Running a module with custom environment variables

You can set custom environment variables before running the script:

```python
import os
import runpy

# Original environment variables
original_env = dict(os.environ)

# Set new environment variables
new_env = {'MY_VAR': 'value', 'OTHER_VAR': 'another_value'}
os.environ.update(new_env)

# Run the module
result = runpy.run_path('my_script.py')
print(result)

# Restore the original environment variables
os.environ.clear()
os.environ.update(original_env)
```

### Example 6: Running a module with custom import paths

You can specify additional directories to search for modules when running the script:

```python
import sys
import runpy

# Original import path
original_path = sys.path[:]

# Add new directory to the import path
new_dir = '/path/to/new/directory'
sys.path.append(new_dir)

# Run the module
result = runpy.run_path('my_script.py')
print(result)

# Restore the original import path
sys.path = original_path
```

These examples demonstrate various ways to use the `runpy` module to execute Python scripts and modules, providing flexibility for running standalone scripts, handling command-line arguments, customizing runtime environments, and more.
