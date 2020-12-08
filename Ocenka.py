a = []
with open('C:\Python my\dataset_3363_4.txt') as text:
    for s in text:
        a.append(s.strip().lower().split(';'))
d = []
n = []
f = 0
k = 0
for i in range(len(a)):
    for j in range(1,4):
        f+=int(a[i][j])
    d.append(f/3)
    f = 0
c = i + 1
for i in range (1, 4):
    for j in range (c):
        k += int(a[j][i])
    n.append(k/c)
    k = 0
with open('C:\Python my\dataset_3363_4.txt', 'w') as text:
    for i in d:
        text.write(str(i) + '\n')
    for j in n:
        text.write(str(j) + ' ')
