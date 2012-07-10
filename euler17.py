def numbers(n):
    if n < 20:
        return ['one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen'][n-1]
    if n<100:
        s = n
        s /= 10
        l = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
        if n%10 != 0:
            return l[s-2] +" "+ numbers(n%10)
        else:
            return l[s-2]
    if n<1000:
        s = n
        s /= 100
        if n%100 != 0:
            return numbers(s) + " hundred and " + numbers(n%100)
        else:
            return numbers(s) + " hundred"
    if n == 1000:
        return "one thousand"

def count():
    s = ""
    for i in xrange(1, 1001):
        s += numbers(i)
    s=s. split(" ")
    l = 0
    for i in s:
        l += len(i)
    return l

print count()
