class Solution(object):
    def generateParenthesis(self, n):
        result = []

        def backtrack(current, open_used, close_used):
            # If the string is complete
            if len(current) == 2 * n:
                result.append(current)
                return

            # Add '(' if we still can
            if open_used < n:
                backtrack(current + "(", open_used + 1, close_used)

            # Add ')' if it won't break validity
            if close_used < open_used:
                backtrack(current + ")", open_used, close_used + 1)

        backtrack("", 0, 0)
        return result

