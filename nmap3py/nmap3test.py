

def top10test():
    import json
    from nmap3py.nmap3 import nmap3
    import sqlite3
    nmap = nmap3.Nmap()
    results = nmap.scan_top_ports("127.0.0.1")

    d = json.dumps(results['127.0.0.1']['ports'])
    l = json.loads(d)
    for _ports in l:
        #print(_ports)
        traffic = _ports
        a = traffic['protocol']
        b = traffic['portid']
        c = traffic['state']

        conn = sqlite3.connect('D:\\pyhon projects\\OLAPS_SCAN\\database\\test.db')
        cur = conn.cursor()
        cur.execute('create table if not exists top10 (protocol text, portid text, state text)')
        conn.commit()
        cur.execute('INSERT INTO top10 VALUES (?,?,?)', (a, b, c))
        conn.commit()
        conn.close()


if __name__ == '__main__':
    top10test()