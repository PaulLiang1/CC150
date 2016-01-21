class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):

        if n == 0:
            return 1

        if n == 1:
            return 1

        if n == 2:
            return 2

        arr = [0] * (n + 1)

        arr[0] = arr[1] = 1

        for i in xrange(2, n + 1):
            arr[i] = arr[i - 1] + arr[i - 2]

        return arr[-1]
