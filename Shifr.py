key1, key2= input(), input()
shifr = {}
for i in range(len(key1)):
    for j in range(len(key2)):
        if i == j:
            shifr[key1[i]]=key2[j]
def code1(a):
    rez=''
    for i in range(len(a)):
        for key, value in shifr.items():
            if a[i]==key:
                rez+=(shifr[key])
    return(rez)
def code2(a):
    rez=''
    for i in range(len(a)):
        for key, value in shifr.items():
            if a[i]==value:
                rez+=key
    return(rez)
b=input()
c=input()
print(code1(b))
print(code2(c))