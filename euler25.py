#Fibonacci Sequence

def genFibs(n):
    f = open("fib.txt", "r+a+")
    fibs = f.read()
    fibs = fibs.splitlines()
    while len(fibs) < n:
        f1 = fibs[len(fibs)-1]
        f2 = fibs[len(fibs)-2]
        fibs.append(int(f1)+int(f2))
        f.write("\n" + str(int(f1)+int(f2)))
    f.close()
    return fibs[len(fibs)-1]

def findLenFib(n):
    f = open("fib.txt")
    fibs = f.read()
    fibs = fibs.splitlines()
    i = 0
    while len(fibs[i]) < n-1:
        i+=1
    return i+1

genFibs(10000)
print findLenFib(1000)
