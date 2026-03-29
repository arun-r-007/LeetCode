class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        tp_min = []

        for i in timePoints:
            hour = int(i.split(":")[0])
            minute = int(i.split(":")[1])

            tp_min.append(hour*60 + minute)

        tp_min.sort()

        min_diff = float('inf')

        n = len(tp_min)

        for i in range(1,n):
            min_diff = min(min_diff, tp_min[i] - tp_min[i-1])

        return min(min_diff, tp_min[0] + 1440 - tp_min[n-1])