import requests
from bs4 import BeautifulSoup
import smtplib

BUY_PRICE = 30
my_email = "pratikgadkar1996@gmail.com"
password = "YOUR APP PASSKEY"
URL= "https://www.amazon.co.uk/gp/product/B0BTJD6LCL/ref=ox_sc_act_title_1?smid=A3P5ROKL5A1OLE&psc=1"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 "
                  "Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
res = requests.get(url=URL, headers=headers)
html_content = res.text

soup = BeautifulSoup(html_content, "html.parser")
price = soup.find(class_="a-offscreen").get_text()
title = soup.find(id="productTitle").get_text().strip()
# print(title)
price_without_currency = price.split("£")[1]
price_as_float = float(price_without_currency)
# print(price_as_float)

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="pratik38gadkar@gmail.com",
                            msg=f"Subject:Amazon Price Alert!\n\n{message} \n\n{URL}".encode("utf-8")
                            )
        connection.close()
