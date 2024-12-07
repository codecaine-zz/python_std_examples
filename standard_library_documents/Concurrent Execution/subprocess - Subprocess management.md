# subprocess - Subprocess management

The `subprocess` module in Python provides a way to spawn new processes, connect to their input/output/error pipes, and obtain their return codes. Below are comprehensive examples demonstrating various functionalities of the `subprocess` module. These examples are designed to be clear, concise, and suitable for inclusion in official documentation.

### Example 1: Running an External Command

```python
import subprocess

# Example command to run 'ls -l'
result = subprocess.run(['ls', '-l'], capture_output=True, text=True)

# Print the output of the command
print("Command Output:")
print(result.stdout)

# Check if the command was successful
if result.returncode == 0:
    print("Command executed successfully.")
else:
    print(f"Error: {result.stderr}")
```

**Explanation**: This example demonstrates how to use `subprocess.run()` to execute an external command. The `['ls', '-l']` list specifies the command and its arguments. The `capture_output=True` argument captures both standard output and error, and `text=True` ensures that the output is returned as a string instead of bytes. The result is then printed, and the script checks if the command was successful.

### Example 2: Running a Command in a Separate Process

```python
import subprocess

# Create a subprocess object to run 'echo Hello'
process = subprocess.Popen(['echo', 'Hello'], stdout=subprocess.PIPE)

# Read the output from the subprocess
output, _ = process.communicate()

# Print the output of the command
print("Command Output:")
print(output.decode('utf-8'))

# Check if the command was successful
if process.returncode == 0:
    print("Command executed successfully.")
else:
    print(f"Error: {process.stderr}")
```

**Explanation**: This example shows how to use `subprocess.Popen()` to run a command in a separate process. The `stdout=subprocess.PIPE` argument allows reading the output of the command. The `communicate()` method is used to get both the standard output and error from the subprocess. The script decodes the output from bytes to a string before printing it.

### Example 3: Handling Subprocess Input

```python
import subprocess

# Create a subprocess object to run 'cat' with input piped in
process = subprocess.Popen(['cat'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

# Write input to the subprocess
input_data = "Hello, World!\n"
process.stdin.write(input_data.encode('utf-8'))

# Read the output from the subprocess
output, _ = process.communicate()

# Close the stdin after communicate
process.stdin.close()

# Print the output of the command
print("Command Output:")
print(output.decode('utf-8'))

# Check if the command was successful
if process.returncode == 0:
    print("Command executed successfully.")
else:
    print(f"Error: {process.stderr}")
```

**Explanation**: This example demonstrates how to write input to a subprocess. The `stdin=subprocess.PIPE` argument allows writing input to the subprocess, and `encode('utf-8')` is used to convert the string to bytes before sending it to the process. The script reads the output from the subprocess and checks if the command was successful.

### Example 4: Running Commands with Environment Variables

```python
import subprocess

# Define environment variables
env = {
    'PATH': '/usr/local/bin',
    'MY_VAR': 'my_value'
}

# Run a command with specified environment variables
result = subprocess.run(['/bin/sh', '-c', 'echo $MY_VAR'], env=env, capture_output=True, text=True)

# Print the output of the command
print("Command Output:")
print(result.stdout)

# Check if the command was successful
if result.returncode == 0:
    print("Command executed successfully.")
else:
    print(f"Error: {result.stderr}")
```

**Explanation**: This example shows how to run a command with specified environment variables. The `env` dictionary is used to set environment variables for the subprocess. The `$MY_VAR` in the command string is replaced with its value from the environment.

### Example 5: Running Commands in Parallel

```python
import subprocess
import time

# List of commands to run in parallel
commands = [
    ['echo', 'Command1'],
    ['sleep', '2'],
    ['echo', 'Command3']
]

# Create and start processes for each command
processes = []
for cmd in commands:
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    processes.append(process)

# Wait for all processes to complete
for p in processes:
    output, _ = p.communicate()
    print(f"Output of {p.args}:")
    print(output.decode('utf-8'))
    print("Command executed successfully." if p.returncode == 0 else f"Error: {p.stderr}")

# Wait for all subprocesses to finish
for p in processes:
    p.wait()
```

