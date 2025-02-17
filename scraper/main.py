import csv
from pymongo import MongoClient
import sys
import requests
from bs4 import BeautifulSoup

# Send a GET request to the specified URL
response = requests.get('https://www.hostinger.com/tutorials/how-to-run-a-python-script-in-linux')

# Parse the HTML content of the response using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find the first <h1> tag in the HTML and print its text content
first_header = soup.find('h1')
print('first h1 tag :', first_header.text)

# Find all <a> tags (links) in the HTML and print their href attributes
all_links = soup.find_all('a')
print('all a tags hrefs :')
for link in all_links:
    print(link.get('href'))

# Print the text and href attribute of the first <a> tag
first_link = all_links[0]
print('first link text :', first_link.text)
print('first link href :', first_link.get('href'))

# Find a <div> with class 'd-flex' and print the text of its first <span> child, if it exists
specific_div = soup.find('div', class_='d-flex')
if specific_div:
    child_element = specific_div.find('span')
    if child_element:
        print('text of child span in div', child_element.text)
else:
    print('the div is not found')

# If the first <h1> tag is found, print its parent's tag name and the tag name of its next sibling
if first_header:
    parent_element = first_header.parent
    print('parent of first h1 is ', parent_element.name)
    next_sibling = first_header.find_next_sibling()
    print('next sibling of first h1 : ', next_sibling.name if next_sibling else 'no next sibling')

# Prepare data to store in CSV and MongoDB
data_to_store = {
    'first_h1': first_header.text,
    'first_link_text': first_link.text,
    'first_link_href': first_link.get('href')
}

# Define the CSV file name
csv_file = 'scraped.data.csv'

# Write the data to a CSV file
with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=data_to_store.keys())
    writer.writeheader()
    writer.writerow(data_to_store)
    print('data stored in csv : ', csv_file)

# Try to connect to MongoDB and insert the data into a collection
try:
    client = MongoClient('mongodb://localhost:27017/')# change this part
    db = client['scraping_db']
    collection = db['scraped_data']
    collection.insert_one(data_to_store)
    print('Data saved to MongoDB collection: scraped_data')
except Exception as e:
    print('Error:', e)
    print('Failed to connect to MongoDB. Exiting...')
    sys.exit(1)