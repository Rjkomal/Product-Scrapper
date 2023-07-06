import requests
from bs4 import BeautifulSoup


base_url = 'https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_'

# Function to scrape product information from a single page
def scrape_page(page_number):
    url = base_url + str(page_number)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    products = soup.find_all('div', {'data-component-type': 's-search-result'})
    
    data = []
    
    for product in products:
        product_url = 'https://www.amazon.in' + product.find('a', {'class': 'a-link-normal'})['href']
        product_name = product.find('span', {'class': 'a-size-medium'}).text.strip()
        product_price = product.find('span', {'class': 'a-offscreen'}).text.strip()
        
        rating = product.find('span', {'class': 'a-icon-alt'})
        if rating:
            rating = rating.text.split()[0]
        else:
            rating = 'Not available'
        
        reviews = product.find('span', {'class': 'a-size-base'})
        if reviews:
            reviews = reviews.text.strip()
        else:
            reviews = 'Not available'
        
        data.append({
            'Product URL': product_url,
            'Product Name': product_name,
            'Product Price': product_price,
            'Rating': rating,
            'Number of Reviews': reviews
        })
    
    return data


# Scrape 20 pages of product listings
all_data = []
for page in range(1, 51):
    print('Scraping Page', page)
    page_data = scrape_page(page)
    all_data.extend(page_data)

    # Break the loop if the desired number of products (200) is reached
    if len(all_data) >= 200:
        break
    