class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
         
        string = str(x)
        string_rev = string[::-1]

        if string == string_rev:
            return True
        else:
            return False