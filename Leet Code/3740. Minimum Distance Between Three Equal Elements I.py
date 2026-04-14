class Solution(object):
    def minimumDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = float('inf')

        dict1 = {}

        for i in range(len(nums)):
            if nums[i] in dict1:
                dict1[nums[i]].append(i)
            else:
                dict1[nums[i]] = [i]  


        for key in dict1:
            indices = dict1[key]

            if len(indices) >= 3:
                for i in range(len(indices) - 2):
                    a = indices[i]
                    b = indices[i+1]
                    c = indices[i+2]

                    temp = abs(a - b) + abs(b - c) + abs(c - a)
                    ans = min(ans, temp)

        return ans if ans != float('inf') else -1























# class Solution(object):
#     def minimumDistance(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         n = len(nums)
#         ans = float('inf')

#         for i in range(n):
#             for j in range(i + 1, n):
#                 for k in range(j + 1, n):
#                     if nums[i] == nums[j] == nums[k]:
#                         dist = abs(i - j) + abs(j - k) + abs(k - i)
#                         ans = min(ans, dist)

#         return ans if ans != float('inf') else -1