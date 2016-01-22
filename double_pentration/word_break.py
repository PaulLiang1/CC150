class Solution:
    # @param s: A string s
    # @param dict: A dictionary of words dict
    def wordBreak(self, s, dict):

        if s is None:
            return False

        if len(dict) == 0:
            return len(s) == 0

        max_word_length = max([len(k) for k in dict.keys()])
        arr = [False] * (len(s) + 1)
        arr[0] = True

        for i in xrange(1, len(s) + 1):
            last_word_length = 1

            while last_word_length <= max_word_length and last_word_length <= i:
                if arr[i - last_word_length] is False:
                    last_word_length += 1
                    continue

                word = s[i - last_word_length:i]

                if word in dict:
                    arr[i] = True
                    break

                last_word_length += 1

        return arr[-1]
        
