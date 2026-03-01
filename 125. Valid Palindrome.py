class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        result1 = ""

        for ch in s:
            if ch.isalnum():
                result1 += ch.lower()
        
        return result1 == result1[::-1]