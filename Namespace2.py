n = int(input())
a = []
ns = {}
for i in range (n):
    b = input()
    if ':' not in b:
        ns[b] = []
    else:
        c, g = b.split(' :', 1)
        a += g.split()
        if c not in ns.keys():
            ns[c] = a
            a = []
        else:
            ns[c].extend(a)
            a = []
def get_ns (ns1, ns2):
    count = 0
    for key, item in ns.items():
        if key == ns2 and ns1 in item:
            print ('Yes')
        elif key == ns2:
            for i in item:
                get_ns(i, key)
            else:
                print ('No')
k = int(input())
for k in range (k):
    l, m = input().split()
    get_ns(l, m)
    


n = int(input())
a = []
ns = {}
for i in range (n):
    b = input()
    if ':' not in b:
        ns[b] = []
    else:
        c, g = b.split(' :', 1)
        a += g.split()
        if c not in ns.keys():
            ns[c] = a
            a = []
        else:
            ns[c].extend(a)
            a = []
def get_ns (ns1, ns2):
    if ns2 in ns.keys() and ns1 in ns[ns2]:
        print ('Yes')
        return
    elif ns1 == ns2:
        print ('Yes')
    elif ns2 in ns.keys():
        if ns[ns2] == []:
            print ('No')
        else:
            for i in ns[ns2]:
                if i in ns.keys() and ns1 in ns[i]:
                    print ('Yes')
                    break
                    return
                else:
                    print ('No')
    else:
        print ('No')
    return
k = int(input())
for k in range (k):
    l, m = input().split()
    get_ns(l, m)
{'C ': ['A'], 'D ': ['B', 'C'], 'A': [], 'B ': ['A']}