class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):

        if A is None or len(A) == 0:
            return True

        if len(A) == 1 and A[0] != 0:
            return True

        prev_idx = 0
        idx = 0
        target = len(A) - 1

        jump = 0

        while True:
            if prev_idx == idx and prev_idx != 0:
                return False

            tmp = idx

            if idx == 0:
                idx += A[idx]
            else:
                idx += max(A[prev_idx:A[idx]])

            prev_idx = tmp
            jump += 1

            if idx >= target:
                break

            while A[idx] == 0 and idx >= prev_idx + 1:
                idx -= 1

        return jump
