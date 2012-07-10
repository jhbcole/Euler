import math

def sremove(n,l):
    if n in l:
        l.remove(n)
    return l

def divisors(n):
    d = [1]
    if n > 1:
        for i in xrange(2, int(math.sqrt(n))+1):
            if n%i==0 and i not in d:
                d.append(i)
                d.append(n/i)
        d = sremove(n,d)
    d.sort()
    #print n,d
    return d

def d(n):
    d = divisors(n)
    return sum(d)


def a():
    s = []
    l = [i for i in xrange(1, 10000)]
    for i in l:
        d1 = d(i)
        d2 = d(d1)
        if i == d2 and i!=d1:
            print i,d1
            s.append(i)
            s.append(d1)
            l = sremove(d1,l)
            l = sremove(i,l)
    print s
    return sum(s)

print a()
