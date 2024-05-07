import sys, json

data = json.load(sys.stdin)['data']

for c in data:
    if c['pdb-name']==sys.argv[1]:
        if c['lifecycle-state']=='TERMINATED':
            print (c['pdb-name']+":TERMINATED")
        elif c['lifecycle-state']=='PROVISIONING':
            print (c['pdb-name']+":PROVISIONING)
        else:
            print (c['pdb-name']+":"+c['id'])



