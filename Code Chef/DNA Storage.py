t = int(input())

while t > 0:
    n = int(input())
    s = input()
    # Your code goes here
    t -= 1
    
    dict1 ={
        '00' : 'A',
        '01' : 'T',
        '10' : 'C',
        '11' : 'G'
    }
    


    
    str1 = ''
    
    for i in range (0,n,2):
        s1 = str(s[i])+str(s[i+1])
        if s1 in dict1:
            str1 += dict1[s1]
    
    print(str1)