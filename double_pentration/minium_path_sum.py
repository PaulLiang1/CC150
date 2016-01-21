class Solution:
    """
    @param grid: a list of lists of integers.
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):

        if grid is None or len(grid) == 0:
            return -1

        if grid[0] is None or len(grid[0]) == 0:
            return -1

        m = len(grid)
        n = len(grid[0])

        mat = [
            [0 for x in xrange(n)] for x in xrange(m)
        ]

        # insert base cases
        base = 0
        for i in xrange(n):
            base += grid[0][i]
            mat[0][i] = base

        base = 0
        for i in xrange(m):
            base += grid[i][0]
            mat[i][0] = base

        for i in xrange(1, m):
            for j in xrange(1, n):
                mat[i][j] = min(
                        mat[i - 1][j],
                        mat[i][j - 1]
                    ) + grid[i][j]

        return mat[-1][-1]
