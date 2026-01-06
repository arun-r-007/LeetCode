class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
         
        string = str(x)
        # string_rev = string[::-1]

        # if string == string_rev:
        #     return True
        # else:
        #     return False
        n = len(string)//2

        for i in range(0,n):
            if string[i] == string[-i-1]:
                continue
            else : return False
        
        return True








# class Solution(object):
#     def isPalindrome(self, x):
#         """
#         :type x: int
#         :rtype: bool
#         """
#         if x < 0:
#             return False
         
#         string = str(x)
#         string_rev = string[::-1]

#         if string == string_rev:
#             return True
#         else:
#             return False 
        