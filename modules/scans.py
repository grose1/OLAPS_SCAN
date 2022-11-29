from modules import new_scan



def basic_scan():
    import nmap
    scanner = nmap.PortScanner()
    for i in range(new_scan.beginning, new_scan.ending + 1):
        res = scanner.scan(new_scan.target_ip, str(i))
        res = res['scan'][new_scan.target_ip]['tcp'][i]['state']
        print(f'port {i} is {res}.')


def advanced_scan():
    import nmap
    import sqlite3
    scanner = nmap.PortScanner()
    print("Nmap Version: ", scanner.nmap_version())
    for i in range(new_scan.beginning, new_scan.ending + 1):
        scanner.scan(new_scan.target_ip, str(i), '-v -sS -sV -sC -A -O')

    scaninfo = scanner.scaninfo()
    ipstat = "Ip Status: ", scanner[new_scan.target_ip].state()
    protocol = scanner[new_scan.target_ip].all_protocols()
    "Open Ports: ", scanner[new_scan.target_ip]['tcp'].keys()
    a = ''.join(filter(str.isalnum, scaninfo))
    b = ''.join(filter(str.isalnum, ipstat))
    c = ''.join(filter(str.isalnum, protocol))
    print('Protocol Used: ', a)
    print('State: ', b)
    print('Protocol of Port: ', c)
    for key, value in scanner[new_scan.target_ip]['tcp'].items():
        j = key
        if value['state'] == 'open':
            print('Open Ports: ', j)
    con_db = 'database/' + new_scan.db_name
    connection = sqlite3.connect(con_db)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO adv_scan (name, ip_address, port_start, port_end, ports_open) VALUES (?,?,?,?,?)",
                   (new_scan.scan_name, new_scan.target_ip, new_scan.beginning, new_scan.ending, j ))
    connection.commit()
    connection.close()


    # sS for SYN scan, sv probe open ports to determine what service and version they are running on
    # O determine OS type, A tells Nmap to make an effort in identifying the target OS


