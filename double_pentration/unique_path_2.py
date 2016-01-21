class Solution:
    """
    @param obstacleGrid: An list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):

        if obstacleGrid is None or len(obstacleGrid) == 0:
            return -1

        if obstacleGrid[0] is None or len(obstacleGrid[0]) == 0:
            return -1

        row = len(obstacleGrid)
        col = len(obstacleGrid[0])

        mat = [
            [1 for i in xrange(col)] for i in xrange(row)
        ]

        obstacle_found = False
        for i in xrange(row):
            if obstacleGrid[i][0] == 1:
                obstacle_found = True

            if obstacle_found is True:
                mat[i][0] = 0

        obstacle_found = False
        for i in xrange(col):
            if obstacleGrid[0][i] == 1:
                obstacle_found = True

            if obstacle_found is True:
                mat[0][i] = 0

        for i in xrange(1, row):
            for j in xrange(1, col):

                if obstacleGrid[i][j] == 1:
                    mat[i][j] = 0
                else:
                    mat[i][j] = mat[i-1][j] + mat[i][j-1]

        return mat[-1][-1]
                    
