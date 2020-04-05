###
# Binary Search
# Time Complexit: O(logn)
# Space Complexity: O(1)
###
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n
        l, r = 1, n
        while l + 1 < r:
            mid = (l + r) / 2
            g = guess(mid)
            if g == 0:
                return mid
            elif g < 0:
                r = mid
            else:
                l = mid
        return l if guess(l) == 0 else r
        