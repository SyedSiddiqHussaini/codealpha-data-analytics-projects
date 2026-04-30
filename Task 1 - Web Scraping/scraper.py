import requests
from bs4 import BeautifulSoup
import csv

# URL of the website
url = "https://books.toscrape.com/catalogue/category/books/childrens_11/index.html"

# 1. Fetch the webpage
response = requests.get(url)

# 2. Create the 'soup' object
soup = BeautifulSoup(response.text, 'html.parser')

# 3. Locate the 'containers'
# On this site, each quote is inside a <div> with the class 'quote'
quote_elements = soup.find_all('div', class_='quote')

# 4. Extract data and store it in a list
scraped_data = []

for quote in quote_elements:
    # Extract the text of the quote
    text = quote.find('span', class_='text').text
    
    # Extract the author's name
    author = quote.find('small', class_='author').text
    
    # Extract the tags (joining multiple tags with a comma)
    tags_list = quote.find_all('a', class_='tag')
    tags = ", ".join([tag.text for tag in tags_list])
    
    # Append to our list as a dictionary
    scraped_data.append({
        'Text': text,
        'Author': author,
        'Tags': tags
    })

for i in range(1, 6): # To scrape pages 1 through 5
    url = f"http://quotes.toscrape.com/page/{i}/"
    # ... rest of the code ...

# 5. Save to a CSV file
with open('quotes_dataset.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Text', 'Author', 'Tags'])
    writer.writeheader()
    writer.writerows(scraped_data)

print(f"Success! Successfully scraped {len(scraped_data)} quotes.")