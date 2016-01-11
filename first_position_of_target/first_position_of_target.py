class Solution:

    def binarySearch(self, nums, target):

        # boundary check
        if nums is None or len(nums) == 0 or not isinstance(target, int):
            return -1

        low = 0
        high = len(nums) - 1

        while low + 1 < high:
            mid = low + (high - low) / 2

            if nums[mid] == target:
                high = mid

            elif nums[mid] > target:
                high = mid

            else:
                low = mid

        if nums[low] == target:
            return low

        if nums[high] == target:
            return high

        return -1

if __name__ == '__main__':
    s = Solution()

    assert 2 == s.binarySearch(
        nums=[1, 2, 3, 4, 5, 10],
        target=3
    )
