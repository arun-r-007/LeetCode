class Solution(object):
    def constructTransformedArray(self, nums):
        n = len(nums)
        result = [None] * n

        for i in range(n):
            if nums[i] == 0:
                result[i] = nums[i]
            else:
                new_idx = (i + nums[i]) % n
                result[i] = nums[new_idx]

        return result

    

# Example usage:
sol = Solution()
print(sol.constructTransformedArray([3,-2,1,1])) 





















# class Solution(object):
#     def constructTransformedArray(self, nums):
#         n = len(nums)
#         original = nums[:]  

#         for i in range(n):
#             if original[i] == 0:
#                 nums[i] = 0
#             else:
#                 new_idx = (i + original[i]) % n
#                 nums[i] = original[new_idx]

#         return nums
