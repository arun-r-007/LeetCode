








































# class Solution(object):
#     def isBalanced(self, num):
#         """
#         :type num: str
#         :rtype: bool
#         """
#         pointer = 0
#         odd = 0
#         even = 0
#         for ch in num:
#             if pointer % 2 == 0:
#                 even += int(ch)
#             else:
#                 odd += int(ch)
#             pointer += 1
        
#         return odd == even
        