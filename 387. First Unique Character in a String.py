class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        fre = {}
        for i in s:
            if i in fre:
                fre[i] += 1
            else:
                fre[i] = 1

        n = len(s)

        for i in range(n):
            if fre[s[i]] == 1:
                return i

        return -1