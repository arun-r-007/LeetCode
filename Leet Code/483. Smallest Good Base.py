import math
class Solution(object):
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        n = int(n)

        for m in range(int(math.log(n, 2)), 1, -1):
            k = int(n**m**-1)
            if (k**(m + 1) - 1) // (k - 1) == n:
                return str(k)

        return str(n - 1)