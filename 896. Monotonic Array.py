class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        if len(nums) <= 1:
            return True

        temp = nums[:]
        temp.sort()

        if nums == temp or nums == temp[::-1]:
            return True
        else:
            return False