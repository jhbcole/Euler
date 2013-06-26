#Double Base Palindromes
#The decimal number, 585 = 1001001001 is palidromic in both bases
#Find the sum of all numbers, less than 1M, which are palindromic in
#base 10 and base2

#answer: 872187 

def pb10(n):
  if(str(n) == str(n)[::-1]):
    return True
  return False


def pb2(n):
  bn = bin(n)[2:]
  if(bn == bn[::-1]):
    return True
  return False


def main():
  sum = 0
  for i in xrange(0,1000000):
    if(pb10(i) and pb2(i)):
      sum += i
  print sum

main()
