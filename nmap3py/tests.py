import nmap3
import json
nmap = nmap3.NmapScanTechniques()
result = nmap.nmap_tcp_scan("127.0.0.1")
#print(result['127.0.0.1']['ports'])
jd = json.dumps(result['127.0.0.1']['ports'])
l = json.loads(jd)
for k in l:
        #print(k)
        
        a = k['protocol']
        b = k['portid']
        c = k['state']
        d = k['service']['name']
        print(a)
        print(b)
        print(c)
        print(d)

