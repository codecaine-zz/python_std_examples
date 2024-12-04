# smtplib — SMTP protocol client

Here's an example of how you can use the `smtplib` module in Python:

```python
# Importing the smtplib module
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailClient:
    def __init__(self, host, port, username, password):
        """
        Initializes an EmailClient object.

        Args:
            host (str): The SMTP server hostname.
            port (int): The SMTP server port number.
            username (str): The sender's email address.
            password (str): The sender's email password.
        """
        self.host = host
        self.port = port
        self.username = username
        self.password = password

    def send_email(self, recipient, subject, body):
        """
        Sends an email to the specified recipient.

        Args:
            recipient (str): The recipient's email address.
            subject (str): The email subject.
            body (str): The email body.
        """
        try:
            # Create a message
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = recipient
            msg['Subject'] = subject

            # Attach the message body
            msg.attach(MIMEText(body, 'plain'))

            # Set up the SMTP connection
            server = smtplib.SMTP(self.host, self.port)
            server.starttls()
            server.login(msg['From'], self.password)

            # Send the email
            text = msg.as_string()
            server.sendmail(msg['From'], recipient, text)
            server.quit()

            print("Email sent successfully!")

        except Exception as e:
            print(f"Error sending email: {e}")

# Example usage:
if __name__ == "__main__":
    # Create an EmailClient object
    client = EmailClient('smtp.gmail.com', 587, 'your_email@gmail.com', 'your_password')

    # Send an email
    recipient = 'recipient@example.com'
    subject = 'Test Email'
    body = 'This is a test email sent using Python.'
    client.send_email(recipient, subject, body)
```

You can also use the `smtplib` module directly without creating a class:

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(host, port, username, password, recipient, subject, body):
    """
    Sends an email to the specified recipient.

    Args:
        host (str): The SMTP server hostname.
        port (int): The SMTP server port number.
        username (str): The sender's email address.
        password (str): The sender's email password.
        recipient (str): The recipient's email address.
        subject (str): The email subject.
        body (str): The email body.
    """
    try:
        # Create a message
        msg = MIMEMultipart()
        msg['From'] = username
        msg['To'] = recipient
        msg['Subject'] = subject

        # Attach the message body
        msg.attach(MIMEText(body, 'plain'))

        # Set up the SMTP connection
        server = smtplib.SMTP(host, port)
        server.starttls()
        server.login(msg['From'], password)

        # Send the email
        text = msg.as_string()
        server.sendmail(msg['From'], recipient, text)
        server.quit()

        print("Email sent successfully!")

    except Exception as e:
        print(f"Error sending email: {e}")

# Example usage:
if __name__ == "__main__":
    # Set up the SMTP connection
    host = 'smtp.gmail.com'
    port = 587
    username = 'your_email@gmail.com'
    password = 'your_password'

    recipient = 'recipient@example.com'
    subject = 'Test Email'
    body = 'This is a test email sent using Python.'
    send_email(host, port, username, password, recipient, subject, body)
```

Please replace `'your_email@gmail.com'` and `'your_password'` with your actual Gmail credentials. Also note that you may need to generate an App Password for less secure apps.
