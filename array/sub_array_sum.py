class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number
             and the index of the last number
    """
    def subarraySum(self, nums):

        if nums is None or len(nums) == 0:
            return list()

        hashmap = dict()
        hashmap[0] = -1

        sum = 0
        for i, num in enumerate(nums):
            sum += num

            if sum in hashmap:
                return [hashmap[sum] + 1, i]

            hashmap[sum] = i

        return list()
