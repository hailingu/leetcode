class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == None or len(s) == 0:
            return s
        
        nStr = '#'
        for c in s:
            nStr = nStr + c + '#'
        
        p = [0] * len(nStr)
        p[0] = 1
        idt, mx, hId, hmx = 0, 0, 0, 0
        
        i = 1
        while i < len(nStr):
            p[i] = 1 if i < mx else min(p[2 * idt -i], mx - i)
            while i + p[i] < len(nStr) and i >= p[i] and nStr[i + p[i]] == nStr[i - p[i]]:
                p[i] += 1

            if i + p[i] > mx:
                mx = i + p[i]
                idt = i

                if p[i] > p[hId]:
                    hId = idt
                    hmx = mx
            i += 1

        ans = ''
        r = hmx - hId - 1 
        tmp = nStr[hId - r: hId + r]
        for c in tmp:
            if c != '#':
                ans += c

        return ans
