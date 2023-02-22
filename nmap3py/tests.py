import nmap3
import json
nmap = nmap3.NmapScanTechniques()
result = nmap.nmap_tcp_scan("127.0.0.1")
#print(result['127.0.0.1']['ports'])
jd = json.dumps(result)
l = json.loads(jd)
for k in l:
        print(k)
        
        #a = k['127.0.0.1']['ports']['protocol']
        #print(a)
        #b = k['portid']
        #c = k['state']