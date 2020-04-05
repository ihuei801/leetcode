###
# DP
# Time Complexity: O(n)
# Space Complexity: O(1)
###
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        if len(s) == 1:
            return int(self.valid(s))
        
        dp_2 = 1
        dp_1 = int(self.valid(s[0]))
        for i in xrange(1, len(s)):
            dp = 0
            if self.valid(s[i-1:i+1]):
                dp += dp_2
            if self.valid(s[i]):
                dp += dp_1
            dp_2 = dp_1
            dp_1 = dp
        return dp_1
    def valid(self, s):
        return s[0] != "0" and int(s) > 0 and int(s) <= 26
