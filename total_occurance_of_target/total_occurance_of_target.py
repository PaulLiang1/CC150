class Solution:

    def findFirstOccurence(self, A, target):

        low = 0
        high = len(A) - 1

        while low + 1 < high:
            mid = low + (high - low) / 2

            if A[mid] == target:
                high = mid

            elif A[mid] > target:
                high = mid

            else:
                low = mid

        if A[low] == target:
            return low

        if A[high] == target:
            return high

        return -1

    def findLastOccurence(self, A, target):

        low = 0
        high = len(A) - 1

        while low + 1 < high:
            mid = low + (high - low) / 2

            if A[mid] == target:
                low = mid

            elif A[mid] > target:
                high = mid

            else:
                low = mid

        if A[high] == target:
            return high

        if A[low] == target:
            return low

        return -1

    def totalOccurrence(self, A, target):

        # boundary check
        if A is None or target is None or len(A) == 0:
            return 0

        first_occ = self.findFirstOccurence(A, target)

        if first_occ == -1:
            return 0

        last_occ = self.findLastOccurence(A, target)

        return last_occ - first_occ + 1

if __name__ == '__main__':
    s = Solution()

    assert 3 == s.totalOccurrence(
        A=[1, 3, 3, 3, 4, 5],
        target=3
    )
