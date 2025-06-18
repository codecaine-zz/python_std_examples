# socket - Low-level networking interface
## Table of Contents

1. [1. Creating a TCP Socket](#1-creating-a-tcp-socket)
2. [Explanation:](#explanation)
3. [2. Creating a UDP Socket](#2-creating-a-udp-socket)
4. [Explanation:](#explanation)
5. [3. Connecting to a Remote Server](#3-connecting-to-a-remote-server)
6. [Explanation:](#explanation)
7. [4. Using Sockets with Multithreading](#4-using-sockets-with-multithreading)
8. [Explanation:](#explanation)



The `socket` module in Python provides a low-level interface for network communication. It allows you to create sockets and use them to connect to other servers, send and receive data over various protocols such as TCP and UDP. Below are comprehensive code examples demonstrating various functionalities of the `socket` module.

### 1. Creating a TCP Socket

```python
import socket

# Create a new TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to an address and port
server_address = ('localhost', 10000)
print(f'Starting up on {server_address[0]} port {server_address[1]}')
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen()
print('Waiting for a connection...')

# Accept a connection
connection, client_address = server_socket.accept()
try:
    print(f'Connection from {client_address}')
    
    # Receive data in small chunks and echo it back to the client
    while True:
        data = connection.recv(16)
        if data:
            print(f"Received: '{data.decode()}'")
            connection.sendall(data)  # Echo the received data
        else:
            print('No more data from', client_address)
            break

finally:
    # Clean up the connection
    connection.close()
```

### Explanation:
- **`socket.socket(socket.AF_INET, socket.SOCK_STREAM)`**: Creates a new TCP/IP socket.
- **`server_socket.bind(server_address)`**: Binds the socket to an IP address and port.
- **`server_socket.listen()`**: Starts listening for incoming connections.
- **`connection, client_address = server_socket.accept()`**: Accepts a connection from a client.

### 2. Creating a UDP Socket

```python
import socket

# Create a new UDP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define the server address and port
server_address = ('localhost', 10000)
print(f'Sending to {server_address[0]} port {server_address[1]}')

# Message to send
message = b'Hello from UDP client'

try:
    # Send data
    print('Sending message: "%s"' % message)
    client_socket.sendto(message, server_address)

    # Receive a response from the server (assuming it echoes back)
    received_data, server_address = client_socket.recvfrom(4096)
    print(f'Received "{received_data.decode()}" from {server_address}')

finally:
    # Close the socket
    client_socket.close()
```

### Explanation:
- **`socket.socket(socket.AF_INET, socket.SOCK_DGRAM)`**: Creates a new UDP/IP socket.
- **`client_socket.sendto(message, server_address)`**: Sends data to the specified server address and port.
- **`received_data, server_address = client_socket.recvfrom(4096)`**: Receives data from the server.

### 3. Connecting to a Remote Server

```python
import socket

# Create a new TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_address = ('example.com', 80)

try:
    # Connect to the server
    print('Connecting to %s port %d' % server_address)
    client_socket.connect(server_address)

    # Send data
    message = b"GET / HTTP/1.0\r\nHost: example.com\r\n\r\n"
    print("Sending message:", message.decode())
    client_socket.sendall(message)

    # Receive the response from the server
    amount_received = 0
    amount_expected = len(message)
    
    while True:
        data = client_socket.recv(16)
        if not data:
            break
        amount_received += len(data)
        print(f"Received {amount_received} bytes of data")
    
    print('Received', amount_received, 'bytes from', server_address)

finally:
    # Close the socket
    client_socket.close()
```

### Explanation:
- **`client_socket.connect(server_address)`**: Connects to a remote server at the specified IP address and port.
- **Sending data** using `client_socket.sendall()`.
- **Receiving data** in chunks using `client_socket.recv()`.

### 4. Using Sockets with Multithreading

```python
import socket
import threading

def handle_client(client_socket, client_address):
    print('Handling client', client_address)
    
    try:
        while True:
            data = client_socket.recv(16)
            if not data:
                break
            print(f"Received: '{data.decode()}' from {client_address}")
            client_socket.sendall(data)  # Echo the received data

    finally:
        # Close the connection
        client_socket.close()
        print('Closed connection with', client_address)

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to an address and port
server_address = ('localhost', 10000)
print(f'Starting up on {server_address[0]} port {server_address[1]}')
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen()

try:
    while True:
        print('Waiting for a connection...')
        client_socket, client_address = server_socket.accept()
        
        # Handle the new connection in a separate thread
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

except KeyboardInterrupt:
    print('Server shutting down.')

finally:
    # Clean up the listening socket
    server_socket.close()
```

### Explanation:
- **Using `threading` to handle multiple clients**: Each new connection is handled by a separate thread.
- The `handle_client` function processes data received from and sends back data to each client.

These examples cover basic functionalities of the `socket` module, including creating sockets, binding and listening, connecting to remote servers, and handling multiple connections with threading.
