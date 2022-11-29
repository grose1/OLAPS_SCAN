from modules import new_scan


def advscan_table():
    import sqlite3
    connection = sqlite3.connect('database/' + new_scan.db_name)
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE adv_scan (name TEXT, ip_address TEXT, port_start INTEGER, port_end INTEGER, "
                   "ports_open TEXT)")

    connection.commit()
    connection.close()
