import sys, json

data = json.load(sys.stdin)['data']

for c in data:
        if c['lifecycle-state']=='TERMINATED':
            print (" db: "+c['pdb-name']+":TERMINATED")
        elif c['lifecycle-state']=='PROVISIONING':
            print (" db: "+c['pdb-name']+":PROVISIONING")
        else:
            print (" db: "+c['pdb-name']+":"+c['open-mode']+":"+c['connection-strings']['pdb-default'].split("/",1)[1])
            print (" id: "+c['id'])
            print ("")



