# A network scanning utility written in python.
# Create scans and save them to a database.
import pyfiglet
from modules.new_scan import *
from modules.use_db import *
from modules.nmap3top10 import *

title = pyfiglet.figlet_format("Oh Look , Another Port Scanner", font="doom")



def main():
    print(title)
    print('A network scanning utility that saves results to a database.')
    print('Please select an option from the menu below.')
    print('1. Create a new scan database.')
    print('2. Use an existing database.')
    print('3. Print a database results.')
    print('4. Exit.')
    print('5. Top 10 port scan.')

    selection = input('Enter your selection: ')
    if selection == '1':
        new_db()
        target()
        new_scan_menu()
        print('Database created.')
    if selection == '2':
        select_db()
    elif selection == '3':
        print_db()
    elif selection == '4':
        exit()
    elif selection == '5':
        top10()



def print_db():
    import sqlite3
    connection = sqlite3.connect('database/' + new_scan.db_name)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM hosts")
    print(cursor.fetchall())
    connection.commit()
    connection.close()


if __name__ == '__main__':
    main()
