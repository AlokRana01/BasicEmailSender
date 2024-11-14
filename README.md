<h1>Summary </h1>
<p>This is an automated email sender that connects to Gmail's SMTP server for sending emails with attachments, which can be optional. To use it, one enters the sender's email, password, recipient email, subject, body, and optionally the attachment file path. <br>
It reads in the given parameters, creates a MIME email, attaches files if provided, and securely sends the email through Gmail's SMTP server, thus catching errors during execution.
This code is made with Python. </p><br>

<h1>How to Run?..</h1>
<h2>Prepare Your Environment</h2>
<p><b>Install Python:</b> Make sure Python (version 3.x) is installed. You can download it from python.org.<br>
<b>Enable Less Secure App Access or App Passwords:</b>
If using Gmail, you’ll need to generate an App Password for your email account, as Gmail blocks sign-ins from less secure applications by default. You can create an App Password in your Google Account Security settings if you have 2-Step Verification enabled.</p><br>

<h2>Install Required Packages</h2>
<p>All the necessary packages (smtplib, email, os) are part of Python's standard library, so you don’t need any additional installations.</p><br>

<h2>Save the Code</h2>
<p>Copy the code into a Python file. For example, name it auto_email_sender.py.</p><br>

<h2>Run the Script</h2>
- Open a terminal or command prompt.<br>
- Navigate to the directory where auto_email_sender.py is saved.<br>
- Run the script with:<br>
---> python AutoEmail.py

