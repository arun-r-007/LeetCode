class Solution(object):
    def closestTarget(self, words, target, startIndex):
        """
        :type words: List[str]
        :type target: str
        :type startIndex: int
        :rtype: int
        """

        n = len(words)
        ans = float('inf')

        for i in range(n):
            if words[i] == target:
                dist = abs(i - startIndex)
                ans = min(ans, dist, n - dist)

        return ans if ans != float('inf') else -1