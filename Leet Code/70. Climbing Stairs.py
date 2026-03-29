class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <= 45 and n >= 1:
            a, b = 1, 1
            for i in range(n-1):
                temp = a
                a = b
                b = temp + b
                print(a)
                print(b)
            return b

print(Solution().climbStairs(3))