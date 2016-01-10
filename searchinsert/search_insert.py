class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be inserted
    @return : an integer
    """
    def searchInsert(self, A, target):
        # boundary check
        if A is None or target is None:
            return None

        if len(A) == 0:
            return 0

        low = 0
        high = len(A)

        prev_mid = None
        while low <= high:
            mid = (low + high) / 2

            if prev_mid == mid:
                break

            if A[mid] == target:
                return mid

            if A[mid] > target:
                high = mid
            else:
                low = mid

            prev_mid = mid

        return high

if __name__ == '__main__':
    s = Solution()
    assert 0 == s.searchInsert([], 100)
    assert 1 == s.searchInsert([1], 100)
    assert None == s.searchInsert(None, None)
    assert 5 == s.searchInsert([1, 2, 3, 4, 5, 9], 6)
    assert 4 == s.searchInsert([1, 3, 5, 6, 8, 9], 7)
