# Description: This module will scan the top 10 ports of a target using nmap3. It will then save the results to a database.

def top10():
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

    nmap = nmap3.Nmap()
    results = nmap.scan_top_ports(ip)

    d = json.dumps(results[ip]['ports'])
    l = json.loads(d)
    for _ports in l:
        #print(_ports)
        traffic = _ports
        a = traffic['protocol']
        b = traffic['portid']
        c = traffic['state']


        conn = sqlite3.connect('olaps.db')
        cur = conn.cursor()
        cur.execute('create table if not exists top10 (host text, ip text, protocol text, portid text, state text, date text)')
        conn.commit()
        cur.execute('INSERT INTO top10 VALUES (?,?,?,?,?,?)', (host, ip, a, b, c, dt_string))
        conn.commit()
        conn.close()


if __name__ == '__main__':
    top10()