# Amazon Price Tracker with Email Alerts

This Python script monitors the price of a product on Amazon and sends an email alert if the price drops below a specified threshold.

## Overview

The Amazon Price Tracker is a simple script that allows you to track the price of a product on Amazon and receive email notifications when the price falls below a certain amount. It utilizes web scraping techniques to extract product information and sends email alerts using SMTP with Gmail.

## How It Works

1. **Web Scraping**: The script makes an HTTP GET request to the specified Amazon product URL using `requests` library and extracts the HTML content of the page.
2. **Parsing HTML**: It uses `BeautifulSoup` to parse the HTML content and extract the product title and current price from the page.
3. **Price Comparison**: The extracted price is compared with a predefined `BUY_PRICE` threshold.
4. **Sending Email Alert**: If the price drops below the threshold, the script sends an email alert using SMTP with Gmail.

## Features

- **Dynamic Price Monitoring**: The script checks the current price of the specified Amazon product dynamically.
- **Email Alerts**: Receive email notifications when the price drops below the desired threshold.
- **Customizable Parameters**: Easily customize the product URL, desired price threshold (`BUY_PRICE`), and email settings directly in the script.

## Usage

1. **Prerequisites**:
   - Python 3.x installed on your system.
   - Gmail account with "Less Secure Apps" setting enabled or generate an "App Password" for authentication.

2. **Installation**:
   - Clone this repository:
     ```bash
     git clone https://github.com/your_username/priceTracker.git
     ```
   - Install required Python packages:
     ```bash
     pip install requests beautifulsoup4
     ```

3. **Configuration**:
   - Open `amazon_price_tracker.py` script.
   - Replace `URL` with the Amazon product URL you want to track.
   - Set `BUY_PRICE` to your desired price threshold.
   - Update `my_email` and `password` with your Gmail credentials or App Password.

4. **Execution**:
   - Run the script in your Python environment:
     ```bash
     python amazon_price_tracker.py
     ```
   - Enter your Gmail password when prompted (or use an App Password).

## Customization

- **Email Settings**: Customize the email sender and recipient addresses.
- **Product URL**: Track prices of different Amazon products by updating the `URL` in the script.
- **Threshold**: Adjust the `BUY_PRICE` threshold to receive alerts when the price drops below a specific amount.

## Notes

- Ensure your Gmail credentials are kept secure and use an "App Password" for authentication.
- This project is for educational purposes only. Use responsibly and respect Amazon's Terms of Service regarding web scraping.


<img width="605" alt="image" src="https://github.com/patreeck/priceTracker/assets/163764755/6e623a65-3a73-4f2c-978d-9794c5f7e906">

