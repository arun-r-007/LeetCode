class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        if len(s) != len(indices):
            return None

        n = len(indices)
        ls = [""] * n  
        for i in range(n):
            ls[indices[i]] = s[i]

        return "".join(ls)