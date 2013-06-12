import math

def is_prime(n):
  if n < 0:
    return False
  for i in xrange(2,int(math.sqrt(n))+1):
    if(n % i == 0):
      return False
  return True

def main():
  n = 0
  maxl = (0, 0, 0) #(max consec, a, b)
  for a in xrange(-1000,1000):
    for b in xrange(-1000, 1000):
      while is_prime(n**2 + a*n + b):
        n += 1
      if(n > maxl[0]):
        maxl = (n, a, b)
      n = 0
  return maxl

print main()
