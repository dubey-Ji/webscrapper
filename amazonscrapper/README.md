# Amazon Mobile Scraper

A simple Python script to scrape mobile phone data from Amazon.com within a specified price range.

## Prerequisites

Before running the script, make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

Install the required libraries using the following command:

```bash
pip install requests beautifulsoup4
```

## Usage
Clone this repository or download the amazon_scraper.py file.

Open a terminal and navigate to the directory containing the script.

Run the script:
```bash
python amazon_scraper.py
```
The script will fetch mobile phone data from Amazon.com with prices ranging from 15000 to 20000, extract the name, price, and specifications, and save the data to a CSV file (amazon_mobiles.csv).

## Customization
* If you want to scrape data for a different price range, modify the low-price and high-price parameters in the base_url variable in the script.

* Adjust the HTML parsing logic in the extract_data function if the structure of the Amazon page changes.

## Note
Web scraping should be done responsibly and in compliance with the terms of service of the website. Check the website's robots.txt file and terms of use to ensure you're not violating any rules.

## Disclaimer
Scraping Amazon's data is against their terms of service. This script is provided for educational purposes only. Ensure you have the right to scrape the data you are interested in.
