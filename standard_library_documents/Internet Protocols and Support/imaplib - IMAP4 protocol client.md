# imaplib - IMAP4 protocol client

The `imaplib` module in Python provides an interface to the IMAP4 protocol, which is used for retrieving and managing email messages on a mail server. Below are comprehensive code examples demonstrating various functionalities of the `imaplib` module.

### 1. Connecting to an IMAP Server

```python
import imaplib

def connect_to_imap_server(server, username, password):
    """
    Connects to an IMAP server and returns an IMAP4 object.

    :param server: The IMAP server address (e.g., 'imap.example.com').
    :param username: The user's email username.
    :param password: The user's email password.
    :return: An IMAP4 object connected to the specified server.
    """
    try:
        # Connect to the IMAP server
        imap = imaplib.IMAP4_SSL(server)
        imap.login(username, password)
        print(f"Connected to {server} as {username}")
        return imap
    except Exception as e:
        print(f"Failed to connect to {server}: {e}")
        return None

# Example usage
server = 'imap.example.com'
username = 'your-email@example.com'
password = 'your-password'

imap_connection = connect_to_imap_server(server, username, password)
if imap_connection:
    # Proceed with operations
    pass
```

### 2. Listing Mailboxes (Inboxes)

```python
def list_mailboxes(imap):
    """
    Lists all mailboxes on the server.

    :param imap: An IMAP4 object connected to an IMAP server.
    :return: A list of mailbox names.
    """
    try:
        # Select the INBOX mailbox
        status, messages = imap.select('INBOX')
        if status == 'OK':
            print("Listing mailboxes...")
            # List all available mailboxes
            return imap.list()[1]
        else:
            print(f"Failed to list mailboxes: {status}")
            return None
    except Exception as e:
        print(f"Failed to list mailboxes: {e}")
        return []

# Example usage
if imap_connection:
    mailboxes = list_mailboxes(imap_connection)
    if mailboxes:
        for mailbox in mailboxes:
            print(mailbox.decode('utf-8'))
```

### 3. Searching for Emails

```python
def search_emails(imap, criteria):
    """
    Searches for emails based on a set of criteria.

    :param imap: An IMAP4 object connected to an IMAP server.
    :param criteria: A list of search criteria (e.g., ['FROM', 'example@example.com']).
    :return: A list of email IDs that match the criteria.
    """
    try:
        # Search for emails
        status, messages = imap.search(None, *criteria)
        if status == 'OK':
            print(f"Found {len(messages[0].split())} matching messages.")
            return messages[0].split()
        else:
            print(f"Failed to search for emails: {status}")
            return []
    except Exception as e:
        print(f"Failed to search for emails: {e}")
        return []

# Example usage
if imap_connection:
    criteria = ['FROM', 'example@example.com']
    email_ids = search_emails(imap_connection, criteria)
    if email_ids:
        for email_id in email_ids:
            print(email_id.decode('utf-8'))
```

### 4. Retrieving Emails

```python
def retrieve_email(imap, message_id):
    """
    Retrieves an email based on its ID.

    :param imap: An IMAP4 object connected to an IMAP server.
    :param message_id: The ID of the email to retrieve.
    :return: The raw email data as bytes.
    """
    try:
        # Fetch the email
        status, email_data = imap.fetch(message_id, '(RFC822)')
        if status == 'OK':
            print(f"Email retrieved: {message_id}")
            return email_data[0][1]
        else:
            print(f"Failed to retrieve email: {status}")
            return None
    except Exception as e:
        print(f"Failed to retrieve email: {e}")
        return None

# Example usage
if imap_connection and email_ids:
    message_id = email_ids[0]  # Assume the first email ID is the one to fetch
    raw_email = retrieve_email(imap_connection, message_id)
    if raw_email:
        print(raw_email.decode('utf-8'))
```

### 5. Storing Emails (Outbox)

```python
def store_emails(imap, folder_name, messages):
    """
    Stores email messages in a specified folder.

    :param imap: An IMAP4 object connected to an IMAP server.
    :param folder_name: The name of the folder where emails will be stored.
    :param messages: A list of raw email data as bytes.
    """
    try:
        # Select the target folder
        imap.select(folder_name)
        # Store each message
        for msg in messages:
            status, result = imap.append(folder_name, '', None, msg)
            if status == 'OK':
                print(f"Message stored in {folder_name}: {result[0].decode('utf-8')}")
            else:
                print(f"Failed to store message in {folder_name}: {status}")
    except Exception as e:
        print(f"Failed to store emails: {e}")

# Example usage
if imap_connection and email_ids:
    folder_name = 'Sent'
    messages_to_store = [raw_email for _, raw_email in enumerate(messages, 1)]  # Assume all retrieved emails are to be stored
    store_emails(imap_connection, folder_name, messages_to_store)
```

### 6. Deleting Emails

```python
def delete_emails(imap, message_id):
    """
    Deletes an email based on its ID.

    :param imap: An IMAP4 object connected to an IMAP server.
    :param message_id: The ID of the email to delete.
    """
    try:
        # Delete the email
        status, result = imap.store(message_id, '+FLAGS', '\\Deleted')
        if status == 'OK':
            print(f"Email deleted: {message_id}")
        else:
            print(f"Failed to delete email: {status}")
    except Exception as e:
        print(f"Failed to delete email: {e}")

# Example usage
if imap_connection and email_ids:
    message_id = email_ids[0]  # Assume the first email ID is the one to delete
    delete_emails(imap_connection, message_id)
```

### 7. Expunging Deleted Emails

```python
def expunge_deleted_emails(imap):
    """
    Expunges (deletes) all deleted emails from a mailbox.

    :param imap: An IMAP4 object connected to an IMAP server.
    """
    try:
        # Expunge all deleted emails
        status, result = imap.expunge()
        if status == 'OK':
            print("Deleted emails expunged.")
        else:
            print(f"Failed to expunge deleted emails: {status}")
    except Exception as e:
        print(f"Failed to expunge deleted emails: {e}")

# Example usage
if imap_connection and email_ids:
    expunge_deleted_emails(imap_connection)
```

### 8. Disconnecting from the Server

```python
def disconnect_from_imap_server(imap):
    """
    Disconnects from the IMAP server.

    :param imap: An IMAP4 object connected to an IMAP server.
    """
    try:
        # Logout and close the connection
        imap.logout()
        print("Disconnected from the IMAP server.")
    except Exception as e:
        print(f"Failed to disconnect from the IMAP server: {e}")

# Example usage
if imap_connection:
    disconnect_from_imap_server(imap_connection)
```

These examples provide a comprehensive overview of how to use various functionalities in the `imaplib` module. Each example includes error handling and assumes that you have already established a connection to the IMAP server using `connect_to_imap_server`.
