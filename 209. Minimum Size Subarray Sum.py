class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        subSum = 0
        minimum = float('inf')   

        for right in range(len(nums)):
            subSum += nums[right]

            while subSum >= target:
                minimum = min(minimum, right - left + 1)
                subSum -= nums[left]
                left += 1

        return 0 if minimum == float('inf') else minimum
    