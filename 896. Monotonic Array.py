class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return all(nums[i] <= nums[i+1] for i in range(len(nums)-1)) or \
               all(nums[i] >= nums[i+1] for i in range(len(nums)-1))



































































# class Solution(object):
#     def isMonotonic(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         if len(nums) <= 1:
#             return True

#         increasing = decreasing = True

#         for i in range(1, len(nums)):
#             if nums[i] > nums[i - 1]:
#                 decreasing = False
#             if nums[i] < nums[i - 1]:
#                 increasing = False

#         return increasing or decreasing









































# class Solution(object):
#     def isMonotonic(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
        
#         if len(nums) <= 1:
#             return True

#         temp = nums[:]
#         temp.sort()

#         if nums == temp or nums == temp[::-1]:
#             return True
#         else:
#             return False