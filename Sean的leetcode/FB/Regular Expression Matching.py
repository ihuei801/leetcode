###
# DP
# Time Complexity: O(m*n)
# Space Complexity: O(m*n)
###

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False] * (len(p) + 1) for _ in xrange(len(s) + 1)]
        dp[0][0] = True
        for i in xrange(len(s) + 1):
            for j in xrange(1, len(p) + 1):
                if p[j-1] == '*':
                    dp[i][j] = dp[i][j-2] or (i > 0 and dp[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == '.'))
                else:
                    dp[i][j] = i > 0 and dp[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '.')
        return dp[len(s)][len(p)]