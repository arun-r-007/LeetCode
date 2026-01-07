class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        dic = {}
        n = len(s)
        max_leng = 0

        for r in range(n):

            if s[r] in dic and dic[s[r]] >= l :
                l = dic[s[r]] + 1

            dic[s[r]] = r
            max_leng = max(max_leng,r-l+1)

        return max_leng