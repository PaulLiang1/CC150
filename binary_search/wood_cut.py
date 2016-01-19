class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    return: The maximum length of the small pieces.
    """
    def woodCut(self, L, k):

        if L is None or len(L) == 0:
            return 0

        max_wood_len = max(L)

        low = 1
        high = max_wood_len

        while low + 1 < high:
            mid = low + (high - low) / 2

            if self.wood_count(L, mid) >= k:
                low = mid
            else:
                high = mid

        if self.wood_count(L, high) >= k:
            return high
        elif self.wood_count(L, low) >= k:
            return low
        return 0

    def wood_count(self, L, k):
        ret = 0
        for l in L:
            ret += l / k
        return ret
