import os
from dotenv import load_dotenv
import time
from datetime import datetime

from scrape_data import process_sec, process_news, process_index, process_crypto

from colorama import init, Fore, Back, Style



# initialize
# list tuples:  1 - Desc, whatever you wish
#               2 - Symbol, the std symbol for the security or coin

stocks = [
    ("GameStop", "gme"),
    ("AMC", "amc"),
    ("Tesla", "tsla"),
    ("DraftKings", "dkng")]

cryptos = [
    ("Bitcoin", "btcusd"),
    ("Ethereum", "ethusd"),
    ("Litecoin", "ltcusd"),
    ("ZCash", "zecusd"),
    ("Monero", "xmrusd")]

init(autoreset=False)           # for colorama
os.system('cls')
interval = 900                  # in seconds


while True:
    # get stock quotes
    process_sec(stocks)
    time.sleep(interval)

    # get news
    process_news()
    time.sleep(interval)

    # get indeces
    process_index()
    time.sleep(interval)

    # get crypto quotes
    process_crypto(cryptos)
    time.sleep(interval)




