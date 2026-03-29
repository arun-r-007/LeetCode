t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    t -= 1
    # Your code goes here
    
    # x = max(a)
    # while x in a:
    #     a.remove(x)
    # y = max(a)
    # print(x+y)
    
    
    largest = max(a)
    second_largest = max(number for number in a if number != largest)
    print(largest + second_largest)
























# t = int(input())

# while t > 0:
#     n = int(input())
#     a = list(map(int, input().split()))
#     t -= 1
#     # Your code goes here
    
#     x = max(a)
#     while x in a:
#         a.remove(x)
#     y = max(a)
#     print(x+y)
