def pingscan():
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

    #Nmap Ping Scan
    nmap = nmap3.NmapScanTechniques()
    result = nmap.nmap_ping_scan(ip)
    d = json.dumps(result['runtime']['summary'])

    #Save to database
    conn = sqlite3.connect('D:\\pyhon projects\\OLAPS_SCAN\\database\\olaps.db')
    cur = conn.cursor()
    cur.execute('create table if not exists ping_scan (host text, ip text, results text, date text)')
    conn.commit()
    cur.execute('INSERT INTO ping_scan VALUES (?,?,?,?)', (host, ip, d, dt_string))
    conn.commit()
    conn.close()


if __name__ == '__main__':
    pingscan()