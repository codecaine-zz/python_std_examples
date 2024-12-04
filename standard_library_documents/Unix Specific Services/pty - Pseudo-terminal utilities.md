# pty - Pseudo-terminal utilities

The `pty` module in Python provides a way to create pseudoterminal (pseudo-TTY) devices, which are used to simulate a terminal environment in applications that need console input/output. This is particularly useful for creating interactive programs or services that require real-time access to the user's console.

Here are comprehensive examples for various functionalities of the `pty` module:

### Example 1: Simple Pseudoterminal Creation and Usage

```python
import pty
import os

# Define a callback function to handle input/output from the pseudo-terminal
def process_input(data):
    print(f"Received data: {data.decode()}")
    return "Processed Output"

# Open a pseudoterminal
master_fd, slave_fd = pty.openpty()

try:
    # Create a new process using os.fork()
    pid = os.fork()
    
    if pid == 0:
        # Child process: replace the terminal with the pseudo-terminal
        os.setsid()
        os.execvp('bash', ['bash'])
    else:
        # Parent process: communicate with the child through the pseudo-terminal
        while True:
            # Read data from the pseudo-terminal
            input_data = os.read(master_fd, 1024)
            
            if not input_data:
                break
            
            # Process the input and send the output back to the pseudo-terminal
            processed_output = process_input(input_data)
            os.write(master_fd, processed_output.encode())
finally:
    # Ensure the pseudoterminal is closed after usage
    os.close(master_fd)
```

### Example 2: Using `pty.spawn` for Simple Process Execution

The `pty.spawn` function is a convenience wrapper that opens a pseudo-terminal and runs a specified command in it.

```python
import pty
import os

# Define a callback function to handle input/output from the pseudo-terminal
def process_input(data):
    print(f"Received data: {data.decode()}")
    return "Processed Output"

# Open a pseudoterminal
master_fd, slave_fd = pty.openpty()

try:
    # Use pty.spawn to execute 'bash' in the pseudo-terminal
    pid = pty.spawn('bash', stdin=slave_fd, stdout=slave_fd, stderr=slave_fd)
    
    if pid == 0:
        # Child process: replace the terminal with the pseudo-terminal
        os.setsid()
        os.execvp('bash', ['bash'])
    else:
        # Parent process: communicate with the child through the pseudo-terminal
        while True:
            # Read data from the pseudo-terminal
            input_data = os.read(master_fd, 1024)
            
            if not input_data:
                break
            
            # Process the input and send the output back to the pseudo-terminal
            processed_output = process_input(input_data)
            os.write(master_fd, processed_output.encode())
finally:
    # Ensure the pseudoterminal is closed after usage
    os.close(master_fd)
```

### Example 3: Reading Output from a Pseudoterminal

This example shows how to read output from the pseudo-terminal without blocking.

```python
import pty
import os

# Open a pseudoterminal
master_fd, slave_fd = pty.openpty()

try:
    # Use pty.spawn to execute 'sleep 5' in the pseudo-terminal
    pid = pty.spawn('sleep', '5', stdin=slave_fd, stdout=slave_fd, stderr=slave_fd)
    
    if pid == 0:
        # Child process: replace the terminal with the pseudo-terminal
        os.setsid()
        os.execvp('sleep', ['sleep', '5'])
    else:
        # Parent process: read output from the pseudo-terminal without blocking
        while True:
            try:
                # Read data from the pseudo-terminal
                input_data = os.read(master_fd, 1024)
                
                if not input_data:
                    break
                
                print(f"Received output: {input_data.decode()}")
            except OSError as e:
                if e.errno == errno.EAGAIN:
                    continue
                else:
                    raise

finally:
    # Ensure the pseudoterminal is closed after usage
    os.close(master_fd)
```

### Example 4: Handling Input with `pty.master_read` and `pty.master_write`

This example demonstrates how to manually read and write data to a pseudo-terminal.

```python
import pty
import os

# Open a pseudoterminal
master_fd, slave_fd = pty.openpty()

try:
    # Use pty.spawn to execute 'sleep 5' in the pseudo-terminal
    pid = pty.spawn('sleep', '5', stdin=slave_fd, stdout=slave_fd, stderr=slave_fd)
    
    if pid == 0:
        # Child process: replace the terminal with the pseudo-terminal
        os.setsid()
        os.execvp('sleep', ['sleep', '5'])
    else:
        # Parent process: manually read and write data to the pseudo-terminal
        while True:
            try:
                # Read input from the user
                user_input = input("Enter command: ")
                
                if user_input == "exit":
                    break
                
                # Write the user's input to the pseudo-terminal
                os.write(master_fd, user_input.encode())
                
                # Read output from the pseudo-terminal
                output = os.read(master_fd, 1024)
                
                if not output:
                    continue
                
                print(f"Output: {output.decode()}")
            except KeyboardInterrupt:
                break

finally:
    # Ensure the pseudoterminal is closed after usage
    os.close(master_fd)
```

### Example 5: Using `pty.fork` for a Child Process with Pseudo-terminal

This example shows how to create a child process using `pty.fork` and handle input/output through a pseudo-terminal.

```python
import pty
import os

# Define a callback function to handle input/output from the pseudo-terminal
def process_input(data):
    print(f"Received data: {data.decode()}")
    return "Processed Output"

# Open a pseudoterminal
master_fd, slave_fd = pty.openpty()

try:
    # Fork a new process
    pid = os.fork()
    
    if pid == 0:
        # Child process: replace the terminal with the pseudo-terminal
        os.setsid()
        os.dup2(slave_fd, 0)
        os.dup2(slave_fd, 1)
        os.dup2(slave_fd, 2)
        os.close(master_fd)
        os.execvp('bash', ['bash'])
    else:
        # Parent process: communicate with the child through the pseudo-terminal
        while True:
            try:
                # Read input from the user
                user_input = input("Enter command: ")
                
                if user_input == "exit":
                    break
                
                # Write the user's input to the pseudo-terminal
                os.write(master_fd, user_input.encode())
                
                # Read output from the pseudo-terminal
                output = os.read(master_fd, 1024)
                
                if not output:
                    continue
                
                print(f"Output: {output.decode()}")
            except KeyboardInterrupt:
                break

finally:
    # Ensure the pseudoterminal is closed after usage
    os.close(master_fd)
```

These examples cover various aspects of using the `pty` module, from simple terminal simulation to more complex processes involving input/output handling.
