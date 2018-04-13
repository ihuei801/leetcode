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
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for l in xrange(1, len(s) + 1):
            for i in xrange(l):
                if dp[i] and s[i:l] in wordDict:
                    dp[l] = True
                    break
        return dp[len(s)]