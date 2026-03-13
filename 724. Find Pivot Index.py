class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        left_sum = 0
        n = len(nums)

        for i in range(n):
            if left_sum == total - left_sum - nums[i]:
                return i
            left_sum += nums[i]

        return -1