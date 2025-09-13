class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """

        if num == 0:
            return "0"
        
        n = False

        if num < 0:
            n = True
            num = abs(num)

        ls = []

        while num > 0:
            remainder = num % 7
            ls.append(str(remainder))
            num = num // 7

        ls.reverse()

        rs = "".join(ls)

        if n:
            return "-" + rs
        else :
            return rs
        