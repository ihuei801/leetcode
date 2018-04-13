class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        re = ""
        while n:
            n -= 1
            re = chr(ord('A') + n % 26) + re
            n /= 26
        return re