class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be inserted
    @return : an integer
    """
    def searchInsert(self, A, target):
        # boundary case
        if A is None or target is None:
            return None

        if len(A) == 0:
            return 0

        low = 0
        high = len(A) - 1

        while low <= high:
            # prevent overflow
            mid = low + (high - low) / 2

            if A[mid] == target:
                return mid
            elif A[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return low
