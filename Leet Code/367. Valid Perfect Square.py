class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        ans = num ** 0.5
        return ans % 1 == 0
        # return ans * ans == num