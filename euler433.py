#Steps in Euclid's Algorithm
"""
Let E$(x_0, y_0)$ be the number of steps it takes to determine the greatest 
common divisor of $x_0$ and $y_0$ with \textbf{Euclid's Algorithm}. More
formally:\\
$$x_1 = y_0, y_1 = x_0 mod y_0$$
$$x_n = y_{n-1}, y_n = x_{n-1} mod y_{n-1}$$
E$(x_0, y_0) is the smallest $n$ such that $y_n = 0$.\\
We have E(1,1) = 1, E(10,6) = 3, and E(6,10) = 4.\\
Define S(N) as the sum of E$(x,y)$ for $1\leq x,y \leq \text{n}$.\\
We have S(1) = 1, S(10) = 221, and S(100) = 39826.\\

Find S$(5\cdot10^6)$.

"""
N = 5000000

def euclid_steps(x,y,s):
  if y == 0:
    return s
  else:
    return euclid_steps(y, x % y, s+1)

def eucstep(x,y):
  #if x%y == 0:
  #  return 1
  #if y % x == 0 or x == 1 or y+1==x:
  #  return 2
  #if x+1==y:
  #  return 3
  s = 0
  while(y != 0):
    tmp = x
    x = y
    y = tmp%y
    s+=1
  return s


def s(n):
  tot = 0
  for y in range(1,5000001):
    tot += euclid_steps(n,y,0)
  return tot


def S(n):
  tot = 0
  for x in xrange(1,n+1):
    for y in xrange(1,n+1):
      tot += euclid_steps(x,y,0)
    print x
  return tot

def main():
  print S(5000000)
  
def fastS(n):
  tot = 0
  for x in xrange(1,n+1):
    l = [0 for i in xrange(x+1,(2*x)+1)]
    for y in xrange(x+1,(2*x)+1):
      l[y%x] = eucstep(x,y)
    tot += sum(l)*(N/x) + sum(l[1:(N%x)+1]) - (2*x-1)
    #tot += t
    #print x,t
  return tot

N2 = 1000
s = fastS(N2)
print N2,s
      

#main()
