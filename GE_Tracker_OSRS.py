#Install packages required from windows command prompt
# python -m pip install requests
# python -m pip install colorama
import requests
import json
from colorama import Fore, Back, Style, init

init()

#sub in item IDs from https://www.osrsbox.com/tools/item-search/
items = ["139", "2353", "2", "5295", "561","6693","231","257","573","12627","7936"]
print("{:20} {:20} {:20} {:20}".format('Item Name','Item Price','Item Price Change','30 Day Change'))

for x in items:
    url = 'https://secure.runescape.com/m=itemdb_oldschool/api/catalogue/detail.json?item=' + x
    response = requests.get(url)
    data = json.loads(response.text)
    current_price = str(data['item']['current']['price'])
    current_price = current_price.replace(",","").replace(" ","")
    price_change = str(data['item']['today']['price'])
    price_change = price_change.replace(",","").replace(" ","")
    price_change = int(price_change)
    if int(price_change) > 0:
     print(Fore.GREEN + "{:<20} {:<20} {:<20} {:<20}".format(data['item']['name'],current_price,price_change,data['item']['day30']['change']))
    elif int(price_change) < 0:
     print(Fore.RED + "{:<20} {:<20} {:<20} {:<20}".format(data['item']['name'],current_price,price_change,data['item']['day30']['change']))
    else:
     print(Style.RESET_ALL + "{:<20} {:<20} {:<20} {:<20}".format(data['item']['name'],current_price,price_change,data['item']['day30']['change']))

print(Style.RESET_ALL + "\n\n")
input("Press Enter to continue...")