class Solution:

    def strStr(self, source, target):

        # boundary check
        if source is None or target is None:
            return -1

        if len(target) > len(source):
            return -1

        # +1
        # Extreme case; do comparision when len(target) == len(source)
        for i in xrange(len(source) - len(target) + 1):
            for j in xrange(len(target)):
                if source[i + j] != target[j]:
                    break
            else:
                return i
        return -1


if __name__ == '__main__':
    s = Solution()
    print s.strStr('abc', 'cde')
    print s.strStr('abcde', 'cde')
