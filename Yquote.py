from bs4 import BeautifulSoup
import requests
import random

class Yquote():
    def __init__(self):
        self.response = ""
        self.tag = ""
        self.website_url = ""

    def generate_url(self, tag):
        self.tag = tag
        self.website_url = 'https://www.yourquote.in/tags/' + self.tag + '/quotes'

    def get_sourcecode(self, website_url):
        return requests.get(website_url).content

    def get_quote(self, tag):
        self.generate_url(tag)
        source_code = self.get_sourcecode(self.website_url)
        soup = BeautifulSoup(source_code, 'lxml')
        quotes = soup.find_all('img', class_="quote-media-section")
        
        quotes_list = []
        for quote in quotes:
            quotes_list.append(quote['title'])
        
        return quotes_list[random.randint(0, len(quotes)-1)]


# Usage

# yourquote = Yquote()
# quote = yourquote.get_quote('2019')
# print(quote)