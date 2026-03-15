class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        r = len(mat)
        c = len(mat[0])

        r_count = [0] * r
        c_count = [0] * c

        for i in range(r):
            for j in range(c):
                if mat[i][j] == 1:
                    r_count[i] += 1
                    c_count[j] += 1

        count = 0

        for i in range(r):
            for j in range(c):
                if mat[i][j] == 1 and r_count[i] == 1 and c_count[j] == 1:
                    count += 1

        return count