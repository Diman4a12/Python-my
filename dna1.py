a = str(input())
b = len(a)
d = 0
c = 0
i = 0
for i in range(b):
    if i == b - 1:
        break
	elif a[i] == a[i + 1]:
		d = a[i:i+1]
		c = len(d)
	    continue
	print(a[i] + str(c), end='')
print(a[-1])


a = str(input())
b = len(a)
d = 0
c = 0
i = 0
for i in range(b):
    if a[i] == a[i + 1]:
		d = a[i:i+1]
		c = len(d)
	    continue
	elif i == b - 1:
        break
	else:
	    c = 1
	print(a[i] + str(c), end='')
print(a[-1])

a = str(input())
b = len(a)
c = 1
i = 0
for i in range(b):
    if a[i] == a[i + 1]:
        d = a[i]
        c = a.count(d)
        continue
    elif a[i] != a[i + 1]:
        d = a[i]
        c = a.count(d)
        print(a[i] + str(c), end='')
        
        

a = str(input())
b = len(a)
c = 1
i = 0
for i in range(b):
    if a[i] == a[i - 1]:
        d = a[i]
        c = a.count(d)
        continue
    elif a[i] != a[i - 1]:
        d = a[i]
        c = a.count(d)
        print(a[i] + str(c), end='')
        
a = str(input())
b = len(a)
c = 1
i = 0
j = 0
for i in range(b):
    if i == b - 1:
		break
		if a[i] == a[i - 1]:
        d = a[j:i + 1]
        c = d.count(a[i - 1])
        continue
    elif a[i] != a[i - 1]:
        d = a[j:i + 1]
        h = a[i - 1]
        c = d.count(h)
    print(str(c) + a[i], end='')
    j = i
	

a = str(input())
b = len(a)
j = 0
for i in range(b):
    if i == b - 1:
	    break
	    if a[i] == a[i - 1]:
            d = a[j:i + 1 ]
            h = a[i - 1]
            c = d.count(h)
        continue
        elif a[i] != a[i - 1]:
            d = a[j:i + 1]
            h = a[i - 1]
            c = d.count(h)
    print(str(c) + a[i], end='')
    j = i	
