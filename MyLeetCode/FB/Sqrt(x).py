###
# Binary Search
# Time Complexity: O(logn)
# Space Complexity: O(1)
###
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 0:
            return 0
        if x == 1:
            return 1
        l, r = 1, x
        while l + 1 < r:
            mid = (l + r)/2
            if mid*mid == x:
                return mid
            elif mid*mid < x:
                l = mid
            else:
                r = mid
        if r*r <= x:
            return r
        else:
            return l