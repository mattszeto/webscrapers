import requests
from bs4 import BeautifulSoup
import smtplib
import time

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()

server.login('USERNAME', 'GENERATED_PASS')

subject = "Test Email"
body = "Hello World"

server.sendmail("SENDER", "RECEIVER", msg)
print('Email sent')
server.quit()
