###
# Back Tracking
# Time Complexity: O(log(n)) cnt is multiply by 10 each time
###
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        start = 1
        cnt = 9
        while n > cnt * l:
            n -= cnt * l
            cnt *= 10
            start *= 10
            l += 1
        start += (n-1)/l
        start = str(start)
        return int(start[(n-1) % l])
        
        