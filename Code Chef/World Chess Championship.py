t = int(input())

while t :
    t -= 1
    
    x = int(input())
    s = input()
    
    c = 0       # denotes a victory by Carlsen.
    n = 0       # denotes a victory by Chef.
    
    k = len(s)
    
    s = s.lower()
    
    for i in range(k):
        if s[i] == 'c':
            c += 2
        elif s[i] == 'n':
            n += 2
        else:
            c += 1
            n += 1
            
    if c > n:
        print(60 * x)
    elif c == n:
        print(55 * x)
    else:
        print(40 * x)