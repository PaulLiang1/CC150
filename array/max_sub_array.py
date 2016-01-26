
class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """
    def maxSubArray(self, nums):

        if nums is None or len(nums) == 0:
            return None

        arr = [0] * len(nums)
        arr[0] = nums[0]
        max_val = nums[0]

        for i, num in enumerate(nums):
            if i == 0:
                continue

            arr[i] = max(arr[i - 1], 0) + num
            if arr[i] > max_val:
                max_val = arr[i]

        return max_val
        
