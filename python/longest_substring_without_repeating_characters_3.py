class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        d = {}
        o = 0
        max_len = 0
        i = 0

        for c in s:
            if c in d:
                o = max(d[c], o)
            
            max_len = max(max_len, i - o + 1)
            d[c] = i + 1
            i += 1

        return max_len
