# signal - Set handlers for asynchronous events
## Table of Contents

1. [Example 1: Handling SIGINT (Ctrl+C)](#example-1-handling-sigint-ctrlc)
2. [Example 2: Handling SIGHUP](#example-2-handling-sighup)
3. [Example 3: Sending Signals to a Process](#example-3-sending-signals-to-a-process)
4. [Example 4: Handling Signals in a Multi-Threaded Application](#example-4-handling-signals-in-a-multi-threaded-application)
5. [Example 5: Handling Signals with a Custom Signal Class](#example-5-handling-signals-with-a-custom-signal-class)



The `signal` module in Python provides a way to handle signals raised by the operating system, such as SIGINT (CTRL+C) or SIGHUP (hangup). These signals can be used to interrupt running processes, request termination, or perform cleanup actions before exiting.

Here are comprehensive examples of how to use the `signal` module:

### Example 1: Handling SIGINT (Ctrl+C)

```python
import signal

def handle_sigint(signum, frame):
    print("Received SIGINT (CTRL+C), cleaning up...")
    # Perform any necessary cleanup operations here
    # For example, closing file handles, releasing resources, etc.

# Register the handler for SIGINT
signal.signal(signal.SIGINT, handle_sigint)

print("Press Ctrl+C to send a SIGINT signal.")
input()  # This will block until the user presses CTRL+C
```

### Example 2: Handling SIGHUP

```python
import signal

def handle_sighup(signum, frame):
    print("Received SIGHUP (hangup), performing graceful termination...")
    # Perform any necessary shutdown or cleanup operations here
    # For example, saving data to a file, releasing connections, etc.

# Register the handler for SIGHUP
signal.signal(signal.SIGHUP, handle_sighup)

print("This program will continue running until you terminate it manually.")
input()  # This will block until the user terminates the program
```

### Example 3: Sending Signals to a Process

You can send signals to another process using the `os.kill()` function from the `os` module. Here's an example:

```python
import os
import signal

# Function to simulate a simple server that listens for SIGINT and prints messages
def server_process():
    while True:
        try:
            print("Server is running...")
            # Simulate some work
            import time
            time.sleep(2)
        except KeyboardInterrupt:
            print("Server received SIGINT, stopping gracefully.")
            break

# Start the server process in a separate thread or process
import threading
server_thread = threading.Thread(target=server_process)
server_thread.start()

# Function to send SIGINT to the server process
def send_sigint_to_server():
    try:
        # Find the process ID of the server thread
        server_pid = os.getpid(server_thread.ident)
        
        # Send SIGINT to the server process
        print(f"Sending SIGINT to PID {server_pid}")
        os.kill(server_pid, signal.SIGINT)
    except OSError as e:
        print(f"Error sending SIGINT: {e}")

# Simulate a user pressing CTRL+C on the server
send_sigint_to_server()

# Wait for the server process to finish
server_thread.join()
```

### Example 4: Handling Signals in a Multi-Threaded Application

In a multi-threaded application, you can handle signals differently depending on whether they should be propagated to all threads or only to the main thread.

```python
import signal
import threading

def handler(signum, frame):
    print(f"Received signal {signum}, handling it in the main thread.")

# Register the handler for SIGINT
signal.signal(signal.SIGINT, handler)

def worker_thread():
    try:
        while True:
            print("Worker thread is running...")
            # Simulate some work
            import time
            time.sleep(1)
    except KeyboardInterrupt:
        print("Worker thread received SIGINT, stopping gracefully.")

# Create and start the worker thread
worker_thread = threading.Thread(target=worker_thread)
worker_thread.start()

input()  # This will block until the user presses CTRL+C

print("Main thread is handling the signal.")
```

### Example 5: Handling Signals with a Custom Signal Class

You can create a custom class to manage signal handlers more elegantly:

```python
class SignalManager:
    def __init__(self):
        self.handlers = {}

    def register(self, signum, handler):
        if isinstance(signum, int) and callable(handler):
            self.handlers[signum] = handler
            signal.signal(signum, self._handler)
        else:
            raise ValueError("Signum must be an integer and handler must be a callable function.")

    def _handler(self, signum, frame):
        if signum in self.handlers:
            self.handlers[signum](signum, frame)

# Example usage
signal_manager = SignalManager()
def custom_handler(signum, frame):
    print(f"Custom handler for signal {signum}")

signal_manager.register(signal.SIGINT, custom_handler)
print("Press Ctrl+C to send a SIGINT signal.")
input()  # This will block until the user presses CTRL+C
```

These examples demonstrate various ways to handle signals in Python using the `signal` module. Each example includes comments explaining key parts of the code, ensuring clarity and ease of understanding for developers.
