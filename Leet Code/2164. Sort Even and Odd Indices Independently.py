class Solution(object):
    def sortEvenOdd(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums)

        even = []
        odd = []

        # separate
        for i in range(n):
            if i % 2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])

        # sort
        even.sort()
        odd.sort(reverse=True)

        e = 0
        o = 0

        # rebuild array
        for i in range(n):
            if i % 2 == 0:
                nums[i] = even[e]
                e += 1
            else:
                nums[i] = odd[o]
                o += 1

        return nums

        
















# class Solution(object):
#     def sortEvenOdd(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         n = len(nums)
#         lst =[0] * n

#         temp_odd = []
#         temp_even = []

#         for i in range(n):
#             if i % 2 == 0:
#                 temp_even.append(nums[i])
#             else:
#                 temp_odd.append(nums[i])

#         temp_odd.sort(reverse=True)
#         temp_even.sort()
        
#         for i in range(n):
#             if i % 2 == 0:
#                 lst[i] = temp_even.pop(0)
#             else:
#                 lst[i] = temp_odd.pop(0)
            
#         return lst