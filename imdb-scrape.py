import requests
from bs4 import BeautifulSoup
import csv

# Only retrieve english(US) version of site to be scraped
headers = {'Accept-Language': 'en-US'}
website = requests.get('https://www.imdb.com/chart/top', headers=headers)
soup = BeautifulSoup(website.text, 'html.parser')
links = soup.select('.lister-list .titleColumn a')

# Grab the top 10 movies info
for link in links[:10]:
  movie_link = link.attrs['href']
  website = requests.get(f'https://www.imdb.com{movie_link}', headers=headers)
  soup = BeautifulSoup(website.text, 'html.parser')

  title = soup.select_one('.title_wrapper > h1').contents[0].strip() # Separate title name from other header info
  runtime = soup.select_one('time').text.strip()
  plot = soup.select_one('.summary_text').text.strip()
  rating = soup.find(attrs={'itemprop': 'ratingValue'}).text
  rating_count = soup.find(attrs={'itemprop': 'ratingCount'}).text
  cast_list = soup.select('.cast_list tr')[1:5] # Get the first 5 of the cast
  cast = ''
  for item in cast_list:
	  cast += item.select('td')[1].text.strip() + ', '

  print(f'{title}\n{runtime}\n{plot}\n{rating}\n{rating_count}\n{cast}')