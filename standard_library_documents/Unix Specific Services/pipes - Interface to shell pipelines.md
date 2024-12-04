# pipes - Interface to shell pipelines

Below are comprehensive code examples for the `pipes` module in Python 3.12, along with explanations of each example:

### Example 1: Basic Pipelines

```python
import subprocess

# Create a pipe and connect it to a command
process = subprocess.Popen(['ls', '-l'], stdout=subprocess.PIPE)

# Read from the process's stdout
output, error = process.communicate()

# Decode the output from bytes to string
result = output.decode('utf-8')

print("Output:")
print(result)
```

**Explanation:**
This example demonstrates how to use the `subprocess` module to create a simple pipeline. It runs the `ls -l` command and captures its output. The `stdout=subprocess.PIPE` argument sets up the pipe, and `communicate()` reads from the process's standard output.

### Example 2: Multiple Commands in a Pipeline

```python
import subprocess

# Create a pipeline with two commands
process1 = subprocess.Popen(['ls', '-l'], stdout=subprocess.PIPE)
process2 = subprocess.Popen(['grep', 'lib'], stdin=process1.stdout, stdout=subprocess.PIPE)

# Read from the second process's stdout
output, error = process2.communicate()

# Decode the output from bytes to string
result = output.decode('utf-8')

print("Output:")
print(result)
```

**Explanation:**
This example shows how to create a more complex pipeline by connecting the standard output of one command to the input of another. The `grep` command filters lines containing "lib" based on the output from `ls -l`.

### Example 3: Redirecting Standard Input

```python
import subprocess

# Create a pipe and connect it to a command with input redirection
process = subprocess.Popen(['echo', 'Hello, World!'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

# Write to the process's stdin and read from stdout
output, error = process.communicate(input=b'Input for echo\n')

# Decode the output from bytes to string
result = output.decode('utf-8')

print("Output:")
print(result)
```

**Explanation:**
This example demonstrates how to use a pipe to redirect input to a command. The `echo` command is used to print "Hello, World!", and the input redirection is set up using `stdin=subprocess.PIPE`.

### Example 4: Handling Errors

```python
import subprocess

# Create a pipe and connect it to a command with error handling
process = subprocess.Popen(['ls', 'nonexistentfile'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

try:
    output, error = process.communicate()
except FileNotFoundError as e:
    print("Error:", str(e))
else:
    if process.returncode == 0:
        result = output.decode('utf-8')
        print("Output:")
        print(result)
```

**Explanation:**
This example shows how to handle errors gracefully using a try-except block. It attempts to list a non-existent file and catches `FileNotFoundError` if the operation fails.

### Example 5: Using `subprocess.run()`

```python
import subprocess

# Create a pipe and connect it to a command using subprocess.run()
result = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE, check=True)

# Decode the output from bytes to string
output = result.stdout.decode('utf-8')

print("Output:")
print(output)
```

**Explanation:**
This example demonstrates how to use `subprocess.run()`, which provides a more user-friendly interface for running commands. The `check=True` argument ensures that a `CalledProcessError` is raised if the command returns a non-zero exit status.

### Example 6: Using `subprocess.Popen()` with Multiple Arguments

```python
import subprocess

# Create a pipe and connect it to a command with multiple arguments
process = subprocess.Popen(['echo', 'Hello,', '"World!"'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Read from the process's stdout and stderr
output, error = process.communicate()

# Decode the output and error from bytes to string
result = output.decode('utf-8')
error_message = error.decode('utf-8')

print("Output:")
print(result)
print("\nError:")
print(error_message)
```

**Explanation:**
This example shows how to use `subprocess.Popen()` with multiple arguments, including a quoted string, which is useful for handling special characters or strings with spaces.

These examples cover basic and advanced uses of the `pipes` module, demonstrating how to create and manage pipelines in Python using subprocesses.
