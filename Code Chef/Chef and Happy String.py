t = int(input())

while t > 0:
    s = input()
    # Your code goes here
    t -= 1
    
    vol = "aeiou"
    
    n = len(s)
    l = 0
    
    for i in range(n):
        if l > 2:
            print("Happy")
            break
            
        if s[i] in vol:
            l += 1
        else:
            l = 0
            
    if l <= 2:
        print("Sad")