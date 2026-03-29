class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        c = int(a,2) + int(b,2)
        b = bin(c)
        return (str(b[2:]))
        

print(Solution().addBinary("11","1"))