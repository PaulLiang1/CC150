class Solution:

    def permute(self, nums):
        # boundary check
        if nums is None:
            return list()

        perms = list()

        # base case
        if len(nums) == 0:
            # insert empty list for non-base case to insert
            perms.append(list())
            return perms

        else:
            item = nums[0]
            items_left = nums[1:]

            prev_perms = self.permute(items_left)

            for prev_perms_item in prev_perms:
                for i in xrange(len(prev_perms_item) + 1):
                    ret = prev_perms_item[:]
                    ret.insert(i, item)
                    perms.append(ret)
        return perms

if __name__ == '__main__':
    s = Solution()

    print s.permute([1, 2, 3])
