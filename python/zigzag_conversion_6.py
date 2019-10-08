class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        l = len(s)
        if numRows <= 1 or (numRows >= l):
            return s

        ans = ''
        step = 2 * numRows - 2

        for i in range(numRows):
            j = 0
            while j + i < l:
                ans += s[j + i]
                if i != 0 and i != numRows - 1 and j + step - i < l:
                    ans += s[j + step - i]

                j += step
        return ans
