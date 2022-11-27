# A network scanning utility written in python.
# Create scans and save them to a database.
import pyfiglet
from modules.new_scan import *

title = pyfiglet.figlet_format("Oh Look , Another Port Scanner", font="doom")


def main():
    print(title)
    print('Welcome to the network scanner utility.')
    print('Please select an option from the menu below.')
    print('1. Create a new scan database.')
    print('2. Run a basic scan.')
    print('3. View saved scans.')
    print('4. Select a database.')

    selection = input('Enter your selection: ')
    if selection == '1':
        new_db()
        target()
        print('Database created.')
    if selection == '2':
        target()
        basic_scan()
    elif selection == '3':
        print_db()
    elif selection == '4':
        select_db()


def print_db():
    import sqlite3
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM hosts")
    print(cursor.fetchall())
    connection.commit()
    connection.close()


if __name__ == '__main__':
    main()
