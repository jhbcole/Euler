def pythag(a,b,c):
    if(not (a<b and b<c)):
        return False
    else:
        if((a**2 + b**2) == c**2):
            return True
    return False

def add(a,b,c):
    return (a+b+c)==1000

def find():
    for a in xrange(1,998):
        for b in xrange(a,999):
            for c in xrange(b,1000):
                if(pythag(a,b,c) and add(a,b,c)):
                    return [a,b,c]
    else: return "Uh-oh!"

print find()
