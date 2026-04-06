class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        seen = set()
        
        while n not in seen:
            if n == 1:
                return True
            seen.add(n)
            n = sum(int(d)**2 for d in str(n))
        
        return False























# class Solution(object):
#     def isHappy(self, n):
#         """
#         :type n: int
#         :rtype: bool
#         """

#         def cs(a):
#             sum = 0
#             while a != 0:
#                 b = a % 10
#                 sum += b*b
#                 a /= 10
#             return sum

#         slow = n
#         fast = n
#         while True:
#             slow = cs(slow)
#             fast = cs(cs(fast))
#             if fast == 1 or slow == 1:
#                 return True
#             if slow == fast:
#                 return False