import requests
from bs4 import BeautifulSoup
import re
import json

class JapscansParser():
    def __init__(self, url, current):
        self.name = "Japscans Parser"
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
        for i in result:
            print(i.text)
        
    
    def write_output(self, content):
        with open("output.txt", "w") as w:
            w.writelines(content)

datas = [
        {
            "title": "One punch Man",
            "url": "https://chapmanganato.com/manga-wd951838",
            "list": [],
            "current": "Chapter 186"
        },
        {
            "title": "One Piece",
            "url": "https://chapmanganato.com/manga-aa951409",
            "list": [],
            "current": "One Piece 1025 VF: Dragons jumeaux"
        },
        {
            "title": "Dr. Stone",
            "url": "https://chapmanganato.com/manga-yz975382",
            "list": [],
            "current": "Extra.232"
        },
        {
            "title": "Black Clover",
            "url": "https://chapmanganato.com/manga-eh951664",
            "list": [],
            "current": "Chapter 363: Standing In The Way"
        }
    ]


i = datas[2]
scraper = JapscansParser(i['url'], i['current'])
