import sys

class Solution:
    """
    @param triangle: a list of lists of integers.
    @return: An integer, minimum path sum.
    """
    def minimumTotal(self, triangle):

        if triangle is None or len(triangle) == 0:
            return -1

        if triangle[0] is None or len(triangle[0]) == 0:
            return -1

        n = len(triangle)
        mat = [
            [sys.maxint for x in xrange(n)] for x in xrange(n)
        ]

        self.minimumTotalHelper(mat, triangle, 0, 0)
        return mat[0][0]

    def minimumTotalHelper(self, mat, triangle, i, j):
        n = len(triangle)

        if not 0 <= i < n:
            return 0

        if not 0 <= j < n:
            return 0

        if mat[i][j] != sys.maxint:
            return mat[i][j]

        mat[i][j] = min(
            self.minimumTotalHelper(mat, triangle, i + 1, j),
            self.minimumTotalHelper(mat, triangle, i + 1, j + 1)
        ) + triangle[i][j]

        return mat[i][j]
        
