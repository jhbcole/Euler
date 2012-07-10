import math

def sumDigits(n):
    s = str(n)
    s.split()
    s = [int(i) for i in s]
    return sum(s)

print sumDigits(math.factorial(100))
