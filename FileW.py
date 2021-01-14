a =[]
tet = []
with open ('file_write.txt') as red, open ('filewr.txt', 'a') as writ:
    for inf in red:
        inf = inf.strip()
        a.append(inf)
    print(a)
    for i in range(len(a)):
        tet.append(a[-1-i])
    print(tet)
    writ.write('\n'.join(tet))
