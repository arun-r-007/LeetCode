class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        result = ""
        n = columnNumber
    
        while n > 0:
            n -= 1
            remainder = n % 26
            result += chr(ord('A') + remainder)
            n //= 26
        
        return result[::-1]