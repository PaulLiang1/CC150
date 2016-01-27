import sys

class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target : An integer
    @return : return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):

        if numbers is None or len(numbers) < 3:
            return -1

        numbers.sort()

        ret = sys.maxint
        for i in xrange(0, len(numbers) - 2):
            left = i + 1
            right = len(numbers) - 1

            while left < right:
                _sum = numbers[i] + numbers[left] + numbers[right]

                if _sum == target:
                    return _sum

                elif _sum < target:
                    left += 1

                else:
                    right -= 1

                if abs(_sum - target) < abs(ret - target):
                    ret = _sum

        return ret
