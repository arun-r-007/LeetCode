class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        max_sum = float("-inf")
        for i in nums:
            if sum < 0 :sum = 0
            sum+=i
            max_sum = max(max_sum,sum)

        return max_sum






# class Solution(object):
#     def maxSubArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         max_sum = curr_sum = nums[0]
#         n = len(nums)
#         for i in range(1, n):
#             curr_sum = max(nums[i], curr_sum + nums[i])
#             max_sum = max(max_sum, curr_sum)

#         return max_sum