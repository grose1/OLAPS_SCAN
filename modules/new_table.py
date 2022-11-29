from modules import new_scan


def basic_table():
    import sqlite3
    # Connects to the database named in new_scan.py
    connection = sqlite3.connect('database/' + new_scan.db_name)
    cursor = connection.cursor()
    # Creates a new table named adv_scan
    cursor.execute("CREATE TABLE basic_scan (name TEXT, ip_address TEXT, port_start INTEGER, port_end INTEGER, "
                   "ports_open TEXT)")
    connection.commit()
    connection.close()




# Creates a new table for the advanced scan results.
def advscan_table():
    import sqlite3
    # Connects to the database named in new_scan.py
    connection = sqlite3.connect('database/' + new_scan.db_name)
    cursor = connection.cursor()
    # Creates a new table named adv_scan
    cursor.execute("CREATE TABLE adv_scan (name TEXT, ip_address TEXT, port_start INTEGER, port_end INTEGER, "
                   "ports_open TEXT)")
    connection.commit()
    connection.close()
