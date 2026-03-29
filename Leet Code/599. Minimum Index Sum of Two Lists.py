class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        min_val = float('inf')
        result = []

        for i in list1:
            if i in list2:
                index_sum = list1.index(i) + list2.index(i)

                if index_sum < min_val:
                    min_val = index_sum
                    result = [i]

                elif index_sum == min_val:
                    result.append(i)

        return result






















# class Solution(object):
#     def findRestaurant(self, list1, list2):
#         """
#         :type list1: List[str]
#         :type list2: List[str]
#         :rtype: List[str]
#         """
#         result = []
#         result2 = []
#         for i in list1:
#             if i in list2 :
#                 result.append(i)

#         min_val = float('inf')

#         for i in result:
#             index_sum = list1.index(i) + list2.index(i)

#             if index_sum < min_val:
#                 min_val = index_sum
#                 result2 = [i]

#             elif index_sum == min_val:
#                 result2.append(i)

#         return result2