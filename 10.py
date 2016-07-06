def f1(x,y):
    y = y -1
    
    if y == 0:
        return x
    else:
        x = f2(x)
        
        return f1(x,y)


def f2(x):
    
    a = list(str(x))
    
    b = []
    
    c = a[0]
    i = 0
    
    for n in a:
        d = n
        
        if d == c:
            i = i+1
        else:
            b.append(str(i))
            b.append(str(c))
            c = d
            i = 1
    
    b.append(str(i))
    b.append(str(c))
    return ''.join(b)
   
print [f1(1,x) for x in range(1,6)]

print len(f1(1,31))
