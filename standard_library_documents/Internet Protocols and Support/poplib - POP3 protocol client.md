# poplib — POP3 protocol client

**poplib Module**
================

The `poplib` module provides an interface to access and manipulate POP3 mailboxes.

**Installation**
---------------

To use the `poplib` module, you need to install a Python IMAP/POP3 library such as `imaplib` and `smtplib`. These libraries are included in the standard library of Python 3.x.

**Example Usage**
-----------------

Here's an example of how to use the `poplib` module:

```python
import poplib

def main():
    # Define POP3 server details
    host = 'example.com'
    port = 995
    username = 'username'
    password = 'password'

    # Create a POP3 connection object
    try:
        conn = poplib.POP3S(host, port)
    except Exception as e:
        print(f"Failed to connect: {e}")
        return

    # Authentication
    conn.login(username, password)

    # Get the number of messages in the mailbox
    num_messages = conn.get_num_messages()
    print(f"Number of messages: {num_messages}")

    # Retrieve a message by ID
    msg_id = 1
    try:
        raw_message = conn.retr(msg_id)
    except Exception as e:
        print(f"Failed to retrieve message {msg_id}: {e}")
        return

    # Print the message
    print("Message:")
    for line in raw_message.decode('utf-8'):
        print(line)

    # Quit the connection
    conn.quit()

if __name__ == "__main__":
    main()
```

**Available Methods**
--------------------

Here's a list of available methods and their descriptions:

### Connection Object

* `login(username, password)`: Logs in to the POP3 server.
* `quit()`: Quits the connection.
* `get_num_messages()`: Returns the number of messages in the mailbox.
* `retr(msg_id)`: Retrieves a message by ID.

### Mailbox Methods

* `select()`: Selects an email folder or mailbox.
* `append(message_data, filename)`: Appends a file to the selected mailbox.
* `list()`: Lists all the files in the selected mailbox.

**Common Exceptions**
---------------------

Here are some common exceptions you may encounter when using the `poplib` module:

* `ConnectionRefusedError`: Raised if the POP3 server cannot be connected to.
* `AuthenticationError`: Raised if authentication fails.
* `MessageNotFoundError`: Raised if a message is not found by ID.

Note: The above examples and documentation are for Python 3.x.
