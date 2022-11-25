# Create target in database


def target():
    import sqlite3
    from main import db_name
    con_db = "modules/" + db_name
    target_ip = input('Enter the target ip address: ')
    beginning = int(input('Enter the targets beginning port: '))
    ending = int(input('Enter the targets ending port: '))
    scan_name = input('Enter the name of the scan: ')
    connection = sqlite3.connect(con_db)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO hosts (name, ip_address, port_start, port_end) VALUES (?,?,?,?)", (scan_name, target_ip, beginning, ending))
    connection.commit()
    connection.close()



if __name__ == '__main__':
    target()
