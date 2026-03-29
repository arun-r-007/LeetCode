t = int(input())

while t > 0:
    n = int(input())
    s = input()
    # Your code goes here
    t -= 1
    
    last_visit = s[0]
    
    A_count = 1 if s[0] == "A" else 0
    
    B_count = 0
    
    for i in range(1,n):
        if last_visit == s[i]:
            if s[i] == "A":
                A_count += 1
            else :
                B_count += 1
                
        last_visit = s[i]
        
    print(str(A_count) + " " + str(B_count))