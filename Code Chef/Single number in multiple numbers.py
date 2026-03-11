class Solution:
    def singleNumber(self, nums):
        # write your code here
        
        dict1 = {}
        
        for num in nums:
            if num in dict1:
                dict1[num] += 1
            else:
                dict1[num] = 1
        
        for key in dict1:
            if dict1[key] == 1:
                return key