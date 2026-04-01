class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        s1 = min(strs)
        s2 = max(strs)
        
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                return s1[:i]
        
        return s1























# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#         if not strs:
#             return ""
        
#         if len(strs) == 1:
#             return strs[0]
        
#         for s in strs:
#             if s == "":
#                 return ""
        
#         prefix = strs[0]
        
#         for i in range(1, len(strs)):
#             while not strs[i].startswith(prefix):
#                 prefix = prefix[:-1]
#                 if prefix == "":
#                     return ""
        
#         return prefix
    