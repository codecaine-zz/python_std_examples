# _thread — Low-level threading API

**Thread Module**
================

The `_thread` module provides an interface for creating and managing threads.

### Importing the Module

```python
import _thread
```

### Creating Threads

You can create a new thread using the `Thread` class from the `_thread` module:

```python
# Create a new thread that runs a function with arguments
def worker(name):
    print(f"Hello, {name}!")

_thread.start_new_thread(worker, ("Alice",))
```

This will start a new thread that prints "Hello, Alice!".

### Daemon Threads

You can set a daemon thread to exit when the main program exits using the `setDaemon` method:

```python
import _thread

def worker():
    print("Worker thread started")

_thread.start_new_thread(worker)
_thread.setDaemon(True)  # Set as daemon thread
```

### Thread Names

You can give a name to a thread using the `name` attribute of the `Thread` object:

```python
import _thread

class MyThread(_thread.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

_thread.start_new_thread(MyThread("Worker").start)
```

### Joining Threads

You can join a thread using the `join` method of the `Thread` object:

```python
import _thread

def worker():
    for i in range(5):
        print(i)

t = _thread.Thread(target=worker)
t.start()
t.join()  # Wait for thread to finish
```

### Stopping Threads

You can stop a thread using the `_stop` method of the `Thread` object:

```python
import _thread

def worker():
    while True:
        print("Worker thread running")

t = _thread.Thread(target=worker)
t.start()
# t._stop()  # This will raise an AttributeError, as this method is private.
```

Note that trying to access the `_stop` method directly raises an `AttributeError`. To stop a thread, you can use other methods, such as using a condition variable or threading event.

### Threading Events

You can create a threading event using the `_Event` class from the `_thread` module:

```python
import _thread

def worker():
    print("Worker waiting for signal")
    e.wait()  # Wait until signal is received
    print("Worker started")

e = _thread.Event()
t = _thread.Thread(target=worker)
t.start()
e.set()  # Send the signal
```

Note that the `_Event` class uses a single lock, so only one thread can access it at a time.

### Threading Locks

You can create a threading lock using the `_Lock` class from the `_thread` module:

```python
import _thread

lock = _thread.Lock()

def worker():
    print("Worker waiting to acquire lock")
    lock.acquire()  # Acquire lock
    try:
        # Critical section code here
        print("Worker holding lock")
    finally:
        lock.release()  # Release lock

t = _thread.Thread(target=worker)
t.start()
```

Note that only one thread can hold the lock at a time.

### Condition Variables

You can create a condition variable using the `_Condition` class from the `_thread` module:

```python
import _thread

cond = _thread.Condition()

def worker():
    cond.wait()  # Wait until signal is received
    print("Worker started")

e = _thread.Event()
t = _thread.Thread(target=worker)
t.start()
e.set()  # Send the signal

# You can also use .notify_all() to wake up all threads waiting on this condition variable
```

Note that condition variables use a private `_Condition` object, which can be accessed directly.

### Synchronization Objects

You can create synchronization objects using the `RLock`, `Semaphore`, and `RLock` classes from the `_thread` module:

```python
import _thread
from threading import RLock

lock = RLock()

def worker():
    lock.acquire()  # Acquire lock
    try:
        print("Worker holding lock")
    finally:
        lock.release()  # Release lock

t = _thread.Thread(target=worker)
t.start()
```

Note that the `RLock` class allows multiple threads to acquire the lock without blocking.

### Low-Level Thread Control

You can control threads at a low level using the `_active`, `_interrupted`, and `_dead` attributes of the `_ActiveThreads` object from the `_thread` module:

```python
import _thread

t = _thread.Thread(target=lambda: print("Worker thread started"))
t.start()
print(_thread.active)  # Get active threads count
```

Note that the `_active` attribute returns the number of active threads.
