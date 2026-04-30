class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        ls = []
        n = len(nums)

        for i in range(0, n, 2):          
            ls.extend([nums[i+1]] * nums[i])      

        return ls