class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def buildString(string):
            result = []
            for char in string:
                if char != '#':
                    result.append(char)
                elif result:
                    result.pop()
            return ''.join(result)
        
        return buildString(s) == buildString(t)
        

s = "ab#c"
t = "ad#c"
print(Solution().backspaceCompare(s,t))