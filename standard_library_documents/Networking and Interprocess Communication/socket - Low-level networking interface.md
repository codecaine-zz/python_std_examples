# socket — Low-level networking interface

**Socket Module**
================

The `socket` module provides an interface to create network sockets, which can be used for communication between processes or threads.

### Creating a Socket

To create a socket, you need to import the `socket` module and use the `socket()`, `.AF_INET`, and `SOCK_STREAM` constants.

```python
import socket

# Create a new socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Socket created:", sock)
```

### Socket Methods

Here are some common methods used with sockets:

#### 1. Bind()

Bind the socket to a specific address and port.

```python
sock.bind(("localhost", 8080))
print("Socket bound to localhost:8080")
```

#### 2. Listen()

Set up the socket to listen for incoming connections.

```python
sock.listen(5)
print("Socket listening on port 8080")
```

#### 3. Accept()

Accept an incoming connection and return a new socket object.

```python
conn, addr = sock.accept()
print("Connected by:", addr)
```

#### 4. Send() and Receive()

Send and receive data over the socket.

```python
sock.sendall(b"Hello, client!")
data = conn.recv(1024)
print(data.decode())
```

### Socket Constants

Here are some common constants used with sockets:

#### 1. AF_INET (Address Family)

Used to specify the address family for the socket. For IPv4, use `AF_INET`. For IPv6, use `AF_INET6`.

```python
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

#### 2. SOCK_STREAM (Socket Type)

Used to specify the type of socket. For TCP sockets, use `SOCK_STREAM`. For UDP sockets, use `SOCK_DGRAM`.

```python
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

### Socket Exception Handling

Use try-except blocks to handle exceptions that may occur while using the socket.

```python
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as e:
    print("Error creating socket:", e)
```

### Closing the Socket

Use `close()` to close the socket and free up system resources.

```python
sock.close()
print("Socket closed")
```

Example Use Case: Creating a Server-Client Communication System
-------------------------------------------------------------

Here's an example of how you can create a simple server-client communication system using sockets:

**server.py**
```python
import socket

# Create a new socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
sock.bind(("localhost", 8080))

# Listen for incoming connections
sock.listen(5)

print("Server listening on port 8080")

while True:
    conn, addr = sock.accept()
    print("Connected by:", addr)
    
    # Receive data from client
    data = conn.recv(1024)
    print(data.decode())
    
    # Send response back to client
    conn.sendall(b"Hello, client!")
```

**client.py**
```python
import socket

# Create a new socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
sock.connect(("localhost", 8080))

print("Connected to server")

# Send data to server
sock.sendall(b"Hello, server!")

# Receive response from server
data = sock.recv(1024)
print(data.decode())

# Close the socket
sock.close()
```

Run `server.py` in one terminal and `client.py` in another to see a simple client-server communication system in action.
