class Solution:

    def subsets(self, S):
        # boundary check
        if S is None or len(S) == 0:
            return list()

        result = list()
        tmp_list = list()

        S = sorted(S)
        return self.subsets_helper(result, tmp_list, S, 0)

    def subsets_helper(self, result, tmp_list, S, index):
        result.append(tmp_list[:])

        for i in xrange(index, len(S)):
            tmp_list.append(S[i])
            self.subsets_helper(result, tmp_list, S, i + 1)
            tmp_list.pop(-1)

        return result


if __name__ == '__main__':
    s = Solution()
    print s.subsets([1, 2])
