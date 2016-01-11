class Solution:

    def closestNumber(self, A, target):

        # boundary check
        if A is None or target is None or len(A) == 0:
            return -1

        low = 0
        high = len(A) - 1

        while low + 1 < high:
            mid = low + (high - low) / 2

            if A[mid] == target:
                return mid

            elif A[mid] > target:
                high = mid

            else:
                low = mid

        if abs(target - A[low]) <= abs(target - A[high]):
            return low
        else:
            return high
