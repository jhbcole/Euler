#digit 5th powers

def main():
  l = []
  for i in xrange(10, 1000000):
    s = str(i)
    tot = 0
    for c in s:
      tot += int(c)**5
    if tot == i:
      print i
      l.append(i)
  return sum(l)

x = main()
print "SUM:", x
