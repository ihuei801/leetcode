###
# Binary Search
# Time Complexity: O(logn)
# Space Complexity: O(logn)
###
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1/x
            n = -n
        if n == 0:
            return 1
        if n & 1:
            return x * self.myPow(x, n/2)**2
        else:
            return self.myPow(x, n/2)**2