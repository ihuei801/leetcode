###
# DP
# Time Complexity: O(m*n)
# Space Complexity: O(m*n)
# State: dp[i][j] whether the first i in s match the first j in p
# Function: if p[j-1] == "*" dp[i][j] = dp[i][j-2] (zero) or ((s[i-1] == p[j-2] or p[j-2] == '.' ) and dp[i-1][j]) (more)
#           else: dp[i][j] = dp[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '.')
# Initialization: dp[0][0] = True
# Answer: dp[len(s)][len(p)]
###
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not s and not p:
            return True
        if not p:
            return False
        dp = [[False] * (len(p) + 1) for i in xrange(len(s) + 1)]
        dp[0][0] = True
        for i in xrange(len(s) + 1):
            for j in xrange(1, len(p) + 1):
                if p[j-1] == '*':
                    dp[i][j] = dp[i][j-2] or (i > 0 and (s[i-1] == p[j-2] or p[j-2] == '.') and dp[i-1][j])
                else:
                    dp[i][j] = i > 0 and dp[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '.')
        return dp[len(s)][len(p)]