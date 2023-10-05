import os
import shutil
import random
import platform
import tarfile
import gdown
import time
from bs4 import BeautifulSoup
        
class AnyWebScraper():
    def __init__(self):
        pass
    
    def start(self):
        operating_sys = platform.system().lower()
        self.get_curl_impersonate(operating_sys)
        
        while "curl-impersonate.zip" in os.listdir():
            os.remove("curl-impersonate.zip")
    
    def stop(self):
        while "curl-impersonate" in os.listdir():
            shutil.rmtree("curl-impersonate")
        
    def get_curl_impersonate(self, operating_system):
        if operating_system == "linux":
            url = "https://drive.google.com/uc?id=1bQ4pEsd-Q0buvK5Zb97rOtIGcbBvPaGh"
    
        if operating_system == "windows":
            url = "https://drive.google.com/uc?id=1D-XsDxQsk6-LSsAxPA2RcWTKKhLvio47"

        if operating_system == "darwin":
            url = "https://drive.google.com/uc?id=1_HXnsfifSibtweMEAXGtOgRo1cbsEHzS"

        output = "curl-impersonate.zip"
        gdown.download(url, output, quiet=True)
        while output not in os.listdir():
            time.sleep(1)

        file = tarfile.open(output) 
        file.extractall('./curl-impersonate') 
        file.close()

        while "curl-impersonate.zip" in os.listdir():
            os.remove("curl-impersonate.zip")
            
    def webScrape(self, url):
        """
        Input: url to web scrape
        Output: Return A BeautifulSoup Object 
        """
        
        while not "curl-impersonate" in os.listdir():
            self.start()
        
        files = os.listdir("curl-impersonate")
        chromes_files = [f for f in files if "chrome" in f and "android" not in f]
        file_exe = random.choice(chromes_files)
        
        result = os.system("curl-impersonate/" + file_exe +" "+ url + " > any-web-scraper.txt")
        
        while "any-web-scraper.txt" not in os.listdir():
            result = os.system("curl-impersonate/" + file_exe +" "+ url + " > any-web-scraper.txt")
        
        file = open('any-web-scraper.txt', 'r', encoding='utf-8', errors='ignore')
        response = file.read()
        file.close()
        
        while "any-web-scraper.txt" in os.listdir():
            os.remove("any-web-scraper.txt")
	
        self.stop()
        soup = BeautifulSoup(response, 'html.parser')
        return soup
