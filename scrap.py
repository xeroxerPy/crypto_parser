import requests
from bs4 import BeautifulSoup

URL = 'https://coinmarketcap.com/'


def get_html(URL):
    result = requests.get(url=URL, params=None)
    if result.status_code != 200:
        pass
    else:
        return result.text


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    btc_price = soup.find('a', {'href': "/currencies/bitcoin/markets/", 'class': "cmc-link"})
    eth_price = soup.find('a', {'href': "/currencies/ethereum/markets/", 'class': "cmc-link"})
    xrp_price = soup.find('a', {'href': "/currencies/xrp/markets/", 'class': "cmc-link"})
    result = f'''BTC : {btc_price.text}
ETH : {eth_price.text}
XRP : {xrp_price.text}'''
    return result


def parse():
    return get_data(get_html(URL))
