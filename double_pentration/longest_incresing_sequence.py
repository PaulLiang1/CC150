class Solution:
    """
    @param nums: The integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):

        if nums is None or len(nums) == 0:
            return 0

        if len(nums) == 1:
            return 1

        arr = [list() for x in xrange(len(nums))]
        arr[0].append(nums[0])

        max_ret = -1

        for i in xrange(1, len(nums)):
            max_j_len = -1
            max_j_idx = -1

            for j in xrange(0, i):
                if arr[j][-1] > nums[i]:
                    continue

                if len(arr[j]) > max_j_len:
                    max_j_len = len(arr[j])
                    max_j_idx = j

            arr[i] = arr[max_j_idx][:]
            arr[i].append(nums[i])

            max_ret = max(max_ret, len(arr[i]))

        return max_ret
