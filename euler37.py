#Truncatable Primes
#3797 is prime but remove digits left to right and you continuously
#get primes. 797, 97, and 7 are also all prime
#find the sum of the 11 truncatable primes.

#answer: 748317

import math as m


def is_prime(n):
  if m.fabs(n) < 2:
    return False
  if n == 2 or n == 3 or n == 5 or n == 7:
    return True
  for i in xrange(2,m.ceil(m.sqrt(n))+1):
    if n % i == 0:
      return False
  return True


def is_trunc_prime(n):
  slr = str(n)
  srl = str(n)
  while len(slr) >= 1:
    if is_prime(int(slr)) and is_prime(int(srl)):
      slr = slr[1:]
      srl = srl[:len(srl)-1]
    else:
      return False
  return True


def main():
  np = 0
  sum = 0
  i = 10
  while np < 11:
    if is_trunc_prime(i):
      np+=1
      sum+=i
      print "\t", i
    i+=1
  print sum


main()
