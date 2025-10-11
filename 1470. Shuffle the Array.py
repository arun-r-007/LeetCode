class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        nums2 = nums[n:]
        nums1 = nums[:n]

        res = []

        for x, y in zip(nums1,nums2):
            res.append(x)
            res.append(y)

        return res