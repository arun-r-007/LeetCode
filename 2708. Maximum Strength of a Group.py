class Solution(object):
    def maxStrength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return nums[0]
            
        negative_numbers = [num for num in nums if num < 0]
        if len(negative_numbers) % 2 != 0:
            negative_numbers.sort()
            nums.remove(negative_numbers[-1])

        new_list = [item for item in nums if item != 0]

        if new_list == []:
            return 0
        else :
            product = 1
            for x in new_list:
                product *= x
            return product