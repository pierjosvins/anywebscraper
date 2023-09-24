if __name__ == "__main__":
    from anywebscraper import AnyWebScraper
    url = "https://www.investing.com/crypto/bitcoin/historical-data"
    any_web_scraper = AnyWebScraper()
    soup = any_web_scraper.webScrape(url=url)
    #linenos = soup.find_all("span", class_="linenos")
    #print(linenos)
    print(soup.prettify())
    #from urllib.request import urlopen
    #page = urlopen(url)
    #print(page)
    #html_bytes = page.read()
    #html = html_bytes.decode("utf-8")
    #print(html)

