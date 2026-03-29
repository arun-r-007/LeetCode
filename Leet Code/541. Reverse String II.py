class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        n = len(s)
        ls = []
        for i in range(0,n,2*k):
            ls.append(s[i:i+k][::-1])
            ls.append(s[i+k:i+2*k])

        return "".join(ls)