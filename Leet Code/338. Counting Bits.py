class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = [0] * (n + 1)

        for i in range(1, n + 1):
            result[i] = result[i >> 1] + (i & 1)

        return result






















# class Solution(object):
#     def countBits(self, n):
#         """
#         :type n: int
#         :rtype: List[int]
#         """
#         lst = []
#         result = []

#         for i in range(n+1):
#             lst.append(int(bin(i)[2:]))
#             result.append(str(lst[i]).count('1'))

#         # print(lst)
#         # print(result)

#         return result