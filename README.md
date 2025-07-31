
Project Title: Amazon Price Tracker

Introduction
This project is a simple web scraping tool written in Python that tracks the price of a specific product on Amazon Turkey and logs the data to a CSV file. The script checks the price every 24 hours and appends the product's title, price, and the date to a file named AmazonWebScraping.csv.

Features

Daily Price Check: The script is set to run and check the price once every 24 hours (86400 seconds).


Data Logging: It saves the product name, its price, and the date into a CSV file.


Beautiful Soup & Requests: It uses the requests library to connect to the Amazon URL and Beautiful Soup to parse the HTML content to find the product title and price.

How to Use
Prerequisites: Ensure you have Python installed. You'll also need the requests and BeautifulSoup4 libraries. You can install them using pip:

Bash

pip install requests beautifulsoup4
Configuration:

Open the project.py file.

Change the URL variable to the Amazon product page you wish to track.

Update the headers dictionary with your User-Agent to avoid being blocked.

Run the script:

Bash
python project.py
The script will start and run indefinitely, updating the AmazonWebScraping.csv file daily.

File Structure
project.py: The main Python script for web scraping.
AmazonWebScraping.csv: The CSV file where the product data (Title, Price, Date) is stored.
