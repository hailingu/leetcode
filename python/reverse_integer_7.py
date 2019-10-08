class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        sgn = 1 if x > 0 else -1
        x *= sgn

        ans = 0
        while x != 0:
            ans = ans * 10 + x % 10
            x = x / 10

        ans *= sgn
        return 0 if ans > 2147483647 or ans < -2147483648 else ans

