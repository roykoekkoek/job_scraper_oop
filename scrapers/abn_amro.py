"""
Deze code implementeert de scraper voor ABN AMRO op basis van de base class van Scraper

"""

import requests
from base_scraper import Scraper

class ABNAMRO_Scraper(Scraper):
    def __init__(self):
        self.base_url = "https://werkenbijabnamro.nl"

    def print(self):
        print(self.base_url)


if __name__ == "__main__":
    response = requests.get("https://www.werkenbijabnamro.nl/api/vacancy/?sort=created&sortDir=DESC")
    
    with open("html.txt", "w") as f:
        f.write(response.text)