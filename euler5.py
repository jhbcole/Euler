def checkDiv(n):
   for i in xrange(1,21):
       if(not(n%i==0)):
           return False
   return True

def search():
    for i in xrange(20,232792561):
        if(checkDiv(i)):
            return i

print search()
