###
# Binary Search
# Time Complexity: O(logn)
###
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n
        while l + 1 < r:
            mid = (l + r) / 2
            if isBadVersion(mid):
                r = mid
            else:
                l = mid
        if isBadVersion(l): 
            return l
        else:
            return r