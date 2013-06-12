#find the longest repeating decimal where the denom is < 1000
from decimal import * 

def repeating(n):
    s = str(n)[2:]
    cycle = [s[0]]
    i = 1
    while s[i] != s[0]:
        cycle.append(s[i])


def cycle(s):
  for i in xrange (2,2000):
    if(s[:i] == s[i:2*i]):
      #print i, s, s[:i], s[i:2*i], 
      return (True,i)
  return (False,0)


def main():
  max = (0,0)
  getcontext().prec = 4000
  for i in xrange(2,1000):
    s = str(Decimal('1') / Decimal(str(i)))[2:]
    while(s[0]=='0'):
      s = s[1:]
    c = cycle(s)
    if(c[0]):
      print i, c[1]
      if(c[1] > max[1]):
        max = (i,c[1])
  return max


print main()

#answer: 1/983 has a cycle of length 982
