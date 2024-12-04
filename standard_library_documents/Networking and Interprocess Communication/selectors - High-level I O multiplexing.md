# selectors - High-level I/O multiplexing

**Selectors in Python**
=====================================

The `select` module in Python provides an interface to the Unix file descriptor selector, allowing you to wait for multiple file descriptors to become ready.

### Importing the Module

```python
import select
```

### Creating a Selector Object

To use the `select` module, you need to create a selector object, passing in three lists of file descriptors:

*   `rlist`: A list of file descriptors that can be read from.
*   `wlist`: A list of file descriptors that can be written to.
*   `xlist`: A list of file descriptors that have exceptional events (e.g., errors).

```python
import socket

# Create a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# List of file descriptors for reading, writing, and exceptions
rlist = [sock]
wlist = []
xlist = []

# Create the selector object
s = select.select(rlist, wlist, xlist)
```

### Using the Selector Object

The `select` function takes three lists of file descriptors as input and returns a tuple containing:

*   A list of readable file descriptors.
*   A list of writable file descriptors.
*   A list of file descriptors with exceptional events.

You can use this information to perform I/O operations on the corresponding file descriptors.

```python
# Iterate over the selectors
for r, w, x in s:
    # Handle read operation
    data = sock.recv(1024)
    if data:
        print("Received:", data.decode())
    
    # Handle write operation
    sock.sendall(b"Hello, world!")
```

### Example Use Case: Web Server

Here's an example of using the `select` module in a simple web server:

```python
import socket
import select

# Create a socket and bind it to a port
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("localhost", 8080))
sock.listen(5)

# List of file descriptors for reading, writing, and exceptions
rlist = [sock]
wlist = []
xlist = []

while True:
    # Wait for I/O operations to become ready
    s = select.select(rlist, wlist, xlist)
    
    # Handle read operation
    for r in s[0]:
        conn, addr = r.accept()
        print("New connection:", addr)
        
        # Add the new connection to the lists of file descriptors
        rlist.append(conn)
        wlist.append(None)
        xlist.append(None)

    # Handle write operations
    for w in s[1]:
        if w is not None:
            data = sock.recv(1024)
            if data:
                print("Sending:", data.decode())
```

This example demonstrates how the `select` module can be used to create a simple web server that handles multiple connections concurrently.

### Error Handling

When using the `select` module, you should always handle errors properly. Here's an example of how to do this:

```python
try:
    # Wait for I/O operations to become ready
    s = select.select(rlist, wlist, xlist)
except KeyboardInterrupt:
    print("Exiting...")
except socket.error as e:
    print("Socket error:", e)
```

This code catches `KeyboardInterrupt` exceptions and `socket.error` exceptions, providing a better user experience.
