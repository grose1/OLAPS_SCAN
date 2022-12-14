# Create initial database for a new scan.
def new_db():
    import sqlite3
    global db_name
    db_input = input('Enter the name of the database: ')
    db_name = db_input + '.db'
    connection = sqlite3.connect('database/' + db_name)
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE hosts (name TEXT, ip_address TEXT, port_start INTEGER, port_end INTEGER)")
    connection.commit()
    connection.close()


# Defines the target IP address and port range for the scan.
def target():
    import sqlite3
    global target_ip
    global beginning
    global ending
    global scan_name
    con_db = 'database/' + db_name
    target_ip = input('Enter the target ip address: ')
    beginning = int(input('Enter the targets beginning port: '))
    ending = int(input('Enter the targets ending port: '))
    scan_name = input('Enter the name of the scan: ')
    connection = sqlite3.connect(con_db)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO hosts (name, ip_address, port_start, port_end) VALUES (?,?,?,?)",
                   (scan_name, target_ip, beginning, ending))
    connection.commit()
    connection.close()


# Menu for selecting the type of scan to run.
def new_scan_menu():
    from modules.scans import basic_scan
    from modules.scans import advanced_scan
    from modules.new_table import advscan_table
    from modules.new_table import basic_table
    print('1. Basic scan.')
    print('2. Advanced scan.')
    selection = input('Enter your selection: ')
    if selection == '1':
        basic_table()
        basic_scan()
    elif selection == '2':
        advscan_table()
        advanced_scan()