**Explanation**: This example demonstrates how to run multiple commands in parallel using the `subprocess` module. Each command is executed in a separate process, and their outputs are captured. The script waits for all processes to complete before proceeding.

### Example 6: Using `check_output()` for Simple Operations

```python
import subprocess

# Use check_output() to run a simple command and capture its output
output = subprocess.check_output(['uname', '-a'], text=True)

# Print the output of the command
print("Output:")
print(output)

# Check if the command was successful
if subprocess.call(['uname', '-a']) == 0:
    print("Command executed successfully.")
else:
    print("Error: Command execution failed.")
```

**Explanation**: This example shows how to use `subprocess.check_output()` to run a simple command and capture its output. The function raises an exception if the command fails, making it convenient for checking the success of operations.

### Example 7: Using `run()` with Timeout

```python
import subprocess
import time

# Initialize the result variable
result = None

# Run a command with a timeout
try:
    result = subprocess.run(['sleep', '3'], timeout=2, capture_output=True, text=True)
except subprocess.TimeoutExpired as e:
    print("Command timed out.")
else:
    # Print the output of the command
    print("Command Output:")
    print(result.stdout)

# Check if the command was successful
if result and result.returncode == 0:
    print("Command executed successfully.")
else:
    print(f"Error: {result.stderr if result else 'No result available.'}")
```

**Explanation**: This example demonstrates how to run a command with a timeout using `subprocess.run()`. If the command takes longer than the specified timeout, it raises a `TimeoutExpired` exception. The script handles this exception and prints an appropriate message.

### Example 8: Using `run()` with Custom Signal Handling

```python
import subprocess
import os

# Run a command with custom signal handling
try:
    result = subprocess.run(['sleep', '10'], preexec_fn=os.setsid, capture_output=True, text=True)
except subprocess.TimeoutExpired as e:
    # Send the SIGTERM signal to the process group
    os.killpg(os.getpgid(result.pid), signal.SIGTERM)
    print("Command timed out. Sent SIGTERM.")
else:
    # Print the output of the command
    print("Command Output:")
    print(result.stdout)

# Check if the command was successful
if result.returncode == 0:
    print("Command executed successfully.")
else:
    print(f"Error: {result.stderr}")
```

**Explanation**: This example shows how to run a command with custom signal handling using `subprocess.run()`. The `preexec_fn=os.setsid` argument creates a new process group, and the script sends the SIGTERM signal to the entire process group if the command times out.

### Example 9: Using `run()` with Background Execution

```python
import subprocess
import time

# Run a command in the background
process = subprocess.Popen(['sleep', '5'], stdout=subprocess.PIPE)

# Wait for the process to complete
output, _ = process.communicate()

# Print the output of the command
print("Command Output:")
print(output.decode('utf-8'))

# Check if the command was successful
if process.returncode == 0:
    print("Command executed successfully.")
else:
    print(f"Error: {process.stderr}")
```

**Explanation**: This example demonstrates how to run a command in the background using `subprocess.Popen()`. The process is executed without waiting for it to complete, and the output is captured using `communicate()`.

### Example 10: Using `run()` with Multiple Arguments

```python
import subprocess

# Run a command with multiple arguments
result = subprocess.run(['echo', 'Hello', 'World'], capture_output=True, text=True)

# Print the output of the command
print("Command Output:")
print(result.stdout)

# Check if the command was successful
if result.returncode == 0:
    print("Command executed successfully.")
else:
    print(f"Error: {result.stderr}")
```

**Explanation**: This example shows how to run a command with multiple arguments using `subprocess.run()`. The list `['echo', 'Hello', 'World']` specifies the command and its arguments.

These examples cover various aspects of the `subprocess` module, including running commands, handling input/output, environment variables, parallel execution, error handling, and more. Each example is designed to be clear and concise, making it suitable for inclusion in a broader discussion or usage guide.
