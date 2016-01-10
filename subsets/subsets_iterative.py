class Solution:

    def subsets(self, S):
        # boundary check
        if S is None or len(S) == 0:
            return list()

        result = list()

        # There are 2^len(S) solutions
        for i in xrange(1 << len(S)):
            bit_pos = 0
            solution = list()

            while i != 0:
                bit = i & 1

                if bit != 0:
                    solution.append(S[bit_pos])

                bit_pos += 1
                i = i >> 1

            result.append(solution)

        return result

if __name__ == '__main__':
    s = Solution()
    print s.subsets([1, 2])
    print s.subsets([1, 2, 3])
