class Solution:

    def subsets(self, S):
        return self.subsets_helper(S, 0)

    def subsets_helper(self, sets, index):

        if len(sets) == index:
            all_subsets = list()
            all_subsets.append(list())
        else:
            all_subsets = self.subsets_helper(sets, index + 1)
            item = sets[index]

            more_subsets = list()
            for subset in all_subsets:
                _new_subset = subset[:]
                _new_subset.append(item)
                more_subsets.append(_new_subset)

            all_subsets += more_subsets
        return all_subsets

if __name__ == '__main__':
    s = Solution()

    print s.subsets([0, 1, 2])
