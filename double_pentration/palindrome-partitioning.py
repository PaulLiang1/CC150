class Solution:

    def is_palindrome(self, string):
        return string == string[::-1]

    def partition(self, s):
        if s is None or len(s) == 0:
            return list()

        result = list()
        self.partition_helper(s, result, list(), 0)
        return result

    def partition_helper(self, s, result, tmp_arr, index):

        if index == len(s):
            result.append(tmp_arr[:])
            return

        for i in xrange(index, len(s)):
            prefix = s[index:i + 1]
            if self.is_palindrome(prefix) is False:
                continue

            tmp_arr.append(prefix)
            self.partition_helper(s, result, tmp_arr, i + 1)
            tmp_arr.pop(-1)
