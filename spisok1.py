a = []
with open ('C:\Users\Acer\Desktop\Python\Python my\dataset_3363_3.txt', 'r') as text:
	for s in text:
		a += s.strip().lower().split(' ')
d=len(a)
с = 0
m = {}
for i in a:
    c = a.count(i)
    m[i]=c
l = 0
for j in m.values():
    if j > l:
        l = j
f = {}
for t in m.keys():
    if m[t] == l:
        f[t]=l
r = ''
for p in f.keys():
    if p < r:
        r = p
with open ('C:\Users\Acer\Desktop\Python\Python my\dataset_3363_3.txt', 'w') as text:
	text.write(p)
	text.write(' ')
	text.write(str(l))