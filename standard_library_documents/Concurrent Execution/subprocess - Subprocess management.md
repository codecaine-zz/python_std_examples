# subprocess — Subprocess management

**Subprocess Management**
==========================

The `subprocess` module allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes.

### Functions

#### `Popen([b'command', *args], **kwargs)`

Creates a new process.

*   `command`: A string containing the program name or a bytes object.
*   `args`: Variable number of arguments to pass to the command.
*   `stdin`, `stdout`, `stderr`, `shell`: Optional keyword arguments that control how the child's input/output/error pipes are used. Default values are:
    *   `stdin`: Opened from system's standard input (`sys.stdin`).
    *   `stdout`: Opened to system's standard output (`sys.stdout`).
    *   `stderr`: Opened to system's standard error (`sys.stderr`).
    *   `shell`: Use a new shell to execute the command. Default is `False`.

```python
import subprocess

# Create a new process that runs the 'ls' command with the '-l' option.
process = subprocess.Popen(['ls', '-l'])

# Wait for the process to finish and print its return code.
print(process.wait())  # Output: 0 (Successful)

```

#### `run(command, *, stdin=None, stdout=None, stderr=None, shell=False, check=True)`

Run a command in a new process.

*   `command`: A string containing the program name or a bytes object.
*   `stdin`, `stdout`, `stderr`: Optional keyword arguments that control how the child's input/output/error pipes are used. Default values are:
    *   `stdin`: Opened from system's standard input (`sys.stdin`).
    *   `stdout`: Opened to system's standard output (`sys.stdout`).
    *   `stderr`: Opened to system's standard error (`sys.stderr`).
*   `shell`: Use a new shell to execute the command. Default is `False`.
*   `check`: Whether to raise an exception if the return code of the process is non-zero. Default is `True`.

```python
import subprocess

# Run the 'ls' command with the '-l' option.
result = subprocess.run(['ls', '-l'], check=True)

# Print whether the operation was successful.
print(result.success)  # Output: True

```

#### `Popen(*args, **kwargs) -> Popen`

Create a new process.

*   `args`: Variable number of arguments to pass to the command. The first argument must be the program name or a bytes object.
*   `kwargs`: Keyword arguments that control how the child's input/output/error pipes are used. Default values are:
    *   `stdin`: Opened from system's standard input (`sys.stdin`).
    *   `stdout`: Opened to system's standard output (`sys.stdout`).
    *   `stderr`: Opened to system's standard error (`sys.stderr`).

```python
import subprocess

# Create a new process that runs the 'ls' command with the '-l' option.
process = subprocess.Popen(['ls', '-l'])

# Wait for the process to finish and print its return code.
print(process.wait())  # Output: 0 (Successful)

```

### Classes

#### `Popen([b'command', *args], **kwargs)`

Create a new process.

*   `command`: A string containing the program name or a bytes object.
*   `args`: Variable number of arguments to pass to the command.
*   `stdin`, `stdout`, `stderr`, `shell`: Optional keyword arguments that control how the child's input/output/error pipes are used. Default values are:
    *   `stdin`: Opened from system's standard input (`sys.stdin`).
    *   `stdout`: Opened to system's standard output (`sys.stdout`).
    *   `stderr`: Opened to system's standard error (`sys.stderr`).
    *   `shell`: Use a new shell to execute the command. Default is `False`.

```python
import subprocess

# Create a new process that runs the 'ls' command with the '-l' option.
process = subprocess.Popen(['ls', '-l'])

# Wait for the process to finish and print its return code.
print(process.wait())  # Output: 0 (Successful)

```

#### `run(command, *, stdin=None, stdout=None, stderr=None, shell=False, check=True)`

Run a command in a new process.

*   `command`: A string containing the program name or a bytes object.
*   `stdin`, `stdout`, `stderr`: Optional keyword arguments that control how the child's input/output/error pipes are used. Default values are:
    *   `stdin`: Opened from system's standard input (`sys.stdin`).
    *   `stdout`: Opened to system's standard output (`sys.stdout`).
    *   `stderr`: Opened to system's standard error (`sys.stderr`).
*   `shell`: Use a new shell to execute the command. Default is `False`.
*   `check`: Whether to raise an exception if the return code of the process is non-zero. Default is `True`.

```python
import subprocess

# Run the 'ls' command with the '-l' option.
result = subprocess.run(['ls', '-l'], check=True)

# Print whether the operation was successful.
print(result.success)  # Output: True

```

#### `Popen(*args, **kwargs) -> Popen`

Create a new process.

*   `args`: Variable number of arguments to pass to the command. The first argument must be the program name or a bytes object.
*   `kwargs`: Keyword arguments that control how the child's input/output/error pipes are used. Default values are:
    *   `stdin`: Opened from system's standard input (`sys.stdin`).
    *   `stdout`: Opened to system's standard output (`sys.stdout`).
    *   `stderr`: Opened to system's standard error (`sys.stderr`).

```python
import subprocess

# Create a new process that runs the 'ls' command with the '-l' option.
process = subprocess.Popen(['ls', '-l'])

# Wait for the process to finish and print its return code.
print(process.wait())  # Output: 0 (Successful)

```

### Example Usage

```python
import subprocess

def run_command(command, check=True):
    """
    Run a command in a new process.

    Args:
        command (str): The command to run.
        check (bool): Whether to raise an exception if the return code is non-zero. Defaults to True.

    Returns:
        tuple: A tuple containing the return code and output of the process.
    """
    result = subprocess.run(command, check=check)
    return result.returncode, result.stdout.decode()

def run_process(process):
    """
    Run a new process that runs the 'ls' command with the '-l' option.

    Args:
        process (Popen): The process to run.

    Returns:
        int: The return code of the process.
    """
    return process.wait()

if __name__ == "__main__":
    # Run the 'ls' command with the '-l' option.
    command = ['ls', '-l']
    check = True

    # Run the command and print its return code.
    return_code, output = run_command(command, check=check)
    print(f"Return Code: {return_code}")
    print(f"Output:\n{output}")

    # Create a new process that runs the 'ls' command with the '-l' option.
    process = subprocess.Popen(['ls', '-l'])

    # Wait for the process to finish and print its return code.
    return_code = run_process(process)
    print(f"Return Code: {return_code}")
```

This example demonstrates how to use the `subprocess` module to run a command in a new process, wait for its completion, and retrieve its return code. The `run_command` function runs a command and returns its return code and output. The `run_process` function runs a new process that runs the 'ls' command with the '-l' option and waits for it to finish.

**Note:** This is not an exhaustive guide to the `subprocess` module, but rather a collection of examples demonstrating how to use some of its most commonly used functions.
