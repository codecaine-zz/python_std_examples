# atexit - Exit handlers

The `atexit` module in Python provides a way to register functions that will be called when normal program termination occurs, typically upon exit. This is useful for cleanup tasks such as closing files or releasing resources.

Below are comprehensive code examples demonstrating various functionalities of the `atexit` module:

### 1. Basic Usage

The simplest use case involves registering a function to be called on program exit.

```python
import atexit

def cleanup_function():
    print("Cleanup function executed")

# Register the cleanup function
atexit.register(cleanup_function)

# Simulate program termination (e.g., by reaching the end of the script)
print("Program is about to terminate")
```

### 2. Multiple Handlers

You can register multiple functions that will be called in reverse order of registration.

```python
import atexit

def first_cleanup():
    print("First cleanup function executed")

def second_cleanup():
    print("Second cleanup function executed")

# Register multiple cleanup functions
atexit.register(first_cleanup)
atexit.register(second_cleanup)

# Simulate program termination
print("Program is about to terminate")
```

### 3. Handling Exceptions

If one of the cleanup functions raises an exception, it will be caught by Python's default exception handling mechanism.

```python
import atexit

def first_cleanup():
    print("First cleanup function executed")

def second_cleanup():
    raise Exception("Error in second cleanup")

# Register multiple cleanup functions
atexit.register(first_cleanup)
atexit.register(second_cleanup)

try:
    # Simulate program termination with an error
    print("Program is about to terminate")
except Exception as e:
    print(f"An error occurred: {e}")
```

### 4. Cleanup on Module Exit

You can use `atexit` in modules to ensure cleanup code runs when the module is unloaded.

```python
import atexit

def my_module_cleanup():
    print("Module cleanup function executed")

# Register a cleanup function for this module
atexit.register(my_module_cleanup)

def my_module_function():
    # Module-specific logic here
    print("Module function is running")

# Use the module
my_module_function()
```

### 5. Using `atexit` with Subprocesses

When working with subprocesses, you might want to ensure that cleanup actions are performed on both the parent and child processes.

```python
import atexit
import os
import sys
import subprocess

def parent_cleanup():
    print("Parent cleanup function executed")

def child_cleanup():
    print("Child cleanup function executed")

# Register cleanup functions for the parent and child processes
atexit.register(parent_cleanup)
atexit.register(child_cleanup)

# Create a new process
pid = os.fork()

if pid == 0:
    # This is the child process
    sys.exit(0)  # Terminate the child process
else:
    # This is the parent process
    print("Parent process is running")
```

### 6. Using `atexit` with Signals

You can use signals to trigger cleanup actions, such as when a program receives a termination signal.

```python
import atexit
import os
import signal

def cleanup_function():
    print("Cleanup function executed")

# Register the cleanup function
atexit.register(cleanup_function)

# Set up a signal handler for SIGTERM (kill -SIGTERM)
signal.signal(signal.SIGTERM, lambda signum, frame: cleanup_function())

print("Program is running and can be terminated with Ctrl+C")
try:
    while True:
        # Simulate long-running task
        pass
except KeyboardInterrupt:
    print("Termination signal received")
```

### 7. Using `atexit` with Threads

When using threads, you might want to ensure that cleanup actions are performed when all threads complete.

```python
import atexit
import threading
import time

def thread_cleanup():
    print("Thread cleanup function executed")

# Register the cleanup function
atexit.register(thread_cleanup)

def worker_thread(name):
    print(f"Thread {name} is running")
    time.sleep(2)
    print(f"Thread {name} is completed")

# Create and start multiple threads
threads = []
for i in range(3):
    thread = threading.Thread(target=worker_thread, args=(i,))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("All threads have completed")
```

### 8. Using `atexit` with Resource Management

You can use `atexit` to ensure that resources are properly released when the program terminates.

```python
import atexit
import tempfile

def cleanup_file():
    # Clean up any temporary files created by this module
    for filename in os.listdir(tempfile.gettempdir()):
        if filename.startswith("my_module_temp_"):
            os.remove(os.path.join(tempfile.gettempdir(), filename))

# Register the cleanup function
atexit.register(cleanup_file)

def my_module_function():
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp:
        print(f"Created temporary file: {temp.name}")

my_module_function()
print("Program is running")
```

These examples demonstrate various use cases for the `atexit` module, including basic cleanup, handling exceptions, and using `atexit` within modules and threads. By following these examples, you can effectively manage resources and ensure that your program performs necessary cleanup actions before termination.
