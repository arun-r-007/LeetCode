# cook your dish here
t= int(input())

while t:
    s = input()
    t1 = input()
    
    res = ""
    
    for i,j in zip(s,t1):
        if i == j:
            res += 'G'
        else:
            res += 'B'
            
    print(res)
    t -= 1