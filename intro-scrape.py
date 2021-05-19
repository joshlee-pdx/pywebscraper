import requests
from bs4 import BeautifulSoup

page = 1
next_button = True

while next_button:
  # Target site to scrape
  website = requests.get('https://quotes.toscrape.com/page/' + str(page))
  soup = BeautifulSoup(website.text, 'html.parser')
  next_button = soup.select_one('.next > a')

  #print(next_button)
  
  quotes = soup.select('.quote')
  for quote in quotes:
    text = quote.select_one('.text')
    author = quote.select_one('.author')
    tags = quote.select('.tag')
    print(text.text)
    print(author.text)
    for tag in tags:
      print(tag.text)
    print('====================================')
  print('Scraped Page: ' + str(page))
  page += 1

  # Find first title
  #title = soup.find('title')
  #print(title.text)

  # Find login link
  #login_link = soup.find(href='/login')
  #print(login_link.text)

  # Find all links
  #links = soup.find_all('a')
  #for link in links:
  #  print(link.text)

  # Find all quotes
  #quotes = soup.find_all(class_='text')
  #for quote in quotes:
  #  print(quote.text)

  # Find all quotes and display their author and text
  #quotes = soup.find_all(class_='quote')
  #for quote in quotes:
  #  quote_text = quote.find(class_='text')
  #  quote_author = quote.find(class_='author')

  #  print(quote_text.text)
  #  print(quote_author.text)

  #Alternate way to find all quotes text using CSS Selectors
  #quotes_text = soup.select('.text')
  #for quote_text in quotes_text:
  #  print(quote_text.text)

  #Find and display all quotes, their authors, and their tags
