def basic_scan():
    import nmap
    scanner = nmap.PortScanner()
    for i in range(beginning, ending + 1):
        res = scanner.scan(target_ip, str(i))
        res = res['scan'][target_ip]['tcp'][i]['state']
        print(f'port {i} is {res}.')