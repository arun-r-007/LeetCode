class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # return sorted(s) == sorted(t)

        if len(s) != len(t):
            return False

        count = {}

        for i in s:
            count[i] = count.get(i, 0) + 1

        for i in t:
            count[i] = count.get(i, 0) - 1

        for value in count.values():
            if value != 0:
                return False

        return True















# class Solution(object):
#     def isAnagram(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         return sorted(s) == sorted(t)