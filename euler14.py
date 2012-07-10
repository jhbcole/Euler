def sequence(n,l):
    if n==1: 
        return l
    elif n%2==0:
        l+=1
        return sequence(n/2,l)
    else:
        l+=1
        return sequence(1+3*n,l)


def find():
    s = []
    for i in xrange(899999,799999,-1):
        n = sequence(i,1)
        if n == 525:
            print i
        s.append(n)
    return max(s)

print find()
