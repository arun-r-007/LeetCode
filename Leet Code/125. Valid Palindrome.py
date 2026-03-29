class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        left = 0
        right = len(s) - 1
        
        while left < right:
            
            # Skip non-alphanumeric from left
            while left < right and not s[left].isalnum():
                left += 1
            
            # Skip non-alphanumeric from right
            while left < right and not s[right].isalnum():
                right -= 1
            
            # Compare characters
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True










        # s=s.lower()
        # temp=""
        # alpha="abcdefghijklmnopqrstuvwxyz1234567890"
        # for i in s:
        #     if(i in alpha):
        #         temp+=i
        # return (temp[::1]==temp[::-1])





        






        # result1 = ""

        # for ch in s:
        #     if ch.isalnum():
        #         result1 += ch.lower()
        
        # return result1 == result1[::-1]