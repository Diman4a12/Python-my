n = int(input())
a = []
for j in range(n):
    a.append([i for i in input().split(';')])
tabl = {}
for i in range(n):
    for j in range(4):
        if j%2==0:
           tabl[a[i][j]] = 0
for key in tabl.keys():
    igr=0
    for i in range(n):
        for j in range(4):
            if key == a[i][j]:
                igr+=1
    tabl[key]=[igr]
for key in tabl.keys():
    win = 0
    for j in range(n):
        for i in range(4):
            if key == a[i][j] and i == 0:
                if a[i-3][j] > a[i-1][j]:
                    win+=1
            elif key == a[i][j] and i == 2:
                if a[i-1][j] > a[i-3][j]:
                    win+=1
    tabl[key].append(win)