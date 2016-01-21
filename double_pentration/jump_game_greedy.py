class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):

        if A is None or len(A) == 0:
            return False

        if len(A) == 1:
            return True

        idx = 0
        prev_idx = -1
        target = len(A) - 1

        while True:
            if idx == prev_idx:
                return False

            prev_idx = idx
            idx += A[idx]

            if idx >= target:
                return True

            while A[idx] == 0 and idx >= prev_idx + 1:
                idx -= 1

        return False
