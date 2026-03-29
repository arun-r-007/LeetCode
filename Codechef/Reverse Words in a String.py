def reverseWords(s: str) -> str:
    # write your code here
    
    lst1 = s.split()
    
    str1 = ""
    
    while lst1:
        last_word = lst1.pop()
        str1 += last_word + " "
        
    return str1