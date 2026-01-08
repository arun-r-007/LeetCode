class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0: return 0
        dic = {0:0,1:1}

        for i in range(n+1):
            if i in dic:
                continue
            else:
                dic[i] = dic[i-1] + dic[i-2]

        return next(reversed(dic.values()))
                













# class Solution(object):
#     def fib(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """

#         if n <= 1:
#             return n
#         a , b = 0 , 1

#         for _ in range(2, n + 1):
#             temp = a + b
#             a = b
#             b = temp
        
#         return b