import math

def isPrime(n):
   for i in xrange(2, int(math.sqrt(n))+1):
       if(n%i==0):
           return False
   return True

def find():
   primes = [2,3,5,7]
   while(len(primes)<10001):
       p = len(primes)
       i = primes[p-1]+2
       while i in xrange(primes[p-1],10*primes[p-1]) and len(primes)==p:
           if(isPrime(i)):
               primes.append(i)
               #print "here", i
           i+=2
   return primes[len(primes)-1]

def ffind():
    f = open("primes.txt", "r+a+")
    primes = f.read()
    primes = primes.splitlines()
    #print primes
    while(len(primes)<1000001):
        p = len(primes)
        i = int(primes[p-1])+2
        while i in xrange(int(primes[p-1]),10*int(primes[p-1])) and len(primes)==p:
            if(isPrime(i)):
                primes.append(i)
                f.write("\n"+str(i))
                #print "here", i
            i+=2
    f.close()
    return primes[len(primes)-1]


print ffind()
