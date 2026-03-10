class Solution:
    def count_non_minimum(self, nums):
        m = min(nums)
        count = 0
        
        for x in nums:
            if x > m:
                count += 1
                
        return count