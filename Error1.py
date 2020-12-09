err = {}
for i in range(int(input())):
    b = input().split()
    err[b[0]] = b [2:]
lst = []

def err_f(a):
    for key in err.keys():
        if a == key:
            lst.extend(err[key])
            if err[key] == []:
                lst.append(key)
                break
            else:
                for i in err[key]:
                    err_f(i)
    return lst
a = []
for i in range(int(input())):
    b = (input())
    a.append(b)
    err1 = err_f(b)
    c1 = a.count(b)
    for j in a:
        if j in err1 and b not in err1 and c1 == 1:
            print (b)
            lst = []
            break
        else:
            lst = []
            