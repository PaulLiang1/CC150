class Solution:
    """
    @param n and m: positive integer(1 <= n , m <= 100)
    @return an integer
    """
    def uniquePaths(self, m, n):

        mat = [
            [1 for x in xrange(n)] for x in xrange(m)
        ]

        for i in xrange(1, m):
            for j in xrange(1, n):
                mat[i][j] = mat[i - 1][j] + mat[i][j - 1]

        return mat[-1][-1]
