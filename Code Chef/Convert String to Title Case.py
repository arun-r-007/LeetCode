# cook your dish here
t = int(input())

while t:
    t -= 1
    
    s = input()
    lst = s.split()
    
    capitalized_lst = [i if i.isupper() else i.capitalize() for i in lst]
    
    s = " ".join(capitalized_lst)
    
    print(s)