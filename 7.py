from PIL import Image

a = Image.open('oxygen.png')

w,h = a.size

c = [a.getpixel((x,h // 2)) for x in range(0,w,7)]

def gray(i):
    if i[0]==i[1]==i[2]:
        return True
    else:
        return False

d = filter(gray,c)

e = map(lambda i:i[0],d)
        
f = "".join(map(chr,e))

g = f[-44:-1]

print "".join(map(chr,map(int,g.split(','))))



