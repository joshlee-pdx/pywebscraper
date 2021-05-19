import requests
from bs4 import BeautifulSoup
import csv

# Target website to scrape
website = requests.get('https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population')
soup = BeautifulSoup(website.text,'html.parser')

# Target first wikitable for data
first_table = soup.select_one('.wikitable')

# Collect table data, skipping first row (table headings)
table_rows = first_table.select('tr')[1:-1]
csv_data = [['rank','name','population','percent','date','source']]

# Iterate through the rows of the table and store it in csv_data array
for row in table_rows:
  rank = row.find('th').text.strip()
  table_data = row.select('td')
  name = table_data[0].find('a').text
  population = table_data[1].text
  percent = table_data[2].text
  date = table_data[3].text
  source = table_data[4].text.split('[')[0].strip()
  #print(rank + ") " + name + " - Population: " + population + " (" + percent + " of world population) as of " + date + " - Source: " + source)
  csv_data.append([rank,name,population,percent,date,source]) 

# Write collected data to csv file
with open('countries_population.csv', 'w', newline='') as file:
   writer = csv.writer(file)
   writer.writerows(csv_data)