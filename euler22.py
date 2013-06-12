def wordscore(s):
  l = [ord(c)-ord('A')+1 for c in s]
  return sum(l)

def names():
  f = open("names.txt")
  f = f.read()
  s = f.split(",")
  print(len(s))
  l = [a[1:len(a)-1] for a in s]
  l.sort()
  print(l[0], wordscore(l[0]))
  l2 = [((i+1) * wordscore(l[i])) for i in xrange(len(l))]
  return sum(l2)


print names()
