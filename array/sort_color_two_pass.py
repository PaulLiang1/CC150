class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """
    def sortColors(self, nums):

        if nums is None or len(nums) == 0:
            return nums

        hashmap = dict()

        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1

        for i in xrange(len(nums)):
            if i < hashmap[0]:
                nums[i] = 0
            elif i < hashmap[0] + hashmap[1]:
                nums[i] = 1
            else:
                nums[i] = 2
        
