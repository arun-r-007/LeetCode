class Solution(object):
    def luckyNumbers(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        r = len(matrix)
        c = len(matrix[0])

        for i in range(r):
            row_min = min(matrix[i])
            col_index = matrix[i].index(row_min)

            is_max = True

            for i in range(r):
                if matrix[i][col_index] > row_min:
                    is_max =False
                    break
            
            if is_max:
                result.append(row_min)

        return result