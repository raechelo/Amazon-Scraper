import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.com/PAPAISON-SPORTS-Adjustable-Outdoor-Rollerblades/dp/B07MKSPYKW/ref=sr_1_1_sspa?crid=3SEQ3APTZR60X&keywords=rollerblades+women&qid=1567553431&s=gateway&sprefix=rollerblades+%2Caps%2C211&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFJRUdBUkxFWkhQRzcmZW5jcnlwdGVkSWQ9QTAyODA4NjMzN1pYQ0xLVDcyQkE5JmVuY3J5cHRlZEFkSWQ9QTA3MTA3ODAxWkw0QTNJVlNUM0c3JndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3876.0 Safari/537.36'}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

print()