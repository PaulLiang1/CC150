# http://www.lintcode.com/en/problem/search-for-a-range/

class Solution:

    def searchFirstOccurance(self, A, target):
        low = 0
        high = len(A) - 1

        while low + 1 < high:
            mid = low + (high - low) / 2

            if A[mid] == target:
                high = mid
            elif A[mid] < target:
                low = mid
            else:
                high = mid

        if A[low] == target:
            return low
        if A[high] == target:
            return high
        return -1


    def searchLastOccurance(self, A, target):
        low = 0
        high = len(A) - 1

        while low + 1 < high:
            mid = low + (high - low) / 2

            if A[mid] == target:
                low = mid
            elif A[mid] < target:
                low = mid
            else:
                high = mid

        if A[high] == target:
            return high
        if A[low] == target:
            return low

        return -1

    def searchRange(self, A, target):

        # boundary check
        if A is None or target is None or len(A) == 0:
            return [-1, -1]

        first_occurance = self.searchFirstOccurance(A, target)
        if first_occurance == -1:
            return [-1, -1]

        last_occurance = self.searchLastOccurance(A, target)

        return [first_occurance, last_occurance]
