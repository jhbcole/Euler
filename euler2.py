def fib():
   f = [0,1]
   i = 1
   while(f[len(f)-1] <4000000):
       f.append(f[i]+f[i-1])
       i+=1
   return f

def sum():
   f = fib()
   sum = 0
   for i in xrange(0,len(f)):
       if(f[i]%2==0):
           sum+=f[i]
   return sum

print sum()
