class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        res = 0
        for i in nums:
            res ^= i
        return res


        # if nums == []:
        #     return NULL
        # else :
        #     n = len(nums)
        #     ls = []
        #     for i in range(n):
        #         if nums[i] in ls:
        #             ls.remove(nums[i])

        #         else :
        #             ls.append(nums[i])

        #     return ls[0]
        