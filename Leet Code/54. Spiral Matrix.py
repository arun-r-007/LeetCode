class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        lst1 = []
        
        while matrix:
            lst1 += matrix.pop(0)   # take first row

            if not matrix:
                break

            rows = len(matrix)
            cols = len(matrix[0])
            trans = []

            for j in range(cols):
                temp = []
                for i in range(rows):
                    temp.append(matrix[i][j])
                trans.append(temp)

            matrix = trans[::-1]   # reverse rows (rotate)

        return lst1