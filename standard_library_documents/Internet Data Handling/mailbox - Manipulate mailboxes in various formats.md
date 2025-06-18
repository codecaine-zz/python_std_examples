# mailbox - Manipulate mailboxes in various formats
## Table of Contents

1. [Example 1: Reading an mbox mailbox](#example-1-reading-an-mbox-mailbox)
2. [Example 2: Writing to an mbox mailbox](#example-2-writing-to-an-mbox-mailbox)
3. [Example 3: Reading from a Maildir mailbox](#example-3-reading-from-a-maildir-mailbox)
4. [Example 4: Writing to a Maildir mailbox](#example-4-writing-to-a-maildir-mailbox)
5. [Example 5: Reading from an IMAP4 mailbox](#example-5-reading-from-an-imap4-mailbox)
6. [Example 6: Writing to an IMAP4 mailbox](#example-6-writing-to-an-imap4-mailbox)
7. [Example 7: Reading from a POP3 mailbox](#example-7-reading-from-a-pop3-mailbox)
8. [Example 8: Writing to a POP3 mailbox](#example-8-writing-to-a-pop3-mailbox)
9. [Explanation](#explanation)



The `mailbox` module in Python provides a consistent interface to access mailboxes in several popular formats, including mbox, Maildir, IMAP4, and POP3. Below are comprehensive examples demonstrating how to use this module for different operations.

### Example 1: Reading an mbox mailbox

```python
import mailbox

# Open an existing mbox mailbox
with mailbox.mbox('path/to/your/mailbox') as m:
    # Iterate over all messages in the mailbox
    for msg in m:
        # Print the message ID and sender
        print(f"Message ID: {msg['Message-ID']}, From: {msg['From']}")

# Example output:
# Message ID: <uuid@domain.com>, From: user@example.com
```

### Example 2: Writing to an mbox mailbox

```python
import mailbox

# Create a new empty mbox file for writing
with mailbox.mbox('path/to/new_mailbox') as m:
    # Create a new email message
    msg = mailbox.Message()
    msg['From'] = 'sender@example.com'
    msg['To'] = 'recipient@example.com'
    msg['Subject'] = 'Test Message'
    msg.set_payload("This is the body of the test message.")

    # Add the message to the mailbox
    m.add(msg)

# Example output: The message will be added to the mbox file.
```

### Example 3: Reading from a Maildir mailbox

```python
import mailbox

# Open an existing Maildir mailbox
with mailbox.Maildir('path/to/your/maildir') as m:
    # Iterate over all messages in the mailbox
    for msg in m:
        # Print the message ID and subject
        print(f"Message ID: {msg['Message-ID']}, Subject: {msg['Subject']}")

# Example output:
# Message ID: <uuid@domain.com>, Subject: Test Email
```

### Example 4: Writing to a Maildir mailbox

```python
import mailbox

# Create a new empty Maildir directory for writing
with mailbox.Maildir('path/to/new_maildir') as m:
    # Create a new email message
    msg = mailbox.Message()
    msg['From'] = 'sender@example.com'
    msg['To'] = 'recipient@example.com'
    msg['Subject'] = 'Test Message'
    msg.set_payload("This is the body of the test message.")

    # Add the message to the Maildir mailbox
    m.add(msg)

# Example output: The message will be added to a new directory within the Maildir.
```

### Example 5: Reading from an IMAP4 mailbox

```python
import mailbox

# Connect to an IMAP4 server and login
imap = mailbox.IMAP4_SSL('imap.example.com', 993)
imap.login('username@example.com', 'password')

# Select a mailbox (e.g., INBOX)
imap.select("INBOX")

# Search for all messages
status, data = imap.search(None, "ALL")
for num in data[0].split():
    # Fetch the email message by number
    status, msg_data = imap.fetch(num, "(RFC822)")
    msg = mailbox.Message(msg_data[1][1])
    
    # Print the sender and subject of the message
    print(f"Sender: {msg['From']}, Subject: {msg['Subject']}")

# Example output: The sender and subject of each email will be printed.
```

### Example 6: Writing to an IMAP4 mailbox

```python
import mailbox

# Connect to an IMAP4 server and login
imap = mailbox.IMAP4_SSL('imap.example.com', 993)
imap.login('username@example.com', 'password')

# Select a mailbox (e.g., INBOX)
imap.select("INBOX")

# Create a new email message
msg = mailbox.Message()
msg['From'] = 'sender@example.com'
msg['To'] = 'recipient@example.com'
msg['Subject'] = 'Test Message'
msg.set_payload("This is the body of the test message.")

# Append the message to the IMAP4 mailbox
imap.append("INBOX", msg.as_bytes())

# Example output: The message will be appended to the specified mailbox.
```

### Example 7: Reading from a POP3 mailbox

```python
import mailbox

# Connect to a POP3 server and login
pop = mailbox.POP3('pop.example.com', 110)
pop.user('username@example.com')
pop.pass_('password')

# Retrieve all messages
num_messages = pop.stat()[0]
for i in range(num_messages):
    # Retrieve the message by index
    msg = mailbox.Message(pop.retr(i + 1)[1])
    
    # Print the sender and subject of the message
    print(f"Sender: {msg['From']}, Subject: {msg['Subject']}")

# Example output: The sender and subject of each email will be printed.
```

### Example 8: Writing to a POP3 mailbox

```python
import mailbox

# Connect to a POP3 server and login
pop = mailbox.POP3('pop.example.com', 110)
pop.user('username@example.com')
pop.pass_('password')

# Create a new email message
msg = mailbox.Message()
msg['From'] = 'sender@example.com'
msg['To'] = 'recipient@example.com'
msg['Subject'] = 'Test Message'
msg.set_payload("This is the body of the test message.")

# Append the message to the POP3 mailbox
pop.append("INBOX", msg.as_bytes())

# Example output: The message will be appended to the specified mailbox.
```

### Explanation

- **mbox**: Used for reading and writing mbox files. It supports basic mail handling operations.
- **Maildir**: Used for reading and writing Maildir files, which are a directory structure for storing email messages.
- **IMAP4**: Connects to an IMAP4 server and allows for search and retrieval of emails, as well as appending new ones.
- **POP3**: Connects to a POP3 server and provides methods to retrieve and delete emails.

These examples demonstrate how to use the `mailbox` module to interact with different types of mailboxes in various formats. Each example includes comments that explain key operations and outputs for clarity.
