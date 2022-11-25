# A network scanning utility written in python.
# Create scans and save them to a database.
import pyfiglet
import modules.create_db
import modules.targets
title = pyfiglet.figlet_format("Oh Look , Another Port Scanner", font = "doom" )

# Create a database to store the scans in.
global db_name
db_input = input('Enter the name of the database: ')
db_name = db_input + '.db'
modules.create_db.create_db()


print(title)
print('Welcome to the network scanner utility.')
print('Please select an option from the menu below.')
print('1. Create a new scan.')
print('2. View saved scans.')
print('3. Exit.')

selection = input('Enter your selection: ')

if selection == '1':
    modules.targets.target()
elif selection == '2':
    modules.create_db.print_db()
elif selection == '3':
    exit()





