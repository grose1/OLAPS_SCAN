# A network scanning utility written in python.
# Create scans and save them to a database.
import pyfiglet
from modules.use_db import select_db
title = pyfiglet.figlet_format("Oh Look , Another Port Scanner", font = "doom" )

# Create a database to store the scans in.

def new_db():
    import sqlite3
    global db_name
    db_input = input('Enter the name of the database: ')
    db_name = db_input + '.db'
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE hosts (name TEXT, ip_address TEXT, port_start INTEGER, port_end INTEGER)")
    connection.commit()
    connection.close()
    main()

def target():
    import sqlite3
    global target_ip
    global beginning
    global ending
    con_db = db_name
    target_ip = input('Enter the target ip address: ')
    beginning = int(input('Enter the targets beginning port: '))
    ending = int(input('Enter the targets ending port: '))
    scan_name = input('Enter the name of the scan: ')
    connection = sqlite3.connect(con_db)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO hosts (name, ip_address, port_start, port_end) VALUES (?,?,?,?)", (scan_name, target_ip, beginning, ending))
    connection.commit()
    connection.close()

def basic_scan():
    import nmap
    scanner = nmap.PortScanner()
    for i in range(beginning, ending + 1):
        res = scanner.scan(target_ip, str(i))
        res = res['scan'][target_ip]['tcp'][i]['state']
        print(f'port {i} is {res}.')
def print_db():
    import sqlite3
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM hosts")
    print(cursor.fetchall())
    connection.commit()
    connection.close()

def main():
    print(title)
    print('Welcome to the network scanner utility.')
    print('Please select an option from the menu below.')
    print('1. Create a new database.')
    print('2. Run a basic scan.')
    print('3. View saved scans.')
    print('4. Select a database.')



    selection = input('Enter your selection: ')
    if selection == '1':
        new_db()
        print('Database created.')
    if selection == '2':
        target()
        basic_scan()
    elif selection == '3':
        print_db()
    elif selection == '4':
        select_db()



if __name__ == '__main__':
    main()


