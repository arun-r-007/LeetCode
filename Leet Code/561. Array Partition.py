class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        b = int(len(nums))
        sum = 0
        for i in range(0,b,2):
            sum = sum + min(nums[i],nums[i+1])
        return sum

        

a = Solution() 
print(a.arrayPairSum([1,4,3,2]))






# class Solution:
#   def arrayPairSum(self, nums: list[int]) -> int:
#     return sum(sorted(nums)[::2])