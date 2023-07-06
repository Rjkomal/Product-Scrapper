# Amazon Product Scraper

This project is a Python-based web scraper for extracting product information from Amazon.

## Description

The Amazon Product Scraper scrapes product details from Amazon's website, including product URLs, names, prices, ratings, number of reviews, descriptions, ASIN, product descriptions, and manufacturers. It consists of two parts:

- Part 1: Scraping product listings
- Part 2: Fetching additional information from product URLs

## Requirements

- Python 3.7 or above
- Requests library (`pip install requests`)
- BeautifulSoup library (`pip install beautifulsoup4`)
- Pandas library (`pip install pandas`)

## Usage

1. Run `part1.py` to scrape the product listings and generate a CSV file with the scraped data.

2. Run `part2.py` to visit the product URLs obtained in Part 1, extract additional information, and update the CSV file.

3. The final output will be stored in a CSV file named `amazon_products.csv`.

## Configuration

- Modify the `base_url` variable in `part1.py` to specify the desired Amazon search URL.

## Screenshots 

![Screenshot (17)](https://github.com/Rjkomal/Product-Scrapper/assets/69381382/335779c0-b0fc-489b-81ea-bc03c264b9d5)

![Screenshot (16)](https://github.com/Rjkomal/Product-Scrapper/assets/69381382/84ddc015-53f5-496d-bd6c-53a8cbef0c72)




