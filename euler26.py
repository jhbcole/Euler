#find the longest repeating decimal where the denom is < 1000

def repeating(n):
    s = str(n)[2:]
    cycle = [s[0]]
    i = 1
    while s[i] != s[0]:
        cycle.append(s[i])
        
