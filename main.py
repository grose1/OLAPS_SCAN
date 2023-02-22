# A network scanning utility written in python.
# Create scans and save them to a database.
import pyfiglet
from modules.nmap3top10 import *
from modules.pingscan import *
from modules.tcpscan import *
title = pyfiglet.figlet_format("Oh Look , Another Port Scanner", font="doom")



def main():
    print(title)
    print('A network scanning utility that saves results to a database.')
    print('Please select an option from the menu below.')
    print('1. Top 10 port scan.')
    print('2. Ping scan.')
    print('3. Print a database results.')
    print('4. TCP scan.')
    

    selection = input('Enter your selection: ')
    if selection == '1':
        top10()
    if selection == '2':
        pingscan()
    elif selection == '3':
        print_db()
    elif selection == '4':
        tcpscan()

        

def print_db():
    import sqlite3
    table = input('Enter the name of the table you want to print: ')
    connection = sqlite3.connect('database/olaps.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM " + table + " ")
    print(cursor.fetchall())
    connection.commit()
    connection.close()


if __name__ == '__main__':
    main()
