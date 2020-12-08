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
    nch = 0
    lose = 0
    och = 0
    for i in range(n):
        for j in range(4):
            if key == a[i][j] and j == 0:
                if int(a[i][j-3]) > int(a[i][j-1]):
                    win+=1
                elif int(a[i][j-3]) == int(a[i][j-1]):
                    nch+=1
                elif int(a[i][j-3]) < int(a[i][j-1]):
                    lose+=1
            elif key == a[i][j] and j == 2:
                if int(a[i][j-1]) < int(a[i][j-3]):
                    win+=1
                elif int(a[i][j-1]) == int(a[i][j-3]):
                    nch+=1
                elif int(a[i][j-1]) > int(a[i][j-3]):
                    lose+=1
    och = nch*1+win*3
    tabl[key].append(win)
    tabl[key].append(nch)
    tabl[key].append(lose)
    tabl[key].append(och)
for key, value in tabl.items():
    print(key, end=':')
    for i in value:
        print(i, end=' ')
    print()