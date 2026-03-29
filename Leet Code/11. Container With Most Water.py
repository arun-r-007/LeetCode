class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        l = 0
        r = len(height)-1
        maxa = 0
        
        while l < r:
            maxa = max(maxa, min(height[l], height[r])*(r-l))
            if height[l] < height[r]:
                l+=1
            else : r-=1

        return maxa










# class Solution(object):
#     def maxArea(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         left = 0
#         right = len(height) - 1
#         max_area = 0
#         while left < right:
#             area = (right - left ) * min(height[left], height[right])
#             if area > max_area:
#                 max_area = area
#             if height[left] < height[right]:
#                 left += 1
#             else:
#                 right -= 1
#         return max_area