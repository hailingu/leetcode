class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        d = {}
        o = 0
        max_len = 0
        tmp_len = 0
        i = 0

        for c in s:
            if c not in d or (c in d and o > d[c]):
                d[c] = i
            else:
                tmp_len = i - o
                max_len = tmp_len if tmp_len > max_len else max_len
                o = d[c] + 1
                d[c] = i
            i += 1

        tmp_len = i - o
        max_len = tmp_len if tmp_len > max_len else max_len
        return max_len
