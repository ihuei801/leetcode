class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        re = ""
        while n:
            n -= 1
            i = n % 26
            re = chr(ord('A') + i) + re
            n /= 26
        return re