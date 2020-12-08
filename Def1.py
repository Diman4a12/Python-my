

def closest_mod_5(x):
    y = x
    while y%5 != 0:        
        y +=1
    else:
        return y

a = closest_mod_5(6)
print (a)