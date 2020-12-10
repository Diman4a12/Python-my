n = int(input())
a = [[i for i in input().split()] for j  in range(n)]
verc = 0
bok = 0
for i in range(n):
    if a[i][0] == 'север':
        verc+=int(a[i][1])
    elif a[i][0] == 'юг':
        verc-=int(a[i][1])
    elif a[i][0] == 'восток':
        bok+=int(a[i][1]) 
    elif a[i][0] == 'запад':
        bok-=int(a[i][1])
print(bok, verc)
