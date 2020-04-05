###
# Math
# Time Complexity: O(4^4) = O(1) 
# Space Complexity: O(1)
###
class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        ans = start = int(time[:2]) * 60 + int(time[3:])
        allowed = {int(c) for c in time if c != ":"}
        min_diff = float('inf')
        
        for h1, h2, m1, m2 in itertools.product(allowed, repeat=4):
            hour, minute = h1 * 10 + h2, m1 * 10 + m2
            if hour < 24 and minute < 60:
                cur = hour * 60 + minute
                diff = (cur - start) % (24 * 60)
                if 0 < diff < min_diff:
                    min_diff = diff
                    ans = cur
        return "{:02d}:{:02d}".format(*divmod(ans, 60))
        
        
        