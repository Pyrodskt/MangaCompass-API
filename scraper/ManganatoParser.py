import requests
from bs4 import BeautifulSoup
import re
import time

class ManganatoParser():
    def __init__(self, url, current):
        self.name = "Manganato Parser"
        self.url = url
        self.current = current
        self.results = []
        self.pages = []
        self.search(self.url)

    def search(self, url):
        req = requests.get(url)
        page = req.content
        soup = BeautifulSoup(page, features="html.parser")
        result = soup.find_all("a", {"class": "chapter-name text-nowrap"})
        for res in result:
            try:
                self.results.append(res.text)
                # time.sleep(2)
            except Exception as e:
                print("error == ", e)

