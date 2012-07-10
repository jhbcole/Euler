def prime(n):
   if n%2 == 0:
       count = 0
       while(n%2==0):
           n/=2
           count += 1
       yield 2, count, len(str(n))
   f = 3
   while(f < n):
       if n%f==0:
           count = 0
           while(n%f == 0):
               n/=f
               count+=1
           yield f,count,len(str(n))
       f+=2
   if n>1: yield n,1,len(str(n))
   

for i in prime(600851475143):
    print i
