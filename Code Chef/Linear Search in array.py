# cook your dish here
a, b = map(int, input().split())

arr = list(map(int, input().split()))

flag = 0

for i in range(a):
    if arr[i] == b:
        flag = 1
        break
    
if flag:
    print("Yes")
else:
    print("No")