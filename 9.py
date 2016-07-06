from PIL import Image,ImageDraw

a = "".join(open('9-1.txt','r').read().splitlines()).split(',')
b = "".join(open('9-2.txt','r').read().splitlines()).split(',')

c1 = [a[x:x+4] for x in range(0,len(a)-4,2)]
c2 = [b[x:x+4] for x in range(0,len(b)-4,2)]


p = Image.new('RGBA',(640,480))

d = ImageDraw.Draw(p)

for x in c1:
    d.line(map(int,x),(128,128,128),3)

for x in c2:
    d.line(map(int,x),(255,255,255),3)


p.save('9.png','png')
