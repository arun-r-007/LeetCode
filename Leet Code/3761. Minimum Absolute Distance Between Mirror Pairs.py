class Solution(object):
    def reverse(self, x):
        rev = 0
        while x > 0:
            rev = rev * 10 + x % 10
            x //= 10
        return rev

    def minMirrorPairDistance(self, nums):
        mpp = {}
        n = len(nums)
        ans = 10 ** 6

        for i in range(n):
            if nums[i] in mpp:
                ans = min(ans, i - mpp[nums[i]])
            mpp[self.reverse(nums[i])] = i

        return -1 if ans == 10 ** 6 else ans














        # n = len(nums)
        # ans = float('inf')
        
        # for i in range(n):
        #     temp = int(str(abs(nums[i]))[::-1])

        #     for j in range(i + 1, n):
        #         if nums[j] == temp:
        #             ans = min(ans, abs(i - j))

        # if ans == float('inf'):
        #     return -1
        # return ans