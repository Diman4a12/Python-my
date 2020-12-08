with open('D:\My\Python\dataset_3363_2.txt') as text:
    for s in text:
        s = s.strip()
a = [i for i in s]
b = '0123456789'
d = len(a)
c = ''
m = ''
num = ''
for i in range(d):
    if a[i] in b:
        num +=a[i]
        if a[i-d+1] not in b:
            m+=c*int(num)
            num=''
    else:
        c=a[i]
with open('D:\My\Python\dataset_3363_2.txt', 'w') as text:
	text.write(m)