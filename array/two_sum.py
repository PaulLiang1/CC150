class Solution:
    """
    @param numbers : An array of Integer
    @param target : target = numbers[index1] + numbers[index2]
    @return : [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):

        if numbers is None or len(numbers) == 0:
            return numbers

        hashmap = dict()

        for i, num in enumerate(numbers):
            hashmap[num] = i

        for i, num in enumerate(numbers):
            delta = target - num
            if delta not in hashmap:
                continue

            idx = hashmap[delta]

            if idx == i:
                continue
            elif i < idx:
                return [i + 1, idx + 1]
            else:
                return [idx + 1, i + 1]

        
