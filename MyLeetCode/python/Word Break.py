###
# DP
# Time Complexit: O(n^2)
# Space Complexity: O(n)
# State: dp[i] whether the first i characters can be broken
# Function: dp[i] = dp[j] == True and s[j:i] in dict
# Initialization: dp[0] = True
# Answer: dp[n]
###
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s or not wordDict:
            return False
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        for i in xrange(1, n+1):
            for j in xrange(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[n]