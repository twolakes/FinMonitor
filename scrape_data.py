from bs4 import BeautifulSoup
from urllib.request import urlopen

from colorama import init, Fore, Back, Style

from utils import print_time


base_mw_url = "https://www.marketwatch.com"
base_ft_url = "https://www.ft.com"


# ******** STOCKS
def process_sec(stock_list):
    
    output_table = []

    for sec in stock_list:

        # use Beautiful Soup to fetch page
        url = base_mw_url + "/investing/stock/" + sec[1]
        page = urlopen(url)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")

        # locate quote block
        quote_block = soup.find('div', {"class": "intraday__data"})

        # parse quote
        sec_name = "{0:<14}".format(sec[0])
        quote = "{0:>12}".format(quote_block.find('bg-quote', {"class": "value"}).string)
        change = "{0:>10}".format(quote_block.find('bg-quote', {"field": "change"}).string)
        chg_str = "{0:>10}".format(change)
        pct_change = "{0:>11}".format(quote_block.find('bg-quote', {"field": "percentchange"}).string)
        output_table.append((float(change) / abs(float(change)), f"{sec_name}{quote}{chg_str}{pct_change}"))

    # output
    print_time()
    for item in output_table:
        if item[0] > 0:
            print(Fore.GREEN + item[1])
        elif item[0] < 0:
            print(Fore.RED + item[1])
        else:
            print(Style.RESET_ALL + item[1])

    print()


# ******** NEWS
def process_news():

    # fetch page
    url = base_ft_url + "/markets"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")

    # naviagate to list
    article_list = soup.find("div", {"data-trackable": "top-stories-column-one"})
    articles = article_list.find_all("a", {"data-trackable": "heading-link"})

    # output
    print_time()
    for article in articles:
        print(Fore.YELLOW + "> " + article.text)
    
    print()


# ******** INDECES
def process_index():

    output_table = []

    # fetch page
    url = base_mw_url
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")

    # find index table
    index_block = soup.find('tbody', {"class": "markets__group"})
    index_list = index_block.find_all("tr")

    # parse indeces
    for index in index_list:
        index_name = "{0:<12}".format(index.find('a').string)
        price = "{0:>12}".format(index.find('td', {'class': 'price'}).find('bg-quote').string)
        change = index.find('td', {'class': 'change'}).find('bg-quote').string
        chg_str = "{0:>10}".format(change)
        pct_chg = "{0:>11}".format(index.find('td', {'class': 'percent'}).find('bg-quote').string)
        output_table.append((float(change) / abs(float(change)), f"{index_name}{price}{chg_str}{pct_chg}"))

    # output
    print_time()
    for item in output_table:
        if item[0] > 0:
            print(Fore.GREEN + item[1])
        elif item[0] < 0:
            print(Fore.RED + item[1])
        else:
            print(Style.RESET_ALL + item[1])

    print()


# ******** CRYPTO
def process_crypto(crypto_list):
    
    output_table = []

    for crypto in crypto_list:

        #fetch page
        url = base_mw_url + "/investing/cryptocurrency/" + crypto[1]
        page = urlopen(url)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")

        # locate quote block
        quote_block = soup.find('div', {"class": "intraday__data"})

        # parse
        cry_name = "{0:<14}".format(crypto[0])
        quote = "{0:>12}".format(quote_block.find('bg-quote', {"class": "value"}).string)
        chg_str = "{0:>10}".format(quote_block.find('bg-quote', {"field": "change"}).string)
        change = float(chg_str.strip().replace(',', ''))
        pct_change = "{0:>11}".format(quote_block.find('bg-quote', {"field": "percentchange"}).string)
        output_table.append((float(change) / abs(float(change)), f"{cry_name}{quote}{chg_str}{pct_change}"))

    # outpu
    print_time()
    for item in output_table:
        if item[0] > 0:
            print(Fore.GREEN + item[1])
        elif item[0] < 0:
            print(Fore.RED + item[1])
        else:
            print(Style.RESET_ALL + item[1])

    print()