t = int(input())

while t:
    t -= 1
    
    num = input().strip()
    
    num = list(num)
    i = len(num) - 1
    
    while i >= 0:
        if num[i] == '9':
            num[i] = '0'
            i -= 1
        else:
            num[i] = str(int(num[i]) + 1)
            break
    else:
        num.insert(0, '1')   # all digits were 9
    
    print("".join(num))
















# # cook your dish here
# t = int(input())

# while t:
#     t -= 1
    
#     n = int(input())
    
#     print(n+1)