class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pos = 0
        
        for num in nums:
            if num != 0:
                nums[pos] = num
                pos += 1
        
        for i in range(pos, len(nums)):
            nums[i] = 0



















# class Solution(object):
#     def moveZeroes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
#         count = 0
#         reach = 0
        
#         for i in nums:
#             if i == 0:
#                 count += 1

#         nums += [0] * count

#         for i in nums:
#             if i == 0 and reach < count :
#                 nums.remove(i)
#                 reach += 1
        