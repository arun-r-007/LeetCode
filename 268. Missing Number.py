






# class Solution(object):
#     def missingNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         n = len(nums)
#         expected = n * (n + 1) // 2
#         actual = sum(nums)
#         return expected - actual
    


# class Solution(object):
#     def missingNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         nums.sort()
#         n = len(nums)

#         for i in range(n):
#             if i != nums[i]:
#                 return i

#         return n