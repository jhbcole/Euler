import math

def isPrime(n):
    for i in xrange(2,int(math.sqrt(n))+1):
        if(n%i==0):
            return False
    return True

def find():
    f = open("primes.txt","r+a+")
    primes = f.read()
    primes = primes.splitlines()
    while(len(primes)<1000000):
        p = len(primes)
        i = int(primes[p-1])+2
        while len(primes)==p:
            if(isPrime(i)):
                primes.append(i)
                f.write("\n"+str(i))
            i+=2
    f.close()
    return primes[len(primes)-1]

print find()
