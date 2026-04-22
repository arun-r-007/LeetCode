class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse = True)

        final = 0

        n = len(citations)

        for i in range(n):
            if citations[i] >= i + 1:
                final = i + 1

        return final