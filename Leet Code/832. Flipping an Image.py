class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        
        for i in range(len(image)):
            left = 0
            right = len(image[i]) - 1

            while left<=right:
                temp = image[i][left]
                image[i][left] = 1-image[i][right]
                image[i][right] = 1-temp
                left+=1
                right-=1

        return image


print(Solution().flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))