n = int(input())
a= [input().lower() for i in range(n)]
b = int(input())
c=[]
for j  in range(b):
    c += [i for i in input().lower().split()]
g=[]
for k in c:
    if k in a:
        continue
    else:
        if k not in g:
            g.append(k)
        else:
            continue
print(*g, sep='\n') 