# signal — Set handlers for asynchronous events

**Signal Module Code Generation**
=====================================

The `signal` module provides an interface for setting up signal handlers, which are functions that will be executed in response to specific system signals.

### Importing Signal Module
```python
import signal
```

### Setting Up a Default Handler for SIGINT (Interrupt)
--------------------------------------------------------

When the program receives a SIGINT signal, Python normally terminates. We can set a handler function to catch this signal and perform an alternative action.
```python
def default_handler(sig, frame):
    """Default handler function for SIGINT signal."""
    print("Caught SIGINT signal. Exiting...")
    # Add code here that you want to execute instead of exiting

# Register the default handler with Python's signal module
signal.signal(signal.SIGINT, default_handler)
```

### Setting Up a Custom Handler for SIGALRM (Alarm)
----------------------------------------------------

We can also set a custom handler function to be executed when the alarm timer expires.
```python
import time

def alarm_handler(signum, frame):
    """Custom handler function for SIGALRM signal."""
    print("Alarm went off!")
    # Add code here that you want to execute when the alarm timer expires
    signal.alrm(0)  # Cancel the alarm

# Set up an alarm after 5 seconds
signal.alarm(5)

# Register the custom handler with Python's signal module
signal.signal(signal.SIGALRM, alarm_handler)
```

### Deregistering a Signal Handler
---------------------------------

When we're done with a signal handler, we should deregister it to prevent memory leaks.
```python
def clean_up():
    """Deregister the default handler for SIGINT signal."""
    signal.signal(signal.SIGINT, signal.SIG_DFL)  # Reset to default behavior

# Call the clean-up function when your program exits
import atexit
atexit.register(clean_up)
```

### Example Use Cases
---------------------

*   Handling system signals in a multithreaded application:
    ```python
import threading
import time

def signal_handler(sig, frame):
    print("Caught", sig.name, "signal. Exiting...")

# Register the handler with Python's signal module
signal.signal(signal.SIGINT, signal_handler)

def worker():
    while True:
        # Code that might raise a SIGINT signal
        time.sleep(1)

thread = threading.Thread(target=worker)
thread.start()
```

*   Implementing an alarm timer in a long-running task:
    ```python
import signal

def long_task():
    try:
        # Long-running task code here...
        while True:
            pass
    except KeyboardInterrupt:
        print("Caught SIGINT signal. Canceling...")
        return False

# Set up an alarm after 10 seconds
signal.alarm(10)

if not long_task():
    print("Task was interrupted by SIGINT signal")
```
