# http://www.lintcode.com/en/problem/find-peak-element/

class Solution:

    def findPeak(self, A):

        # boundary check
        if A is None or len(A) < 3:
            return -1

        # base case
        if len(A) == 3:
            return 1

        low = 0
        high = len(A) - 1

        while low + 1 < high:
            mid = low + (high - low) / 2

            if A[mid] > A[mid + 1] and A[mid] > A[mid - 1]:
                return mid

            elif A[mid + 1] > A[mid]:
                low = mid

            else:
                high = mid

        if mid[low] > mid[low - 1] and mid[low] > mid[low + 1]:
            return low

        if mid[high] > mid[high - 1] and mid[high] > mid[high + 1]:
            return high

        return -1
