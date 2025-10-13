class Solution(object):
    def isPossibleToSplit(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = {}
        for x in nums:
            seen[x] = seen.get(x, 0) + 1
            if seen[x] > 2:
                return False
        return True