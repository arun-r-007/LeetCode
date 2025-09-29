class Solution(object):
    def largestTriangleArea(self, points):
        def cross(o, a, b):
            return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

        points = sorted(points)
        lower, upper = [], []
        for p in points:
            while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
                lower.pop()
            lower.append(p)
        for p in reversed(points):
            while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
                upper.pop()
            upper.append(p)
        hull = lower[:-1] + upper[:-1]

       
        n = len(hull)
        max_area = 0.0
        for i in range(n):
            k = (i+2) % n
            for j in range(i+1, n):
                while True:
                    cur = abs(cross(hull[i], hull[j], hull[k]))
                    nxt = abs(cross(hull[i], hull[j], hull[(k+1) % n]))
                    if nxt > cur:
                        k = (k+1) % n
                    else:
                        break
                max_area = max(max_area, abs(cross(hull[i], hull[j], hull[k])) / 2.0)

        return max_area













































# class Solution(object):
#     def largestTriangleArea(self, points):
#         """
#         :type points: List[List[int]]
#         :rtype: float
#         """
#         def area(p1, p2, p3):
#             return 0.5 * abs(
#                 p1[0]*(p2[1]-p3[1]) +
#                 p2[0]*(p3[1]-p1[1]) +
#                 p3[0]*(p1[1]-p2[1])
#             )
        
#         n = len(points)
#         max_area = 0.0
#         for i in range(n):
#             for j in range(i+1, n):
#                 for k in range(j+1, n):
#                     max_area = max(max_area, area(points[i], points[j], points[k]))
#         return max_area