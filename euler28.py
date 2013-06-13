#ugh this one kinda sucks. but was super easy. answer 669171001

def main():
  sum = 0
  x = 1
  a = 2
  for j in xrange(0,1001/2):
    for i in xrange(0,4): 
      sum += x
      #print x
      x += a
    a+=2
  sum += x
  print sum


main()
