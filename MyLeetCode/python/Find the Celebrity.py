###
# Time Complexity: O(n)
# Space Complexity: O(1)
###
# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return -1
        c = 0
        for p in xrange(1, n):
            if knows(c, p):
                c = p
        for p in xrange(n):
            if p != c and (knows(c, p) or not knows(p, c)):
                return -1
        return c