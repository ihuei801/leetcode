###
# Bit Manipulation
# Time Complexity: O(1)
###
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        return not n & (n-1)
        
        