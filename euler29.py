#powers and stuff. again super easy. answer 9183

def main():
  s = set([])
  for a in xrange(2,101):
    for b in xrange(2,101):
      s.add(a**b)
  print len(s)

main()
