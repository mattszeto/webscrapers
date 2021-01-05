import smtplib
import ssl
import credentials

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = credentials.login['SENDER_EMAIL']  # Enter your address
receiver_email = credentials.login['RECEIVER_EMAIL']  # Enter receiver address
password = credentials.login['PASSWORD']
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
