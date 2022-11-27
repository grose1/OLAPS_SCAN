def select_db():
    global db_selected
    import os
    for x in os.listdir():
        if x.endswith(".db"):
            # Prints only text file present in My Folder
            print('Select a database: ', x)
    selection = input('Enter your selection: ')
    db_selected = selection
    print('You selected: ', db_selected)
    db_menu()

def db_menu():
    #from targets import target
    #from reg_scan import basic_scan
    print('1. Run a basic scan.')
    print('2. View saved scans.')
    print('3. Select a database.')
    selection = input('Enter your selection: ')
    if selection == '2':
        print_db_select()


def print_db_select():
    import sqlite3
    connection = sqlite3.connect(db_selected)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM hosts")
    print(cursor.fetchall())
    connection.commit()
    connection.close()

if __name__ == '__main__':
    select_db()
    db_menu()
    print_db_select()

