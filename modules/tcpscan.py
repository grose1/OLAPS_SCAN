def tcpscan():
    import json
    from nmap3py.nmap3 import nmap3
    import sqlite3
    from datetime import datetime

    # datetime object containing current date and time
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    #print("date and time =", dt_string)
    host = input('Target Name:')
    ip = input('Target IP:')

    #Nmap TCP Scan
    nmap = nmap3.NmapScanTechniques()
    result = nmap.nmap_tcp_scan(ip)
    jd = json.dumps(result[ip]['ports'])
    l = json.loads(jd)
    for k in l:
        n = k
        a = n['protocol']
        b = n['portid']
        c = n['state']
        d = n['service']['name']
        #print(a)
        #print(b)
        #print(c)
        #print(d)

    #Save to database
    conn = sqlite3.connect('olaps.db')
    cur = conn.cursor()
    cur.execute('create table if not exists tcp_scan (host text, ip text, protocol text, port text, state text, service text, date text)')
    conn.commit()
    cur.execute('INSERT INTO tcp_scan VALUES (?,?,?,?,?,?,?)', (host, ip, a, b, c, d, dt_string))
    conn.commit()
    conn.close()


if __name__ == '__main__':
    tcpscan()