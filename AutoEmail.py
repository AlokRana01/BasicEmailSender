

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

def send_email(sender_email, sender_password, to_address, subject, body, attachment_path=None):
    # Set up the MIME
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = to_address
    message['Subject'] = subject

    # Attach the body with the msg instance
    message.attach(MIMEText(body, 'plain'))

    # Check if there's an attachment
    if attachment_path and os.path.isfile(attachment_path):
        # Add attachment to the email
        with open(attachment_path, "rb") as attachment_file:
            mime_base = MIMEBase("application", "octet-stream")
            mime_base.set_payload(attachment_file.read())
            encoders.encode_base64(mime_base)
            mime_base.add_header(
                "Content-Disposition",
                f"attachment; filename={os.path.basename(attachment_path)}",
            )
            message.attach(mime_base)

    # Set up the SMTP server
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Enable security
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to_address, message.as_string())
            print(f"Email sent to {to_address}")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Gather user input
sender_email = input("Enter your email address: ")
sender_password = input("Enter your app password: ")
recipient = input("Enter recipient's email address: ")
subject = input("Enter the subject of the email: ")
body = input("Enter the body of the email: ")
attachment_path = input("Enter the file path for the attachment (leave blank if none): ")

# Call the send_email function
send_email(sender_email, sender_password, recipient, subject, body, attachment_path if attachment_path else None)
