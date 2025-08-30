class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res, num = 0, abs(x)
        while num:
            res = res * 10 + num % 10
            num //= 10
        res = -res if x < 0 else res
        return res if -2**31 <= res <= 2**31 - 1 else 0
    