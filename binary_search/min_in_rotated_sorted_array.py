class Solution:
    # @param num: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, num):
        A = num

        # boundary check
        if A is None or len(A) <= 1:
            return 0

        # base case 0
        if A[0] < A[1] and A[0] < A[-1]:
            return A[0]

        # base case 1
        if A[-1] < A[-2] and A[-1] < A[0]:
            return A[-1]

        low = 0
        high = len(A) - 1

        while low + 1 < high:
            mid = low + (high - low) / 2

            if A[low] < A[mid] and A[mid] > A[high]:
                low = mid

            elif A[low] > A[mid] and A[mid] < A[high]:
                high = mid

        if A[low] < A[high]:
            return A[low]
        else:
            return A[high]
        
