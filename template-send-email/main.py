import smtplib
import ssl
import credentials
from datetime import date

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = credentials.login['SENDER_EMAIL']  # Enter your address
receiver_email = credentials.login['RECEIVER_EMAIL']  # Enter receiver address
password = credentials.login['PASSWORD']

today = date.today().strftime("%m/%d/%Y")


plain_text_message = """\
Subject: Test - Synology NAS

This message is sent from Synology NAS using Python.

""" + today

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, plain_text_message)
