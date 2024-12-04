# email — An email and MIME handling package

**Email Module Code Examples**
=====================================

The `email` module provides classes for creating, parsing, and manipulating emails.

### 1. Creating an Email Message

```python
# Import the email module
import email

# Create a message with text and HTML content
msg = email.message_from_string('Subject: Hello World\nFrom: test@example.com\nTo: test2@example.com\n\nHello World!\n\nThis is a test email.')
print(msg)

# Create a message with attachments
attachment_msg = email.mime.multipart.MIMEMultipart()
attachment_msg['From'] = 'test@example.com'
attachment_msg['To'] = 'test2@example.com'
attachment_msg['Subject'] = 'Test Email with Attachment'

body = email.mime.text.MIMEText('Hello World!')
attachment_msg.attach(body)

attachment = open('example.txt', 'rb')
part = email.mime.application.MIMEApplication(attachment.read(), _type='application/octet-stream')
attachment_msg.attach(part)
attachment.close()

# Send the message
server = email.SMTP('smtp.example.com', 587)  # replace with your SMTP server details
server.sendmail('test@example.com', 'test2@example.com', attachment_msg.as_string())
```

### 2. Parsing an Email Message

```python
import email

# Create a message from a file
msg = email.message_from_file('example.eml')

print("Subject: ", msg['Subject'])
for part in msg.walk():
    if part.get_content_type() == 'text/plain':
        body = part.get_payload()
        print(body)
```

### 3. Encoding and Decoding Email Content

```python
import email

# Create a message with text content
msg = email.message_from_string('Subject: Hello World\nFrom: test@example.com\nTo: test2@example.com\n\nHello World!\n\nThis is a test email.')
body = msg.get_payload()
print("Original Body: ", body)

# Encode the body using base64
encoded_body = body.encode().decode('base64')
print("Encoded Body: ", encoded_body)

# Decode the body using base64
decoded_body = encoded_body.encode('ascii').decode('base64')
print("Decoded Body: ", decoded_body)
```

### 4. Creating an Email with Attachments

```python
import email.mime

# Create a message with attachments
attachment_msg = email.mime.multipart.MIMEMultipart()
attachment_msg['From'] = 'test@example.com'
attachment_msg['To'] = 'test2@example.com'
attachment_msg['Subject'] = 'Test Email with Attachment'

body = email.mime.text.MIMEText('Hello World!')
attachment_msg.attach(body)

# Add an attachment
file_attachment = open('example.txt', 'rb')
part = email.mime.application.MIMEApplication(file_attachment.read(), _type='application/octet-stream')
attachment_msg.attach(part)
file_attachment.close()

print(attachment_msg.as_string())
```

### 5. Sending an Email using the SMTP Server

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Create a message with text content
msg = MIMEMultipart()
msg['From'] = 'test@example.com'
msg['To'] = 'test2@example.com'
msg['Subject'] = 'Test Email from SMTP Server'

body = MIMEText('Hello World! This is a test email.')
msg.attach(body)

# Create an SMTP server connection
server = smtplib.SMTP('smtp.example.com', 587)
server.starttls()
server.login(msg['From'], 'password')

try:
    server.sendmail(msg['From'], msg['To'], msg.as_string())
except Exception as e:
    print(f"Error: {e}")
finally:
    server.quit()
```

Note that you should replace the SMTP server details (`smtp.example.com`, port 587, and `test@example.com` password) with your actual email provider's settings.
