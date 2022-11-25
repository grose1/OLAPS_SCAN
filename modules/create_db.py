#create database


def create_db():
    import sqlite3
    from main import db_name
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE hosts (name TEXT, ip_address TEXT, port_start INTEGER, port_end INTEGER)")
    connection.commit()
    connection.close()


def print_db():
    import sqlite3
    connection = sqlite3.connect("modules/targets.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM hosts")
    print(cursor.fetchall())
    connection.commit()
    connection.close()

if __name__ == '__main__':
    create_db()
    #print_db()