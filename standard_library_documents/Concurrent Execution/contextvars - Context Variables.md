# contextvars — Context Variables

Here's an example of using the `contextvars` module in Python:
```python
import contextvars

# Create a context variable
var = contextvars.ContextVar('my_var', default='default_value')

def get_context():
    """Get the current value of the context variable."""
    return var.value

def set_context(value):
    """Set the new value of the context variable."""
    var.set(value)

# Usage example:
set_context('new_value')
print(get_context())  # Output: new_value

import threading
with threading.Lock():
    # Accessing the context variable inside a lock block is thread-safe.
    print(get_context())
```
However, if you want to get the current thread's value of `my_var`, you can use the following example:
```python
# Create a context variable with default value 'default_value'
var = contextvars.ContextVar('my_var', default='default_value')

def my_thread_func():
    """Thread function that gets and sets the context variable."""
    print("Current value:", var.value)
    # To get the thread-local value, you need to use the threading.current_thread().ident.
    local_var = var.get(threading.current_thread())
    print(f"Local value: {local_var}")
    set_context('new_value')

# Create and start two threads
import threading

t1 = threading.Thread(target=my_thread_func)
t2 = threading.Thread(target=my_thread_func)

t1.start()
t2.start()

# Wait for the threads to finish
t1.join()
t2.join()

print(get_context())  # Output: new_value
```
You can also use `contextvars.ContextData` instead of `ContextVar`, it allows you to store a dictionary in the context:
```python
import contextvars

# Create a context variable with default value {'a': 'default_a', 'b': 'default_b'}
data = contextvars.ContextData({'a': 'default_a', 'b': 'default_b'})

def get_context():
    """Get the current value of the context data."""
    return data.value()

def set_context(key, value):
    """Set the new value in the context data."""
    data.set(value)

# Usage example:
set_context('new_a', 'new_value_a')
print(get_context())  # Output: {'a': 'new_value_a'}

import threading
with threading.Lock():
    # Accessing the context variable inside a lock block is thread-safe.
    print(get_context())
```
This code will allow you to store and retrieve values in the context of each thread.
