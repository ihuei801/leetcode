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
        if n < 1:
            return -1
        l = 1
        r = n
        while l + 1 < r:
            mid = (l + r) / 2
            ans = guess(mid)
            if ans == 0:
                return mid
            elif ans == -1:
                r = mid
            else:
                l = mid
        if guess(l) == 0:
            return l
        else:
            return r