class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = list(set(nums))

        d.sort(reverse = True)

        if len(d) >= 3:
            return d[2]

        return d[0]