import requests
from bs4 import BeautifulSoup
import smtplib
import time

# amazon product URL
URL = 'AMAZON URL'
# google User-Agent in your browser and paste here
user_agent = 'USER AGENT'
# target price
target_price = 200


headers = {
    "User-Agent": user_agent}


def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = price[:-3]

    # price target
    if(converted_price < target_price):
        send_email()

# need to enable 2-step verification and enable app passwords


def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
# REPLACE USERNAME AND GENERATED PASSWORD HERE
    server.login('USERNAME', 'GENERATED PASSWORD')

    subject = 'Price has changed'
    body = 'Check the amazon link: ' + URL
    msg = f"Subject: {subject}\n\n{body}"

# REPLACE SENDER EMAIL AND RECEIVER EMAIL
    server.sendmail(
        'SENDER EMAIL',

        'RECEIVER EMAIL',
        msg
    )
    print('Email sent')
    server.quit()


while(True):
    check_price()
    time.sleep(60 * 60 * 12)
