from bs4 import BeautifulSoup
import requests

URL = 'https://onewheel.com/products/pint#purchase'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3876.0 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

# title = soup.find()

print(soup.prettify())