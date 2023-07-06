import requests
from bs4 import BeautifulSoup
import pandas as pd
from part1 import all_data

# Function to scrape additional information from a product page
def scrape_product_page(product_url):
    response = requests.get(product_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    description_elem = soup.find('div', {'id': 'feature-bullets'})
    description = description_elem.text.strip() if description_elem else 'Not available'

    asin_elem = soup.find('th', string='ASIN')
    asin = asin_elem.find_next('td').text.strip() if asin_elem else 'Not available'

    product_description_elem = soup.find('div', {'id': 'productDescription'})
    product_description = product_description_elem.text.strip() if product_description_elem else 'Not available'

    manufacturer_elem = soup.find('th', string='Manufacturer')
    manufacturer = manufacturer_elem.find_next('td').text.strip() if manufacturer_elem else 'Not available'

    return {
        'Description': description,
        'ASIN': asin,
        'Product Description': product_description,
        'Manufacturer': manufacturer
    }



# Scrape additional information for each product URL
for i, data in enumerate(all_data):
    print('Scraping Product', i+1)
    product_url = data['Product URL']
    product_info = scrape_product_page(product_url)
    data.update(product_info)


# Export data to CSV
df = pd.DataFrame(all_data)
df.to_csv('amazon_products.csv', index=False)
