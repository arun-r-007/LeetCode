# cook your dish here
s = input()
c = input()

n = len(s)

found = -1

for i in range(n):
    if s[i] == c:
        found = i
        break

print(found)

