import csv
import requests
from bs4 import BeautifulSoup
from decimal import Decimal

# Prompt user for search options
query = input('Enter product: ')
free_shipping = input('Require free shipping?(y/n): ')
max_price = Decimal(input('Enter maximum price: '))

# Scrape the first 5 pages of target site 
for i in range(1,5):
  website = requests.get('https://www.ebay.com/sch/i.html?_nkw=' + query + '&_pgn=' + str(i)).text
  soup = BeautifulSoup(website, 'html.parser')
  items = soup.select('.srp-results .s-item')

  for item in items:
    title = item.h3.text
    price = item.select_one('.s-item__price').text
    shipping = item.select_one('.s-item__shipping').text

    #
    price_decimal = Decimal(price.split(' to ')[0][1:])
    if price_decimal > max_price:
      continue

    # Only display results that have free shipping if required
    if free_shipping == 'y':
      if 'Free' in shipping:
        print(f'{title}\n{price}\n{shipping}')
    # Display all results
    else:
      print(f'{title}\n{price}\n{shipping}')

    print('==================')