class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = int(''.join(map(str,digits))) + 1
        digits[:] = list(map(int, str(num)))
        return digits
    