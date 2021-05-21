import requests
from bs4 import BeautifulSoup
import csv

# Target website to scrape
website = requests.get('https://www.britannica.com/topic/list-of-philosophers-2027173')
soup = BeautifulSoup(website.text, 'html.parser')
links = soup.select('.topic-list .md-crosslink')

# Grab the first 25 links
for link in links[:25]:
  # Try to get the individual author link, name, description, summary, birth,death
  try:
    website = requests.get(link.attrs['href'])
    soup = BeautifulSoup(website.text, 'html.parser')
    name = soup.select_one('h1').text
    description = soup.select_one('.topic-identifier').text
    summary = soup.select_one('.topic-paragraph').text.strip() # Grab summary and strip blank spaces

    # Try to retrieve image if there is one
    try:
      image = soup.select_one('.fact-box-picture img').attrs['src']
    except AttributeError as error: # End of image try block
      image = None
          
    # Find birth and death and select and separate them from other information they come grouped with
    birth = soup.find(attrs={'data-label': 'born'}).find('dd').get_text(separator='|').split('|')[0]
    death = soup.find(attrs={'data-label': 'died'}).find('dd').get_text(separator='|').split('|')[0]
        
    # Try to find subjects of study list 
    try:
      subjects_of_study = soup.find(attrs={'data-label': 'subjects of study'}).select_one('ul')
      subjects_items = subjects_of_study.select('li')
      subjects = ''
      for item in subjects_items:
        subjects += item.text.strip() + ','
    except AttributeError as error: # End of subjects of study try block
      subjects = None # No subjects of study
        
    # Print scraped information
    print(f'{name}\n{description}\n{image}\n{summary}\n{birth}\n{death}\n{subjects}')

  except: # End of first try block
    print('Something went wrong!')