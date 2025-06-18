# email - An email and MIME handling package
## Table of Contents

1. [Example 1: Creating an Email Message](#example-1-creating-an-email-message)
2. [Example 2: Parsing an Email Message](#example-2-parsing-an-email-message)
3. [Example 3: Sending an Email using SMTP](#example-3-sending-an-email-using-smtp)
4. [Example 4: Attaching Files to Email](#example-4-attaching-files-to-email)
5. [Example 5: Handling Email Attachments](#example-5-handling-email-attachments)
6. [Example 6: Filtering Emails from a Mailbox](#example-6-filtering-emails-from-a-mailbox)
7. [Example 7: Handling Email Addresses](#example-7-handling-email-addresses)



The `email` module in Python provides a comprehensive set of tools for parsing, creating, modifying, and sending email messages. Below are several examples that demonstrate how to use this module for different tasks.

### Example 1: Creating an Email Message

```python
from email.message import EmailMessage

# Create a new email message object
msg = EmailMessage()

# Set the sender and recipient
msg['From'] = 'sender@example.com'
msg['To'] = 'receiver@example.com'

# Set the subject of the email
msg['Subject'] = 'Hello, World!'

# Add the body of the email as a plain text
msg.set_content('This is a simple test email message.')

# Optionally, add HTML content to the email
html_message = '''
<html>
<head></head>
<body>
<p>This is a <strong>test</strong> email message with HTML content.</p>
</body>
</html>
'''
msg.add_alternative(html_message, subtype='html')

# Print the full email message for debugging purposes
print(msg)

# Save the email to a file
with open('email.txt', 'w') as f:
    f.write(msg.as_string())
```

### Example 2: Parsing an Email Message

```python
from email.message import EmailMessage

# Read the email from a file or any other source
with open('email.txt', 'r') as f:
    raw_email = f.read()

# Create an EmailMessage object from the raw email data
msg = EmailMessage.from_string(raw_email)

# Access header information
print(f'From: {msg["From"]}')
print(f'To: {msg["To"]}')
print(f'Subject: {msg["Subject"]}')

# Check if there is any plain text content
if msg.is_multipart() and 'plain' in msg['Content-Type']:
    for part in msg.walk():
        if part.get_content_type() == 'text/plain':
            print(part.get_payload(decode=True).decode('utf-8'))

# Check if there is any HTML content
elif 'html' in msg['Content-Type']:
    for part in msg.walk():
        if part.get_content_type() == 'text/html':
            print(part.get_payload(decode=True).decode('utf-8'))
```

### Example 3: Sending an Email using SMTP

```python
import smtplib
from email.message import EmailMessage

# Define the email message object
msg = EmailMessage()
msg['From'] = 'sender@example.com'
msg['To'] = 'receiver@example.com'
msg['Subject'] = 'Hello, World!'

# Set the body of the email as a plain text
msg.set_content('This is a test email sent using SMTP.')

# Connect to an SMTP server and send the email
with smtplib.SMTP('smtp.example.com', 587) as server:
    server.starttls()
    server.login('sender@example.com', 'password')
    server.send_message(msg)
```

### Example 4: Attaching Files to Email

```python
import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Define the email message object
msg = EmailMessage()
msg['From'] = 'sender@example.com'
msg['To'] = 'receiver@example.com'
msg['Subject'] = 'Hello, World!'

# Set the body of the email as a plain text
msg.set_content('This is a test email with an attachment.')

# Create a multipart message to hold both the text and attachments
multipart_msg = MIMEMultipart()
multipart_msg.attach(msg)

# Attach a file
filename = 'file_to_attach.txt'
attachment = open(filename, "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', f"attachment; filename= {filename}")

multipart_msg.attach(part)

# Connect to an SMTP server and send the email
with smtplib.SMTP('smtp.example.com', 587) as server:
    server.starttls()
    server.login('sender@example.com', 'password')
    text = multipart_msg.as_string()
    server.sendmail('sender@example.com', 'receiver@example.com', text)
```

### Example 5: Handling Email Attachments

```python
from email.message import EmailMessage
import os

# Define the email message object
msg = EmailMessage()
msg['From'] = 'sender@example.com'
msg['To'] = 'receiver@example.com'
msg['Subject'] = 'Hello, World!'

# Set the body of the email as a plain text
msg.set_content('This is a test email with an attachment.')

# Define a directory containing files to attach
directory = 'files_to_attach'
attachments = [os.path.join(directory, f) for f in os.listdir(directory)]

for filename in attachments:
    # Create a MIMEBase object for each file
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((open(filename, "rb")).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f"attachment; filename= {filename}")

    # Attach the MIMEBase object to the email message
    msg.attach(part)

# Connect to an SMTP server and send the email
with smtplib.SMTP('smtp.example.com', 587) as server:
    server.starttls()
    server.login('sender@example.com', 'password')
    text = msg.as_string()
    server.sendmail('sender@example.com', 'receiver@example.com', text)
```

### Example 6: Filtering Emails from a Mailbox

```python
import imaplib
from email.parser import BytesParser

# Connect to an IMAP server
imap = imaplib.IMAP4_SSL('imap.example.com')
imap.login('username', 'password')

# Select the mailbox you want to search in (e.g., INBOX)
imap.select('INBOX')

# Search for emails with a specific keyword in the subject line
search_result, data = imap.search(None, '(SUBJECT "Hello")')
email_ids = data[0].split()

for email_id in email_ids:
    # Fetch the raw email content
    _, msg_bytes = imap.fetch(email_id, "(RFC822)")
    msg_str = msg_bytes[0][1]

    # Parse the raw email into an EmailMessage object
    msg = BytesParser().parsemsg(msg_str)

    # Process the message (e.g., print the subject)
    print(f'Subject: {msg["Subject"]}')

# Close and logout from the IMAP server
imap.close()
imap.logout()
```

### Example 7: Handling Email Addresses

```python
from email.utils import parseaddr, formataddr

# Define a list of email addresses
email_list = [
    ('Alice', 'alice@example.com'),
    ('Bob', 'bob@example.org')
]

# Print each email address in the list
for name, email in email_list:
    # Parse the name and email into a tuple
    parsed_addr = parseaddr(f"{name} <{email}>")
    
    # Format the name and email back into a string
    formatted_email = formataddr(parsed_addr)
    
    print(formatted_email)

# Validate an email address
email_to_validate = 'invalid-email'
if parseaddr(email_to_validate):
    print(f"'{email_to_validate}' is a valid email address.")
else:
    print(f"'{email_to_validate}' is not a valid email address.")
```

These examples cover various aspects of handling emails using the `email` module, including creating, parsing, sending, attaching files, filtering emails from a mailbox, and manipulating email addresses. Each example is designed to be clear and self-contained, with comments explaining each step for better understanding.
