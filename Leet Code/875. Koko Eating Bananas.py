class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        left, right = 1, max(piles)

        while left <= right:
            mid = (left + right) // 2
            hours = 0

            for pile in piles:
                hours += (pile + mid - 1) // mid  # ceil division

            if hours <= h:
                right = mid - 1   # try slower speed
            else:
                left = mid + 1    # need faster speed

        return left