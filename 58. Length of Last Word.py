class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        s = s.rstrip()
        count = 0
        for i in reversed(s):
            if i != " ":
                count+=1
            else :
                break
        return count
        