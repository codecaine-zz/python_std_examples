# selectors - High-level I/O multiplexing

Below is a comprehensive set of code examples demonstrating various functionalities of the `selectors` module in Python 3.12, along with comments explaining each step.

### 1. Basic Usage

```python
import selectors

# Create a selector instance
sel = selectors.DefaultSelector()

def accept(sock, mask):
    # Accept a new connection
    conn, addr = sock.accept()
    print(f'Accepted {addr}')
    
    # Register the connection with the selector
    sel.register(conn, selectors.EVENT_READ, read)

def read(conn, mask):
    # Read data from the connection
    data = conn.recv(1024)
    if data:
        print('Received', repr(data))
        conn.sendall(data)  # Echo back to client
    else:
        print('Closing connection')
        sel.unregister(conn)
        conn.close()

def main():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the address and port
    server_socket.bind(('localhost', 12345))
    
    # Enable reuse of the socket address
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Listen for incoming connections
    server_socket.listen(10)
    print('Server listening on port 12345')
    
    # Register the server socket with the selector
    sel.register(server_socket, selectors.EVENT_READ, accept)

    while True:
        # Wait for an event to occur on one of the registered file descriptors
        events = sel.select(timeout=None)
        
        for key, mask in events:
            callback = key.data
            callback(key.fileobj, mask)

if __name__ == '__main__':
    main()
```

### 2. Using `EventLoop` and `Selector`

```python
import selectors

class EchoServer:
    def __init__(self):
        self.sel = selectors.DefaultSelector()

    def run(self, host='localhost', port=12345):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Bind the socket to the address and port
        server_socket.bind((host, port))
        
        # Enable reuse of the socket address
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        # Listen for incoming connections
        server_socket.listen(10)
        print(f'Server listening on {host}:{port}')
        
        # Register the server socket with the selector
        self.sel.register(server_socket, selectors.EVENT_READ, self.accept)

    def accept(self, sock, mask):
        # Accept a new connection
        conn, addr = sock.accept()
        print(f'Accepted {addr}')
        
        # Register the connection with the selector
        self.sel.register(conn, selectors.EVENT_READ | selectors.EVENT_WRITE, self.read_write)

    def read_write(self, conn, mask):
        if mask & selectors.EVENT_READ:
            # Read data from the connection
            data = conn.recv(1024)
            if data:
                print('Received', repr(data))
                conn.sendall(data)  # Echo back to client
            else:
                print('Closing connection')
                self.sel.unregister(conn)
                conn.close()

    def main(self):
        import asyncio

        loop = asyncio.get_event_loop()
        server_task = loop.run_until_complete(
            self.sel.serve_forever(host='localhost', port=12345)
        )

if __name__ == '__main__':
    EchoServer().run()
```

### 3. Handling Multiple Sockets and Events

```python
import selectors
import socket

def handle_socket(server_socket, mask):
    if mask & selectors.EVENT_READ:
        # Accept a new connection
        conn, addr = server_socket.accept()
        print(f'Accepted {addr}')
        
        # Register the connection with the selector
        sel.register(conn, selectors.EVENT_READ | selectors.EVENT_WRITE, read_write)

def read_write(conn, mask):
    if mask & selectors.EVENT_READ:
        # Read data from the connection
        data = conn.recv(1024)
        if data:
            print('Received', repr(data))
            conn.sendall(data)  # Echo back to client
        else:
            print('Closing connection')
            sel.unregister(conn)
            conn.close()
    elif mask & selectors.EVENT_WRITE:
        # Write some data to the connection
        conn.send(b'Hello, client!')

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the address and port
    server_socket.bind(('localhost', 12345))
    
    # Enable reuse of the socket address
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Listen for incoming connections
    server_socket.listen(10)
    print(f'Server listening on port 12345')
    
    sel = selectors.DefaultSelector()
    
    # Register the server socket with the selector
    sel.register(server_socket, selectors.EVENT_READ, handle_socket)

    while True:
        # Wait for an event to occur on one of the registered file descriptors
        events = sel.select(timeout=None)
        
        for key, mask in events:
            callback = key.data
            callback(key.fileobj, mask)

if __name__ == '__main__':
    main()
```

