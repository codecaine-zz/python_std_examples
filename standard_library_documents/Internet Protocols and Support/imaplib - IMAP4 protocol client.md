# imaplib — IMAP4 protocol client

**IMAPlib: A Python Client for IMAP4 Protocol**
====================================================

The `imaplib` module is a Python interface to the Internet Message Access Protocol (IMAP) version 4, which is a standard for accessing and managing email messages on a remote server.

### Installation

You don't need to install anything as it's part of the Python Standard Library.

### Example Usage
```python
import imaplib

# Connect to the IMAP server
def connect_to_imap(server, username, password):
    """
    Establishes a connection to an IMAP server.

    Args:
        server (str): The hostname or IP address of the IMAP server.
        username (str): The username to use for authentication.
        password (str): The password to use for authentication.

    Returns:
        imaplib.IMAP4: An IMAP4 client object.
    """
    # Create an IMAP4 client object
    mail = imaplib.IMAP4(server)

    # Login to the IMAP server
    mail.login(username, password)

    return mail

# Search for emails with a specific subject or keyword
def search_for_emails(mail, subject=None, keyword=None):
    """
    Searches for emails on the IMAP server.

    Args:
        mail (imaplib.IMAP4): An IMAP4 client object.
        subject (str, optional): The subject of the email to search for. Defaults to None.
        keyword (str, optional): A keyword to search for in the email body or subject. Defaults to None.

    Returns:
        list: A list of message IDs matching the search criteria.
    """
    # Search for emails with a specific subject
    if subject:
        result = mail.search(None, 'SUBJECT', subject)
    else:
        result = mail.search(None, '*')

    # Check if any messages were found
    if result[0] != b'':
        return result[1].decode('utf-8').split()
    else:
        return []

# Fetch an email message by ID
def fetch_email(mail, msgid):
    """
    Fetches an email message from the IMAP server.

    Args:
        mail (imaplib.IMAP4): An IMAP4 client object.
        msgid (int or str): The message ID of the email to fetch.

    Returns:
        tuple: A tuple containing the email body and subject.
    """
    result = mail.fetch(str(msgid), '(BODY[TEXT])')
    return result[0].split('\n')

# Close the IMAP connection
def close_connection(mail):
    """
    Closes the IMAP connection.

    Args:
        mail (imaplib.IMAP4): An IMAP4 client object.
    """
    # Logout from the IMAP server
    mail.logout()

    # Close the connection to the IMAP server
    mail.close()
    mail.logout()

# Usage example
if __name__ == '__main__':
    # Connect to the IMAP server
    mail = connect_to_imap('imap.gmail.com', 'your_email@gmail.com', 'your_password')

    # Search for emails with a specific subject
    subject = 'Example Email'
    email_ids = search_for_emails(mail, subject)
    print(f"Found {len(email_ids)} email(s) with subject '{subject}':")
    for emailid in email_ids:
        print(f"- Message ID: {emailid}")

    # Fetch an email message by ID
    msgid = 1
    email_body, email_subject = fetch_email(mail, msgid)
    print(f"Email Subject: {email_subject}")
    print(f"Email Body:\n{email_body}")

    # Close the IMAP connection
    close_connection(mail)
```
This example demonstrates how to connect to an IMAP server, search for emails with a specific subject or keyword, fetch an email message by ID, and close the IMAP connection.

**Note**: This code snippet is just an illustration of the `imaplib` module's capabilities. You should replace `'your_email@gmail.com'`, `'your_password'`, and `'imap.gmail.com'` with your actual email credentials and IMAP server address.
