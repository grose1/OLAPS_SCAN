import nmap

scanner = nmap.PortScanner()

ip_addr = '127.0.0.1'
print("Nmap Version: ", scanner.nmap_version())
# sS for SYN scan, sv probe open ports to determine what service and version they are running on
# O determine OS type, A tells Nmap to make an effort in identifying the target OS
scanner.scan(ip_addr, '78-82', '-v -sS -sV -sC -A -O')
print(scanner.scaninfo())
print("Ip Status: ", scanner[ip_addr].state())
print(scanner[ip_addr].all_protocols())
os = scanner[ip_addr]['osmatch'][0]['name']
accuracy = scanner[ip_addr]['osmatch'][0]['accuracy']
host = scanner[ip_addr]['hostnames'][0]['name']
print("OS: ", os)
print("Accuracy: ", accuracy)
print("Host: ", host)
print("Open Ports: ", scanner[ip_addr].keys())
for key, value in scanner[ip_addr]['tcp'].items():

    j = key
    if value['state'] == 'open':
        print('Open Ports: ', j)