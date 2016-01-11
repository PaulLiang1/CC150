"""
Definition of ArrayReader:
class ArrayReader:
    def get(self, index):
        # this would return the number on the given index
        # if there is no number on that index, return -1
"""
class Solution:

    def searchBigSortedArray(self, reader, target):

        # boundary check
        if reader is None or target is None or reader.get(0) == -1:
            return -1

        idx = 1
        prev_idx = 0

        while reader.get(idx) < target and reader.get(idx) != -1:
            prev_idx = idx
            idx *= 2

        high = idx
        low = prev_idx

        while low + 1 < high:
            mid = low + (high - low) / 2
            mid_val = reader.get(mid)

            if mid_val == target:
                high = mid

            elif mid_val > target:
                high = mid

            else:
                low = mid

        if reader.get(low) == target:
            return low

        if reader.get(high) == target:
            return high

        return -1
