n = int(input())
ns = {'global': {'parent': 'None', 'arg':[]}}
def add(sp, val):
    ns[sp]['arg'].append(val)
    return
def create(sp, sp1):
    ns[sp]={'parent':sp1, 'arg':[]}
    return
def get(sp, val):
    for key in ns.keys():
        if sp == key:
            if val in ns[key]['arg']:
                print (key)
            elif val not in ns[key]['arg']:
                if ns[key]['parent'] == 'None':
					print ('None')
				else:
					get (ns[key]['parent'], val)
        else:
            continue
    return
for i in range(n):
    cmd, space, val = input().split()
    if cmd == 'add':
        add (space, val)
    elif cmd == 'create':
        create (space, val)
    elif cmd == 'get':
        get (space, val)

