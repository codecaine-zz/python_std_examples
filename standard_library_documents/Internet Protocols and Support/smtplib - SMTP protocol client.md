# smtplib - SMTP protocol client
## Table of Contents

1. [Example 1: Sending a Simple Email Using `smtplib`](#example-1-sending-a-simple-email-using-smtplib)
2. [Explanation:](#explanation)
3. [Example 2: Sending an HTML Email Using `smtplib`](#example-2-sending-an-html-email-using-smtplib)
4. [Explanation:](#explanation)
5. [Example 3: Sending an Email with Attachments Using `smtplib`](#example-3-sending-an-email-with-attachments-using-smtplib)
6. [Explanation:](#explanation)
7. [Example 4: Sending Email with SMTP Authentication via Gmail](#example-4-sending-email-with-smtp-authentication-via-gmail)
8. [Explanation:](#explanation)



Below are comprehensive code examples for using the `smtplib` module in Python, covering various functionalities such as sending simple emails, handling exceptions, and configuring SMTP servers with authentication.

### Example 1: Sending a Simple Email Using `smtplib`

```python
import smtplib
from email.mime.text import MIMEText

def send_simple_email():
    # Set up the SMTP server details
    smtp_server = 'smtp.example.com'
    port = 587
    sender_email = 'your-email@example.com'
    receiver_email = 'receiver-email@example.com'
    password = 'your-password'

    try:
        # Create a secure SSL context
        context = smtplib.SMTP(smtp_server, port)
        
        # Start TLS encryption
        context.starttls()
        
        # Log in to the SMTP server
        context.login(sender_email, password)

        # Create a MIMEText object for the email content
        message = MIMEText('Hello, this is a test email sent from Python using smtplib.')
        message['Subject'] = 'Test Email'
        message['From'] = sender_email
        message['To'] = receiver_email

        # Send the email
        context.sendmail(sender_email, receiver_email, message.as_string())
        
        print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the connection
        context.quit()

if __name__ == "__main__":
    send_simple_email()
```

### Explanation:

1. **SMTP Server Setup**: Define the SMTP server address, port, sender's email, receiver's email, and password.
2. **SSL Context**: Create an SSL context to secure the connection.
3. **Start TLS**: Establish a secure connection using TLS.
4. **Login**: Authenticate with the SMTP server using the sender's credentials.
5. **Create Email Content**: Use `MIMEText` to create a simple email message.
6. **Send Email**: Send the email using `context.sendmail()`.
7. **Error Handling and Cleanup**: Include exception handling and ensure the connection is closed in a `finally` block.

### Example 2: Sending an HTML Email Using `smtplib`

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_html_email():
    # Set up the SMTP server details
    smtp_server = 'smtp.example.com'
    port = 587
    sender_email = 'your-email@example.com'
    receiver_email = 'receiver-email@example.com'
    password = 'your-password'

    try:
        # Create a secure SSL context
        context = smtplib.SMTP(smtp_server, port)
        
        # Start TLS encryption
        context.starttls()
        
        # Log in to the SMTP server
        context.login(sender_email, password)

        # Create a MIMEMultipart object for the email content
        message = MIMEMultipart('alternative')
        message['Subject'] = 'Test HTML Email'
        message['From'] = sender_email
        message['To'] = receiver_email

        # Create and attach plain text version of the email
        text_part = MIMEText('This is a test email sent from Python using smtplib.', 'plain')
        message.attach(text_part)

        # Create and attach HTML version of the email
        html_part = MIMEText('<html><body><h1>Hello, this is a <b>test</b> email sent from Python using smtplib.</h1></body></html>', 'html')
        message.attach(html_part)

        # Send the email
        context.sendmail(sender_email, receiver_email, message.as_string())
        
        print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the connection
        context.quit()

if __name__ == "__main__":
    send_html_email()
```

### Explanation:

1. **SMTP Server Setup**: Similar to the simple email example.
2. **MIME Multipart**: Use `MIMEMultipart` to create a multipart email message that can contain both plain text and HTML content.
3. **Attach Content**: Attach each part of the email using `attach()`.
4. **Error Handling and Cleanup**: Same as in the simple email example.

### Example 3: Sending an Email with Attachments Using `smtplib`

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email_with_attachment():
    # Set up the SMTP server details
    smtp_server = 'smtp.example.com'
    port = 587
    sender_email = 'your-email@example.com'
    receiver_email = 'receiver-email@example.com'
    password = 'your-password'

    try:
        # Create a secure SSL context
        context = smtplib.SMTP(smtp_server, port)
        
        # Start TLS encryption
        context.starttls()
        
        # Log in to the SMTP server
        context.login(sender_email, password)

        # Create a MIMEMultipart object for the email content
        message = MIMEMultipart()
        message['Subject'] = 'Test Email with Attachment'
        message['From'] = sender_email
        message['To'] = receiver_email

        # Attach plain text version of the email
        text_part = MIMEText('This is a test email sent from Python using smtplib.', 'plain')
        message.attach(text_part)

        # Specify the file to attach
        filename = "example.txt"
        attachment_path = f"/path/to/{filename}"

        with open(attachment_path, "rb") as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f"attachment; filename= {filename}")

            message.attach(part)

        # Send the email
        context.sendmail(sender_email, receiver_email, message.as_string())
        
        print("Email sent successfully with attachment!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the connection
        context.quit()

if __name__ == "__main__":
    send_email_with_attachment()
```

### Explanation:

1. **SMTP Server Setup**: Same as previous examples.
2. **MIME Multipart**: Use `MIMEMultipart` for email content and attachment.
3. **Attach Plain Text**: Attach a plain text part to the email.
4. **Attach File**: Open the file, encode it in base64, and attach it using `MIMEBase`.
5. **Error Handling and Cleanup**: Same as previous examples.

### Example 4: Sending Email with SMTP Authentication via Gmail

```python
import smtplib
from email.mime.text import MIMEText

def send_email_via_gmail():
    # Set up the SMTP server details for Gmail
    smtp_server = 'smtp.gmail.com'
    port = 587
    sender_email = 'your-email@gmail.com'
    receiver_email = 'receiver-email@example.com'
    password = 'your-app-password'

    try:
        # Create a secure SSL context
        context = smtplib.SMTP(smtp_server, port)
        
        # Start TLS encryption
        context.starttls()
        
        # Log in to the SMTP server with Gmail's credentials
        context.login(sender_email, password)

        # Create a MIMEText object for the email content
        message = MIMEText('Hello, this is a test email sent from Python using smtplib via Gmail.')
        message['Subject'] = 'Test Email via Gmail'
        message['From'] = sender_email
        message['To'] = receiver_email

        # Send the email
        context.sendmail(sender_email, receiver_email, message.as_string())
        
        print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the connection
        context.quit()

if __name__ == "__main__":
    send_email_via_gmail()
```

### Explanation:

1. **SMTP Server Setup**: For Gmail, specify `'smtp.gmail.com'` and use port `587`.
2. **Gmail App Password**: Use a 2FA app password instead of your regular email password.
3. **Login**: Log in using the sender's Gmail credentials.

These examples cover basic functionality for sending emails using `smtplib`, including simple text, HTML, attachments, and handling SMTP authentication for popular services like Gmail. Adjust the server details and credentials as needed for your specific use case.
