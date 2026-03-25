def isAnagram(s, t):
    # write your code here...
    
    if len(s) != len(t):
        return False

    count = [0] * 26  # For 'a' to 'z'

    for ch in s:
        count[ord(ch) - ord('a')] += 1

    for ch in t:
        count[ord(ch) - ord('a')] -= 1

    for c in count:
        if c != 0:
            return False

    return True









# def isAnagram(s, t):
#     # write your code here...
    
        
#     if sorted(s) == sorted(t):
#         return "YES"
        
#     return "NO"