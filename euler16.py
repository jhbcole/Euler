def sumDigits(n):
    d = []
    s = n
    for i in xrange(0,len(str(n))):
        d.append(s%10)
        s /= 10
    return sum(d)

print sumDigits(2**1000)
