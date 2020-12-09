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
	if ns1 == ns2:
		return 1
	elif ns2 in ns.keys() and ns1 in ns[ns2]:
		return 1
	elif ns2 in ns.keys():
		for i in ns[ns2]:
			py = get_ns(ns1, i)
			if py == 1:
			    return 1
	else:
		return 0
k = int(input())
for k in range (k):
    l, m = input().split()
    fun = get_ns(l, m)
    if fun == 1:
        print ('Yes')
    else:
        print ('No')
   