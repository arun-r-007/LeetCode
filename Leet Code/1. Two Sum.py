class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict1 = {}

        n = len(nums)

        for i in range(n):

            check = target - nums[i]
            
            if check in dict1:
                return [i,dict1[check]]
            
            dict1[nums[i]] = i

        return None