import os
from bs4 import BeautifulSoup

class AnyWebScraper():
    def __init__(self):
        pass

    def webScrape(self, url):
        """
        Input: url to web scrape
        Output: Return A BeautifulSoup object 
        """

        result = os.system("curl " + url + " > any-web-scraper.txt")
        
        while "any-web-scraper.txt" not in os.listdir():
            result = os.system("curl " + url + " > any-web-scraper.txt")
        
        file = open('any-web-scraper.txt', 'r', encoding='utf-8', errors='ignore')
        response = file.read()
        file.close()
        
        if "any-web-scraper.txt" in os.listdir():
            os.remove("any-web-scraper.txt")

        soup = BeautifulSoup(response, 'html.parser')
        return soup
