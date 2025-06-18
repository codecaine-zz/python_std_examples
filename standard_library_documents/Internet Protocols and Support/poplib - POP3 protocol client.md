# poplib - POP3 protocol client
## Table of Contents

1. [Example 1: Retrieving Messages](#example-1-retrieving-messages)
2. [Example 2: Deleting Messages](#example-2-deleting-messages)
3. [Example 3: Retrieving Email Headers](#example-3-retrieving-email-headers)
4. [Example 4: Handling Multiple Messages](#example-4-handling-multiple-messages)
5. [Example 5: Handling Large Emails](#example-5-handling-large-emails)
6. [Example 6: Error Handling and Logging](#example-6-error-handling-and-logging)
7. [Example 7: Using TLS with Authentication](#example-7-using-tls-with-authentication)



The `poplib` module in Python provides a convenient interface to access email messages using the Post Office Protocol (POP3). Below are comprehensive examples demonstrating various functionalities of the `poplib` module. These examples cover basic usage, error handling, and advanced features like retrieving specific email headers.

### Example 1: Retrieving Messages

```python
import poplib
from email.parser import BytesParser

# Connect to a POP3 server (e.g., Gmail)
server = poplib.POP3_SSL('pop.gmail.com', 995)

# Login to the server
username = 'your-email@gmail.com'
password = 'your-password'
try:
    server.user(username)
    server.pass_(password)
except poplib.error_proto as e:
    print(f"Login failed: {e}")
else:
    # Retrieve all messages
    num_messages = len(server.list()[1])
    for i in range(num_messages):
        # Retrieve a specific message by index
        resp, lines, octets = server.retr(i + 1)
        raw_email = b'\n'.join(lines)  # Combine lines into one string

        # Parse the email using BytesParser
        email_message = BytesParser().parse(raw_email)

        print(f"Message {i + 1}:")
        print("From:", email_message['from'])
        print("Subject:", email_message['subject'])

    # Close the connection
    server.quit()

# Note: Ensure you handle exceptions properly and close the connection to free resources.
```

### Example 2: Deleting Messages

```python
import poplib

# Connect to a POP3 server (e.g., Gmail)
server = poplib.POP3_SSL('pop.gmail.com', 995)

# Login to the server
username = 'your-email@gmail.com'
password = 'your-password'
try:
    server.user(username)
    server.pass_(password)
except poplib.error_proto as e:
    print(f"Login failed: {e}")
else:
    # Retrieve all messages
    num_messages = len(server.list()[1])
    for i in range(num_messages):
        print(f"Message {i + 1}:")
        try:
            # Delete the message by index
            server.dele(i + 1)
        except poplib.error_proto as e:
            print(f"Failed to delete message {i + 1}: {e}")

    # Close the connection
    server.quit()
```

### Example 3: Retrieving Email Headers

```python
import poplib
from email.parser import BytesParser

# Connect to a POP3 server (e.g., Gmail)
server = poplib.POP3_SSL('pop.gmail.com', 995)

# Login to the server
username = 'your-email@gmail.com'
password = 'your-password'
try:
    server.user(username)
    server.pass_(password)
except poplib.error_proto as e:
    print(f"Login failed: {e}")
else:
    # Retrieve all messages
    num_messages = len(server.list()[1])
    for i in range(num_messages):
        resp, lines, octets = server.retr(i + 1)
        raw_email = b'\n'.join(lines)

        # Parse the email using BytesParser to extract headers
        email_message = BytesParser().parse(raw_email)

        print(f"Message {i + 1}:")
        for header in email_message:
            print(header, ":", email_message[header])

    # Close the connection
    server.quit()
```

### Example 4: Handling Multiple Messages

```python
import poplib
from email.parser import BytesParser

# Connect to a POP3 server (e.g., Gmail)
server = poplib.POP3_SSL('pop.gmail.com', 995)

# Login to the server
username = 'your-email@gmail.com'
password = 'your-password'
try:
    server.user(username)
    server.pass_(password)
except poplib.error_proto as e:
    print(f"Login failed: {e}")
else:
    # Retrieve all messages
    num_messages = len(server.list()[1])
    for i in range(num_messages):
        resp, lines, octets = server.retr(i + 1)
        raw_email = b'\n'.join(lines)

        # Parse the email using BytesParser to extract headers and body
        email_message = BytesParser().parse(raw_email)

        print(f"Message {i + 1}:")
        for header in email_message:
            print(header, ":", email_message[header])

    # Close the connection
    server.quit()
```

### Example 5: Handling Large Emails

```python
import poplib
from email.parser import BytesParser

# Connect to a POP3 server (e.g., Gmail)
server = poplib.POP3_SSL('pop.gmail.com', 995)

# Login to the server
username = 'your-email@gmail.com'
password = 'your-password'
try:
    server.user(username)
    server.pass_(password)
except poplib.error_proto as e:
    print(f"Login failed: {e}")
else:
    # Retrieve all messages
    num_messages = len(server.list()[1])
    for i in range(num_messages):
        resp, lines, octets = server.retr(i + 1)
        raw_email = b'\n'.join(lines)

        # Parse the email using BytesParser to handle large emails
        email_message = BytesParser().parse(raw_email)

        print(f"Message {i + 1}:")
        for header in email_message:
            print(header, ":", email_message[header])

    # Close the connection
    server.quit()
```

### Example 6: Error Handling and Logging

```python
import poplib
from email.parser import BytesParser
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Connect to a POP3 server (e.g., Gmail)
server = poplib.POP3_SSL('pop.gmail.com', 995)

# Login to the server
username = 'your-email@gmail.com'
password = 'your-password'
try:
    server.user(username)
    server.pass_(password)
except poplib.error_proto as e:
    logging.error(f"Login failed: {e}")
else:
    try:
        # Retrieve all messages
        num_messages = len(server.list()[1])
        for i in range(num_messages):
            resp, lines, octets = server.retr(i + 1)
            raw_email = b'\n'.join(lines)

            # Parse the email using BytesParser
            email_message = BytesParser().parse(raw_email)

            logging.info(f"Message {i + 1}:")
            for header in email_message:
                logging.info(f"{header} : {email_message[header]}")

    except poplib.error_proto as e:
        logging.error(f"Error processing message: {e}")

    # Close the connection
    server.quit()
```

### Example 7: Using TLS with Authentication

```python
import poplib
from email.parser import BytesParser

# Connect to a POP3 server (e.g., Gmail) using TLS
server = poplib.POP3_SSL('pop.gmail.com', 995)

# Login to the server
username = 'your-email@gmail.com'
password = 'your-password'
try:
    server.user(username)
    server.pass_(password)
except poplib.error_proto as e:
    print(f"Login failed: {e}")
else:
    # Retrieve all messages
    num_messages = len(server.list()[1])
    for i in range(num_messages):
        resp, lines, octets = server.retr(i + 1)
        raw_email = b'\n'.join(lines)

        # Parse the email using BytesParser
        email_message = BytesParser().parse(raw_email)

        print(f"Message {i + 1}:")
        for header in email_message:
            print(header, ":", email_message[header])

    # Close the connection
    server.quit()
```

These examples demonstrate basic usage of the `poplib` module, including retrieving and parsing emails, handling exceptions, and logging messages. Each example is designed to be self-contained and includes comments for clarity.
