class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) <= 2:
            return len(nums)

        i = 2  # write pointer

        for j in range(2, len(nums)):
            if nums[j] != nums[i-2]:
                nums[i] = nums[j]
                i += 1

        return i









# class Solution(object):
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         num_count = 0
#         p1 = 0

#         while nums and len(nums) > p1+1:
#             if nums[p1] == nums[p1+1]:
#                 num_count += 1
#             else:
#                 num_count = 0

#             if num_count >= 2:
#                 nums.pop(p1+1)
#                 continue

#             p1 += 1
            
#         return len(nums)