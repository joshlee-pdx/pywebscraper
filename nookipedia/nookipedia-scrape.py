from displayAll import *
# import csv

query = 0

# User Menu
while query != '6':
  print('Welcome to Nookipedia!')
  print('1) Display brief information on all villagers')
  print('2) Display villagers starting with a certain letter')
  print('3) Display villagers of a certain species')
  print('4) Display villagers of a certain personality')
  print('5) Get detailed information on a specific villager')
  print('6) Quit')
  query = input('Please choose an option(1-6): ')

  # Display table info for all villagers
  if query == '1':
    displayAll()
  # Search through villagers with a certain string
  elif query == '2':
    searchVillagers()
  # Display villagers of a certain species
  elif query == '3':
    displaySpecies()
  # Display villagers with a certain personality
  elif query == '4':
    displayPersonality()
  # Find a villager by name
  elif query == '5':
    villagerInfo()
  # Close Program
  elif query == '6':
    print('\nClosing Program . . .')
  # User input invalid
  else:
    print('\nInvalid Option. . .')
    print('Please Try again.\n')
  
