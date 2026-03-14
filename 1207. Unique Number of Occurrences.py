from collections import Counter

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        count = Counter(arr)

        return len(count.values()) == len(set(count.values()))

























# class Solution(object):
#     def uniqueOccurrences(self, arr):
#         """
#         :type arr: List[int]
#         :rtype: bool
#         """
#         dict1 = {}
#         set1 = set()

#         for i in arr:
#             if i in dict1:
#                 dict1[i] += 1
#             else:
#                 dict1[i] = 1

#         for i in dict1.values():
#             if i in set1:
#                 return False
#             else:
#                 set1.add(i)

#         return True