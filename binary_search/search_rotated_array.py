# http://www.lintcode.com/en/problem/search-in-rotated-sorted-array/#

class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : an integer
    """
    def search(self, A, target):

        # boundary check
        if A is None or target is None or len(A) == 0:
            return -1

        low = 0
        high = len(A) - 1

        while low + 1 < high:
            mid = low + (high - low) / 2

            if A[mid] == target:
                return mid

            ## M-H sorted
            if A[mid] < A[high] < A[low]:

                if A[mid] < target <= A[high]:
                    low = mid
                else:
                    high = mid

            ## L-M sorted
            else:

                if A[low] <= target < A[mid]:
                    high = mid

                else:
                    low = mid

        if A[low] == target:
            return low

        if A[high] == target:
            return high

        return -1
