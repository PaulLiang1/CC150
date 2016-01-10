from collections import deque

class Solution:

    def permute(self, nums):
        # boundary check
        if nums is None:
            return list()
        perms = list()

        queue = deque()
        # insert base case
        queue.append((list(), 0))

        while len(queue) > 0:
            perm_str, index = queue.popleft()

            # job done, write to output
            if len(perm_str) == len(nums):
                perms.append(perm_str)

            else:
                # insert num[i] into every possible position
                # then push back to queue
                for pos in xrange(len(perm_str) + 1):
                    new_str = perm_str[:]
                    new_str.insert(pos, nums[index])
                    queue.append((new_str, index + 1))

        return perms

if __name__ == '__main__':
    s = Solution()

    print s.permute([1, 2, 3])
