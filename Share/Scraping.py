import requests
from bs4 import BeautifulSoup
'''

url = "https://uzmanpara.milliyet.com.tr/canli-borsa/bist-TUM-hisseleri/"
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0"
}

html = requests.get(url, headers=headers).content
soup = BeautifulSoup(html, 'html.parser')
table = soup.find('table', {'class' : 'table3'})
rows = table.find_all('tr', {'class' : 'zebra'})


for item in rows:
    hisse_adi = item.find('b').text
    hisse_yuzde = item.find('td', {'id' : 'h_td_yuzde_id_{}'.format(hisse_adi)}).text
    hisse_fiyat = item.find('td', {'id' : 'h_td_fiyat_id_{}'.format(hisse_adi)}).text
    print(hisse_adi, hisse_yuzde, hisse_fiyat)

'''

class Scraping:

    def __init__(self):
        self.url = "https://uzmanpara.milliyet.com.tr/canli-borsa/bist-TUM-hisseleri/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0"
        }

    def request(self):
        html_file = requests.get(self.url, headers=self.headers).content
        return html_file

    def getShares(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find_all('tr', {'class': 'zebra'})
        return table