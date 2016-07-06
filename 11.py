from PIL import Image

a = Image.open('cave.jpg')

w,h = a.size

odd = even = Image.new('RGB',(w/2,h/2))

c = a.load()

for x in range(w):
    for y in range(h):

        if (x+y) %2 == 0:
            even.putpixel((x/2,y/2),c[x,y])
        else:
            odd.putpixel((x/2,y/2),c[x,y])
        
odd.save('11-1.jpg','jpeg')
even.save('11-2.jpg','jpeg')

