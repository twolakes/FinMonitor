from datetime import datetime
from colorama import init, Fore, Back, Style


def print_time():
    curr_time = datetime.now()
    curr_time_str = curr_time.strftime("%m/%d/%Y %H:%M:%S")

    print(Style.RESET_ALL)
    print(f"------  {curr_time_str}  -----")
    print()