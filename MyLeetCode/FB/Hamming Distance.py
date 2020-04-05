###
# XOR: different bit
# n & (n-1): set rightmost bit to 0
# Time Complexity: O(1)
# Space Complexity: O(1)
###
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        d = 0
        n = x ^ y
        while n:
            d += 1
            n &= (n-1)
        return d
        
        
        