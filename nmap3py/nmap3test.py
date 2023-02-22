

import nmap3
import json
nmap = nmap3.NmapScanTechniques()
result = nmap.nmap_ping_scan("127.0.0.1")
#print(result)
d = json.dumps(result['runtime']['summary'])
l = json.loads(d)
print(d)

        
        