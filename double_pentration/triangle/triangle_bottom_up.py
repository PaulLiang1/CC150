class Solution:
    """
    @param triangle: a list of lists of integers.
    @return: An integer, minimum path sum.
    """
    def minimumTotal(self, triangle):

        if triangle is None or len(triangle) == 0:
            return list()

        if triangle[0] is None or len(triangle[0]) == 0:
            return list()

        # create tmp result matrix
        mat = [[0 for x in xrange(len(triangle))] for x in xrange(len(triangle))]

        # traverse last row of triangle
        for i, num in enumerate(triangle[-1]):
            mat[len(triangle) - 1][i] = num

        for i in xrange(len(triangle) - 2, -1, -1):
            for j in xrange(0, i + 1):
                mat[i][j] = min(
                        mat[i + 1][j],
                        mat[i + 1][j + 1]
                    ) + triangle[i][j]

        return mat[0][0]
        
