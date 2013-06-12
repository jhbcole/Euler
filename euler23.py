def main():
  l = []
  for i in xrange(1,28123):
    if(abundant(i)):
      l.append(i)
  l2 = []
  for i in xrange(len(l)):
    for j in xrange(i,len(l)):
      if(l[i] + l[j] < 28123):
        l2.append(l[i]+l[j])
  l3 = range(28123)
  l2 = list(set(l2))
  print len(l)
  print len(l2)
  print len(l3)
  for i in xrange(0,len(l2)):
    if(l2[i] in l3):
      l3.remove(l2[i]) 
  return sum(l3)

def abundant(n):
  if n < sum_divisors(n):
    return True
  else:
    return False

def sum_divisors(n):
  sum = 0
  for i in xrange(1,n):
    if(n%i == 0):
      sum += i
  return sum


print main()
