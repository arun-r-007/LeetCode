class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        
        for char in s:
            if char in '([{':
                stack.append(char)
            elif char in ')]}':
                if not stack:
                    return False
                if stack.pop() != pairs[char]:
                    return False
        
        return len(stack) == 0


print(Solution().isValid("(]"))