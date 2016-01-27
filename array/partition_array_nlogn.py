class Solution:
    """
    @param nums: The integer array you should partition
    @param k: As description
    @return: The index after partition
    """
    def partitionArray(self, nums, k):

        if nums is None or len(nums) == 0:
            return 0

        nums.sort()

        low = 0
        high = len(nums) - 1

        while low + 1 < high:
            mid = low + (high - low) / 2

            if nums[mid] == k:
                high = mid

            elif nums[mid] < k:
                low = mid

            else:
                high = mid

        if nums[low] >= k:
            return low
        elif nums[high] >= k:
            return high
        return len(nums)
        
