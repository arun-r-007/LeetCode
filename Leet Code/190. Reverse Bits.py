class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        
        for _ in range(32):
            res = (res << 1) | (n & 1)
            n >>= 1
        
        return res
















# class Solution(object):
#     def reverseBits(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         str1 = bin(n)[2:]
#         str1 = str1.zfill(32)
#         str1 = str1[::-1]
#         return int(str1, 2)