from itertools import product

class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []

        dic = {
            '2': "abc", '3': "def", '4': "ghi", '5': "jkl",
            '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"
        }

        letters = [dic[d] for d in digits]

        result = [''.join(p) for p in product(*letters)]

        return result
    

# Example usage:
sol = Solution()
print(sol.letterCombinations("23"))  # Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]