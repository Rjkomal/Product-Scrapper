# Amazon Product Scraper

#### This project is a Python-based web scraper for extracting product information from Amazon.

## Description

#### The code is a Python-based web scraper that extracts product information from Amazon. It consists of two parts: Part 1 and Part 2.

In Part 1, the code scrapes product listings from the specified Amazon URL. It retrieves the URLs, names, prices, ratings, and number of reviews for each product. The scraping is performed by sending HTTP requests to the Amazon website and using BeautifulSoup to parse the HTML response and extract the desired information. The code iterates over multiple pages of product listings to ensure a sufficient number of products are scraped.

In Part 2, the code uses the product URLs obtained from Part 1 to visit each product page and fetch additional information. It retrieves the description, ASIN, product description, and manufacturer details for each product. Similar to Part 1, it sends HTTP requests to the product pages, parses the HTML response, and extracts the required information using BeautifulSoup.

The code then combines the scraped data from Part 1 and the additional information from Part 2 into a single dataset. It stores the data in a CSV file named `amazon_products.csv` using the Pandas library.

The logic of the code involves navigating through multiple pages of product listings, extracting relevant information from HTML elements, and visiting individual product pages to gather more details. It utilizes HTTP requests, HTML parsing, and data manipulation techniques to achieve the scraping and data processing tasks.

Overall, the code showcases web scraping techniques, data extraction, and data aggregation to provide a comprehensive dataset of products from Amazon, including URLs, names, prices, ratings, reviews, descriptions, ASIN, product descriptions, and manufacturers.

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




