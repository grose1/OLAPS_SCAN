from modules import new_scan


# A basic port scan that only returns open ports and saves them to a database.
def basic_scan():
    import nmap
    import sqlite3
    scanner = nmap.PortScanner()
    print("Nmap Version: ", scanner.nmap_version())
    for i in range(new_scan.beginning, new_scan.ending + 1):
        res = scanner.scan(new_scan.target_ip, str(i))
        res = res['scan'][new_scan.target_ip]['tcp'][i]['state']
        #print(f'port {i} is {res}.')
        for key, value in scanner[new_scan.target_ip]['tcp'].items():
            j = key
            if value['state'] == 'open':
                print('Open Ports: ', j)
                con_db = 'database/' + new_scan.db_name
                connection = sqlite3.connect(con_db)
                cursor = connection.cursor()
                cursor.execute(
                    "INSERT INTO basic_scan (name, ip_address, port_start, port_end, ports_open) VALUES (?,?,?,?,?)",
                    (new_scan.scan_name, new_scan.target_ip, new_scan.beginning, new_scan.ending, j))
                connection.commit()
                connection.close()



# Advanced port scan that returns open ports and saves them to a database.
def advanced_scan():
    import nmap
    import sqlite3
    scanner = nmap.PortScanner()
    print("Nmap Version: ", scanner.nmap_version())
    for i in range(new_scan.beginning, new_scan.ending + 1):
        scanner.scan(new_scan.target_ip, str(i), '-v -sS -sV -sC -A -O')
        for key, value in scanner[new_scan.target_ip]['tcp'].items():
            j = key
            if value['state'] == 'open':
                print('Open Ports: ', j)
                con_db = 'database/' + new_scan.db_name
                connection = sqlite3.connect(con_db)
                cursor = connection.cursor()
                cursor.execute(
                    "INSERT INTO adv_scan (name, ip_address, port_start, port_end, ports_open) VALUES (?,?,?,?,?)",
                    (new_scan.scan_name, new_scan.target_ip, new_scan.beginning, new_scan.ending, j))
                connection.commit()
                connection.close()
    # sS for SYN scan, sv probe open ports to determine what service and version they are running on
    # O determine OS type, A tells Nmap to make an effort in identifying the target OS
