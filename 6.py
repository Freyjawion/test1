import zipfile

a = zipfile.ZipFile('channel.zip','r')
c = open("6.txt","w")

def f1(n):
    b = a.read(str(n) + '.txt','r')
    g = b.rsplit(' ', 1)[1]
    print b
    print g
    c.write(a.getinfo(str(n) + '.txt').comment)
    if is_number(g):
        f1(g)
    else:
        print "No More"
        
def is_number(s):
    try:
        complex(s) # for int, long, float and complex
    except ValueError:
        return False

    return True

def print_info(archive_name):
    zf = zipfile.ZipFile(archive_name)
    for info in zf.infolist():
		if info.comment <> '':
			print info.comment,

f1(90052)
c.close()
#print_info('channel.zip')