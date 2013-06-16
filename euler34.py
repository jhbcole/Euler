from math import *

def main():
  l = []
  for i in xrange(3,1000000):
    s = str(i)
    tot = 0
    for c in s:
      tot += factorial(int(c))
    if tot == i:
      print i
      l.append(i)
  return sum(l)

m = main()
print "SUM:", m
