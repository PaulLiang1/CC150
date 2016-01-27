class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """
    def sortColors(self, nums):

        if nums is None or len(nums) == 0:
            return nums

        zero_idx = 0
        two_idx = len(nums) - 1
        i = 0

        while i <= two_idx:
            if nums[i] == 0:
                nums[zero_idx], nums[i] = nums[i], nums[zero_idx]
                zero_idx += 1
                i += 1

            elif nums[i] == 1:
                i += 1

            elif nums[i] == 2:
                nums[two_idx], nums[i] = nums[i], nums[two_idx]
                two_idx -= 1
