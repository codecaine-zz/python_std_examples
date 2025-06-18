# logging.handlers - Logging handlers
## Table of Contents

1. [1. RotatingFileHandler](#1-rotatingfilehandler)
2. [2. TimedRotatingFileHandler](#2-timedrotatingfilehandler)
3. [3. SocketHandler](#3-sockethandler)
4. [4. HTTPServerHandler](#4-httpserverhandler)
5. [5. QueueHandler and QueueListener](#5-queuehandler-and-queuelistener)
6. [6. SysLogHandler](#6-sysloghandler)
7. [7. SMTPHandler](#7-smtphandler)
8. [8. NullHandler](#8-nullhandler)
9. [9. MemoryHandler](#9-memoryhandler)
10. [10. WatchedFileHandler](#10-watchedfilehandler)



The `logging.handlers` module in Python provides various handler classes that can be used to send log records to different destinations, such as files, network sockets, or remote servers. Below are comprehensive code examples for each handler class provided by this module. These examples demonstrate how to configure and use these handlers effectively.

### 1. RotatingFileHandler
This handler rotates the log file after a certain size is reached.

```python
import logging
from logging.handlers import RotatingFileHandler

# Create a logger object
logger = logging.getLogger('RotatingFileHandlerExample')
logger.setLevel(logging.DEBUG)

# Define the log file name and max bytes for rotation
file_handler = RotatingFileHandler('example.log', maxBytes=1048576, backupCount=3)
file_handler.setLevel(logging.INFO)  # Only INFO and above level logs will be handled by this handler

# Create a formatter and set it for the file handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)

# Log some messages
for i in range(10):
    logger.debug(f'This is a debug message {i}')
    logger.info(f'This is an info message {i}')
```

### 2. TimedRotatingFileHandler
This handler rotates the log file on a schedule, e.g., daily.

```python
import logging
from logging.handlers import TimedRotatingFileHandler

# Create a logger object
logger = logging.getLogger('TimedRotatingFileHandlerExample')
logger.setLevel(logging.DEBUG)

# Define the log file name and rotation interval
file_handler = TimedRotatingFileHandler('example.log', when='midnight', interval=1, backupCount=3)
file_handler.setLevel(logging.WARNING)  # Only WARNING and above level logs will be handled by this handler

# Create a formatter and set it for the file handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)

# Log some messages
for i in range(10):
    logger.debug(f'This is a debug message {i}')
    logger.info(f'This is an info message {i}')
    logger.warning(f'This is a warning message {i}')
```

### 3. SocketHandler
This handler sends log records to a TCP server.

```python
import logging
from logging.handlers import SocketHandler

# Create a logger object
logger = logging.getLogger('SocketHandlerExample')
logger.setLevel(logging.DEBUG)

# Define the host and port of the server
server_address = ('localhost', 12345)
socket_handler = SocketHandler(server_address)

# Create a formatter and set it for the socket handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
socket_handler.setFormatter(formatter)

# Add the socket handler to the logger
logger.addHandler(socket_handler)

# Log some messages
for i in range(10):
    logger.debug(f'This is a debug message {i}')
    logger.info(f'This is an info message {i}')
    logger.warning(f'This is a warning message {i}')
```

### 4. HTTPServerHandler
This handler sends log records to an HTTP server.

```python
import logging
from logging.handlers import HTTPServerHandler

# Create a logger object
logger = logging.getLogger('HTTPServerHandlerExample')
logger.setLevel(logging.DEBUG)

# Define the URL of the server
url = 'http://localhost:8080'
http_handler = HTTPServerHandler(url, handler_class=None)

# Create a formatter and set it for the HTTP server handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
http_handler.setFormatter(formatter)

# Add the HTTP server handler to the logger
logger.addHandler(http_handler)

# Log some messages
for i in range(10):
    logger.debug(f'This is a debug message {i}')
    logger.info(f'This is an info message {i}')
    logger.warning(f'This is a warning message {i}')
```

### 5. QueueHandler and QueueListener
These handlers use a queue to send log records to multiple destinations.

```python
import logging
from logging.handlers import QueueHandler, QueueListener

# Create a logger object
logger = logging.getLogger('QueueHandlerExample')
logger.setLevel(logging.DEBUG)

# Create a queue
queue = logging.Queue()

# Create a file handler and add it to the queue
file_handler = RotatingFileHandler('example.log', maxBytes=1048576, backupCount=3)
queue.addHandler(file_handler)

# Create a socket handler and add it to the queue
socket_handler = SocketHandler(('localhost', 12345))
queue.addHandler(socket_handler)

# Create a logger that uses the queue
logger_queue = logging.getLogger('QueueLogger')
logger_queue.setLevel(logging.INFO)
logger_queue.addHandler(QueueHandler(queue))

# Log some messages
for i in range(10):
    logger.debug(f'This is a debug message {i}')
    logger.info(f'This is an info message {i}')

# Start the queue listener to process the queue and send log records
with QueueListener(queue, file_handler, socket_handler) as listener:
    listener.start()
```

### 6. SysLogHandler
This handler sends log records to a syslog server.

```python
import logging
from logging.handlers import SysLogHandler

# Create a logger object
logger = logging.getLogger('SysLogHandlerExample')
logger.setLevel(logging.DEBUG)

# Define the address of the syslog server
syslog_handler = SysLogHandler(address=('localhost', 514))

# Create a formatter and set it for the syslog handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
syslog_handler.setFormatter(formatter)

# Add the syslog handler to the logger
logger.addHandler(syslog_handler)

# Log some messages
for i in range(10):
    logger.debug(f'This is a debug message {i}')
    logger.info(f'This is an info message {i}')
```

### 7. SMTPHandler
This handler sends log records via email.

```python
import logging
from logging.handlers import SMTPHandler

# Create a logger object
logger = logging.getLogger('SMTPHandlerExample')
logger.setLevel(logging.DEBUG)

# Define the SMTP server and port, and sender and recipient email addresses
smtp_handler = SMTPHandler(mailhost=('localhost', 25), fromaddr='sender@example.com', toaddrs=['recipient@example.com'])

# Create a formatter and set it for the SMTP handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
smtp_handler.setFormatter(formatter)

# Add the SMTP handler to the logger
logger.addHandler(smtp_handler)

# Log some messages
for i in range(10):
    logger.debug(f'This is a debug message {i}')
    logger.info(f'This is an info message {i}')
```

### 8. NullHandler
This handler does not do anything with the log records.

```python
import logging

# Create a logger object
logger = logging.getLogger('NullHandlerExample')
logger.setLevel(logging.DEBUG)

# Add a null handler to the logger
logger.addHandler(logging.NullHandler())

# Log some messages
for i in range(10):
    logger.debug(f'This is a debug message {i}')
    logger.info(f'This is an info message {i}')
```

### 9. MemoryHandler
This handler stores log records in memory and sends them when the queue size reaches a certain limit.

```python
import logging
from logging.handlers import MemoryHandler

# Create a logger object
logger = logging.getLogger('MemoryHandlerExample')
logger.setLevel(logging.DEBUG)

# Define the maximum number of log records to store in memory
memory_handler = MemoryHandler(50)  # Store up to 50 log records in memory

# Add a file handler and add it to the memory handler
file_handler = RotatingFileHandler('example.log', maxBytes=1048576, backupCount=3)
memory_handler.addHandler(file_handler)

# Create a formatter and set it for the memory handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
memory_handler.setFormatter(formatter)

# Add the memory handler to the logger
logger.addHandler(memory_handler)

# Log some messages
for i in range(10):
    logger.debug(f'This is a debug message {i}')
    logger.info(f'This is an info message {i}')
```

### 10. WatchedFileHandler
This handler watches a file and logs all new lines as they are written.

```python
import logging
from logging.handlers import WatchedFileHandler

# Create a logger object
logger = logging.getLogger('WatchedFileHandlerExample')
logger.setLevel(logging.DEBUG)

# Define the log file name to watch
watched_file_handler = WatchedFileHandler('example.log')

# Create a formatter and set it for the watched file handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
watched_file_handler.setFormatter(formatter)

# Add the watched file handler to the logger
logger.addHandler(watched_file_handler)

# Log some messages
for i in range(10):
    logger.debug(f'This is a debug message {i}')
    logger.info(f'This is an info message {i}')
```

These examples demonstrate various logging handlers and their use cases. You can choose the appropriate handler based on your specific needs, such as logging to files, sending emails, or processing log records in memory. Each example includes setting up a logger, adding handlers, and configuring the formatter for clarity. Adjust the configuration parameters as needed for your environment.
