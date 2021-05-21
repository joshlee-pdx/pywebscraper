from re import finditer
import requests
from bs4 import BeautifulSoup

# Display all villagers with simple information
def displayAll():
  # Target website to scrape
  website = requests.get('https://nookipedia.com/wiki/Villagers/New_Horizons')
  soup = BeautifulSoup(website.text,'html.parser')

  # Target first wikitable for data
  first_table = soup.select_one('.sortable')

  # Collect table data
  table_rows = first_table.select('tr')[1:]

  print("Displaying all villagers: ")
  for row in table_rows:
    table_data = row.select('td')
    name = table_data[0].find('a').text
    species = table_data[1].text.strip()
    gender = table_data[2].text.strip()
    personality = table_data[3].text.strip()
    birthday = table_data[4].text.strip()
    catchphrase = table_data[5].text.strip()

    print(name + " " + species + " " + gender + " " + personality + " " + birthday + " " + catchphrase)

# Search for villagers based on user input and display matches
def searchVillagers():
  # Target website to scrape
  website = requests.get('https://nookipedia.com/wiki/Villagers/New_Horizons')
  soup = BeautifulSoup(website.text,'html.parser')

  # Target first wikitable for data
  first_table = soup.select_one('.sortable')

  # Collect table data
  table_rows = first_table.select('tr')[1:]

  find = input("Please enter a letter or letters of a villager you're searching for: ").lower()
  count = 0

  print("\nSearching for " + find + ". . .\n")

  for row in table_rows:
    table_data = row.select('td')
    name = table_data[0].find('a').text
    if find in name.lower(): 
      species = table_data[1].text.strip()
      gender = table_data[2].text.strip()
      personality = table_data[3].text.strip()
      birthday = table_data[4].text.strip()
      catchphrase = table_data[5].text.strip()

      print(name + " " + species + " " + gender + " " + personality + " " + birthday + " " + catchphrase)
      count += 1

  if count == 1:
    print("\n" + str(count) + " match found.\n")
  else:
    print("\n" + str(count) + " matches found.\n")

# Search for villagers based on species
def displaySpecies():
  # Target website to scrape
  website = requests.get('https://nookipedia.com/wiki/Villagers/New_Horizons')
  soup = BeautifulSoup(website.text,'html.parser')

  # Target first wikitable for data
  first_table = soup.select_one('.sortable')

  # Collect table data
  table_rows = first_table.select('tr')[1:]

  allSpecies = ['Alligator', 'Anteater', 'Bear', 'Bird', 'Bull', 'Cat', 'Chicken', 'Cow', 'Cub', 'Deer', 'Dog', 'Duck', 'Eagle', 'Elephant', 'Frog', 'Goat', 'Gorilla', 'Hamster', 'Hippo', 'Horse', 'Kangaroo', 'Koala', 'Lion', 'Monkey', 'Mouse', 'Octopus', 'Ostrich', 'Penguin', 'Pig', 'Rabbit', 'Rhino', 'Sheep', 'Squirrel', 'Tiger', 'Wolf']
  lowerSpecies = [item.lower() for item in allSpecies]
  print(allSpecies)
  find = input("Please enter the species you are looking for: ").lower()
  count = 0

  if find not in lowerSpecies:
    print("\n" + find + " not a valid species.")
    print("Returning to main menu. . .\n")
    #print(lowerSpecies)
    return

  print("\nSearching for " + find + ". . .\n")

  for row in table_rows:
    table_data = row.select('td')
    
    species = table_data[1].text.strip()
    if find == species.lower():
      name = table_data[0].find('a').text 
      gender = table_data[2].text.strip()
      personality = table_data[3].text.strip()
      birthday = table_data[4].text.strip()
      catchphrase = table_data[5].text.strip()

      print(name + " " + species + " " + gender + " " + personality + " " + birthday + " " + catchphrase)
      count += 1

  if count == 1:
    print("\n" + str(count) + " " + find + " found.\n")
  else:
    print("\n" + str(count) + " " + find + "s found.\n")

# Find villagers based on personalities
def displayPersonality():
  # Target website to scrape
  website = requests.get('https://nookipedia.com/wiki/Villagers/New_Horizons')
  soup = BeautifulSoup(website.text,'html.parser')

  # Target first wikitable for data
  first_table = soup.select_one('.sortable')

  # Collect table data
  table_rows = first_table.select('tr')[1:]

  find = input("Please enter the personality type you are looking for: ").lower()
  count = 0

  print("\nSearching for " + find + ". . .\n")

  for row in table_rows:
    table_data = row.select('td')
    
    personality = table_data[3].text.strip()
    if find in personality.lower():
      name = table_data[0].find('a').text 
      species = table_data[1].text.strip()
      gender = table_data[2].text.strip()
      birthday = table_data[4].text.strip()
      catchphrase = table_data[5].text.strip()

      print(name + " " + species + " " + gender + " " + personality + " " + birthday + " " + catchphrase)
      count += 1

  if count == 1:
    print("\n" + str(count) + " " + find + " found.\n")
  else:
    print("\n" + str(count) + " " + find + "s found.\n")

def villagerInfo():
  find = input("Please enter the villager you want info on: ").lower()
  print("\nSearching for " + find + ". . .\n")

  try:
    # Target website to scrape
    website = requests.get('https://nookipedia.com/wiki/'+find)
    soup = BeautifulSoup(website.text,'html.parser')

    first_table = soup.select_one('.infobox')
    table_rows = first_table.select('tr')
    
    name = table_rows[0].find('th').text.strip()
    table_data = table_rows[5].find_all('a')
    species = table_data[0].text
    personality = table_data[1].text
    gender = table_data[2].text
    birthday = table_rows[6].find('td').text.strip()
    saying = table_rows[7].find('td').text.strip()
    catchphrase = table_rows[8].find('td').text.strip()
    clothing = table_rows[9].find('td').text.strip()
    clothes = clothing.replace("[nb 1]"," ").replace("[nb 2]"," ").replace("[nb 3]"," ").replace("[nb 5]"," ").replace("[nb 4]"," ")
    summary = soup.find_all('p')
    
    print("Name: " + name)
    print("Species: " + species)
    print("Personality: " + personality)
    print("Gender: " + gender)
    print("Birthday: " + birthday)
    print("Saying: " + saying)
    print("Catchphrase: " + catchphrase)
    print("Clothing: " + clothes)
    print("Description: ")
    print(summary[1].text + summary[2].text)
  except:
    print("Something went wrong!\n")
