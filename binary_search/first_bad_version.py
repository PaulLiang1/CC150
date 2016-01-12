# http://www.lintcode.com/en/problem/first-bad-version/

#class SVNRepo:
#    @classmethod
#    def isBadVersion(cls, id)
#        # Run unit tests to check whether verison `id` is a bad version
#        # return true if unit tests passed else false.
# You can use SVNRepo.isBadVersion(10) to check whether version 10 is a
# bad version.
class Solution:

    cache = dict()
    def isBadVersion(self, n):
        if n in self.cache:
            return self.cache[n]
        else:
            result = SVNRepo.isBadVersion(n)
            self.cache[n] = result
            return result

    def findFirstBadVersion(self, n):

        # boundary check
        if n is None:
            return -1

        # base case
        if n == 0:
            return 0

        low = 1
        high = n

        while low + 1 < high:
            mid = low + (high - low) / 2

            low_result = self.isBadVersion(low)
            high_result = self.isBadVersion(high)
            mid_result = self.isBadVersion(mid)

            if mid_result is True:
                high = mid
            else:
                low = mid

        if self.isBadVersion(low) is True:
            return low

        else:
            return high
