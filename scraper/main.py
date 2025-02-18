import requests
from bs4 import BeautifulSoup
import re

from urllib.parse import urlparse
url='https://www.geeksforgeeks.org/python-programming-language-tutorial'
keyword='python'

def get_Html():
    try:
        response=requests.get(url)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
            print('error fetching url:',e)
            return None

def get_text_and_count(response):
     html_content=response.text
     count=html_content.count('python')
     return count


def main():
     response=get_Html()
     if response:
        count=get_text_and_count(response)
        print(f'the word {keyword} appears {count} in the page')

if __name__=='__main__':
    main()