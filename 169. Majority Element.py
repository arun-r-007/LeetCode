class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict1 = {}

        for i in nums:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1

        key = max(dict1, key=dict1.get)

        return key