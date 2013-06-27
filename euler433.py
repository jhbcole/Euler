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


def euclid_steps(x,y,s):
  if y == 0:
    return s
  else:
    return euclid_steps(y, x % y, s+1)

def S(n):
  tot = 0
  for x in xrange(1,n+1):
    for y in xrange(1,n+1):
      tot += euclid_steps(x,y,0)
    print x
  return tot

def main():
  print S(5000000)
  
  

main()
