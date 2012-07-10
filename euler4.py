def palindrome(n):
   s = str(n)
   return s  == s[::-1]

def find():
    l=[]
    for i in xrange(999,111,-1):
        for j in xrange(999,111,-1):
            if(palindrome(i*j)):
                print i,j,i*j
                l.append(i*j)
    print max(l)

find()
