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
    scanner = nmap.PortScanner()
    for i in range(beginning, ending + 1):
        res = scanner.scan(target_ip, str(i))
        res = res['scan'][target_ip]['tcp'][i]['state']
        print(f'port {i} is {res}.')
