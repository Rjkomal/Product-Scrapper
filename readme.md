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

## Notes

- The code provided is for educational purposes only. Use responsibly and ensure compliance with website scraping guidelines and legal requirements.

## License

This project is licensed under the [MIT License](LICENSE).