### 4. Using `Selector` with Non-Blocking Sockets

```python
import selectors
import socket

def handle_socket(sock, mask):
    if mask & selectors.EVENT_READ:
        # Read data from the connection
        data = sock.recv(1024)
        if data:
            print('Received', repr(data))
            sock.sendall(data)  # Echo back to client
        else:
            print('Closing connection')
            sel.unregister(sock)
            sock.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the address and port
    server_socket.bind(('localhost', 12345))
    
    # Enable reuse of the socket address
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Listen for incoming connections
    server_socket.listen(10)
    print(f'Server listening on port 12345')
    
    sel = selectors.DefaultSelector()
    
    # Register the server socket with the selector
    sel.register(server_socket, selectors.EVENT_READ, handle_socket)

    while True:
        # Wait for an event to occur on one of the registered file descriptors
        events = sel.select(timeout=None)
        
        for key, mask in events:
            callback = key.data
            callback(key.fileobj, mask)

if __name__ == '__main__':
    main()
```

### 5. Using `Selector` with Timed Events

```python
import selectors
import socket
import time

def handle_socket(sock, mask):
    if mask & selectors.EVENT_READ:
        # Read data from the connection
        data = sock.recv(1024)
        if data:
            print('Received', repr(data))
            sock.sendall(data)  # Echo back to client
        else:
            print('Closing connection')
            sel.unregister(sock)
            sock.close()

def check_timeouts(events):
    for key, mask in events:
        callback = key.data
        try:
            callback()
        except Exception as e:
            print(f'Error from {key.fileobj}: {e}')
            sel.unregister(key.fileobj)

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the address and port
    server_socket.bind(('localhost', 12345))
    
    # Enable reuse of the socket address
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Listen for incoming connections
    server_socket.listen(10)
    print(f'Server listening on port 12345')
    
    sel = selectors.DefaultSelector()
    
    # Register the server socket with the selector
    sel.register(server_socket, selectors.EVENT_READ, handle_socket)

    while True:
        # Wait for an event to occur on one of the registered file descriptors
        events = sel.select(timeout=1)
        
        # Check if any timed out callbacks need to be executed
        check_timeouts(events)

if __name__ == '__main__':
    main()
```

### 6. Using `Selector` with Priority Queues

```python
import selectors
import socket

def handle_socket(sock, mask):
    if mask & selectors.EVENT_READ:
        # Read data from the connection
        data = sock.recv(1024)
        if data:
            print('Received', repr(data))
            sock.sendall(data)  # Echo back to client
        else:
            print('Closing connection')
            sel.unregister(sock)
            sock.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the address and port
    server_socket.bind(('localhost', 12345))
    
    # Enable reuse of the socket address
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Listen for incoming connections
    server_socket.listen(10)
    print(f'Server listening on port 12345')
    
    sel = selectors.DefaultSelector()
    
    # Register the server socket with the selector
    sel.register(server_socket, selectors.EVENT_READ, handle_socket)

    while True:
        # Wait for an event to occur on one of the registered file descriptors
        events = sel.select(timeout=None)
        
        # Process events in order of priority (if needed)
        for key, mask in events:
            callback = key.data
            try:
                callback()
            except Exception as e:
                print(f'Error from {key.fileobj}: {e}')
                sel.unregister(key.fileobj)

if __name__ == '__main__':
    main()
```

These examples demonstrate various use cases for the `selectors` module in Python, including handling multiple connections with different types of events (read, write, etc.), using timed events, and prioritizing event processing. Each example is designed to illustrate a specific feature or scenario within the `selectors` API.
