a = []
with open('D:\My\Python\dataset_3380_5.txt') as text:
    for s in text:
        a.append(s.strip().split('\t'))
d = {}
c = 0
b = 0
for i in range(1, 12):
    d[i] = '-'
for key in d.keys():
    for i in range(len(a)):
        if key == int(a[i][0]):
            c += int(a[i][2])
            b += 1
        else:
            continue
    if b != 0:
        d[key] = (c/b)
    else:
        continue
    c = 0
    b = 0
with open('D:\My\Python\dataset_3380_5.txt', 'w') as text:
    for key, value in d.items():
        text.write(str(key))
        text.write(' ')
        text.write(str(value))
        text.write('\n')
