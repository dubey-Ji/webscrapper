import requests
from bs4 import BeautifulSoup
import csv

def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve HTML content. Status code: {response.status_code}")
        return None

def extract_data(html):
    soup = BeautifulSoup(html, 'html.parser')

    # Find the container that holds the product details
    products = soup.find_all('div', class_='s-result-item')

    data_to_save = []

    for product in products:
        # Extract name, price, and specifications (if available)
        name = product.find('span', class_='a-text-normal')
        price = product.find('span', class_='a-offscreen')
        specifications = product.find('div', class_='a-row a-size-base a-color-secondary')

        if name and price:
            name_text = name.text.strip()
            price_text = price.text.strip()

            # Extracting specifications if available, otherwise use 'N/A'
            specifications_text = specifications.text.strip() if specifications else 'N/A'

            data_to_save.append([name_text, price_text, specifications_text])

    return data_to_save

def save_to_csv(data):
    csv_file = 'amazon_mobiles.csv'

    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Write header
        writer.writerow(['Name', 'Price', 'Specifications'])

        # Write data to CSV
        writer.writerows(data)

        print(f'Data has been successfully written to {csv_file}')

def main():
    base_url = 'https://www.amazon.in/s?k=mobile&rh=n%3A1389432031&low-price=15000&high-price=20000'
    html = get_html(base_url)

    if html:
        extracted_data = extract_data(html)
        save_to_csv(extracted_data)

if __name__ == '__main__':
    main()
