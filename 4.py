import urllib

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

def f1(n):
    x = urllib.FancyURLopener({})
    f = x.open(url + str(n))
    g = f.read()
    gn = g[-5:]
    print g
    print gn
    if is_number(gn):
        f1(gn)
    else:
        print "No More"
        

def is_number(s):
    try:
        complex(s) # for int, long, float and complex
    except ValueError:
        return False

    return True

f1(631)