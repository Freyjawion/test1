import pickle

a = open("banner.p","rb")
b = pickle.load(a)
a.close

c = open("5.txt","w")

def d1(x,y):
	c.write(x*y) 
		
for i in b:
	s = list(i)
	for j in s:
		d1(j[0],j[1])
	c.write("\n")
	

c.close()