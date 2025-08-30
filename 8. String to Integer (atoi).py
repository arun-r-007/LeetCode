class Solution(object):
    def myAtoi(self, s):
        i, n = 0, len(s)
        sign = 1
        result = 0

        while i < n and s[i] == ' ':
            i += 1

        if i < n:
            if s[i] == '-':
                sign = -1
                i += 1
            elif s[i] == '+':
                i += 1

        INT_MIN, INT_MAX = -2147483648, 2147483647

        while i < n and '0' <= s[i] <= '9':
            digit = ord(s[i]) - ord('0')

            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            result = result * 10 + digit
            i += 1

        return sign * result
    