class Solution:
    """
    @param A: sorted integer array A which has m elements,
              but size of A is m+n
    @param B: sorted integer array B which has n elements
    @return: void
    """
    def mergeSortedArray(self, A, m, B, n):
        i = m - 1
        j = n - 1
        index = m + n - 1

        while i >= 0 and j >= 0:

            if A[i] > B[j]:
                A[index] = A[i]
                index -= 1
                i -= 1
            else:
                A[index] = B[j]
                index -= 1
                j -= 1

        while i >= 0:
            A[index] = A[i]
            index -= 1
            i -= 1

        while j >= 0:
            A[index] = B[j]
            j -= 1
            index -= 1
