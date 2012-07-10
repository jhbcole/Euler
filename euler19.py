

def count():
    months = [3,0,3,2,3,2,3,3,2,3,2,3]
    year = 1901
    day = 2 #0 = Sunday, 1 = Monday,..., 6 = Saturday
    c = 0
    i = 0
    while year < 2001:
        if i > len(months)-1:
            i = 0
            year += 1
            #print year       
        if day == 0:
            c+=1
            print i,day,year
        if year%400==0 and i ==1:
            day = (day + months[i] + 1)%7 #accounts for leap century
        elif year%100!=0 and year%4 == 0 and i == 1:
            day = (day + months[i] + 1)%7 #accounts for leap year
        else:
            day = (day + months[i])%7
        i+=1
    return c

print count()


