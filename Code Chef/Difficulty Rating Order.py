t = int(input())

while t > 0:
    n = int(input())
    d = list(map(int, input().split()))
    # Your code goes here
    t -= 1
    
    is_sorted = True
    
    for i in range(n - 1):
        if d[i] > d[i + 1]:
            is_sorted = False
            break
    
    if is_sorted:
        print("YES")
    else:
        print("NO")
        