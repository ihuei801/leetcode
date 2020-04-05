###
# DP
# Time Complexity: O(m*n)
# Space Complexity: O(n)
# State: dp[i][j] maxsubsequence len with first i chars in word1 and first j chars in word2 -> dp[j]: maxsubsequence len in first j chars in word2
# Function: dp[i][j] = dp[i-1][j-1] + 1 if word1[i-1] == word2[j-1] -> dp[j] = pre[j-1] + 1
#                    = max(dp[i-1][j], dp[i][j-1]) if word1[i-1] != word2[j-1] -> dp[j] = max(pre[j], dp[j-1])
# Initialization: dp[0][0] = 0
# Answer: m + n - 2*dp[m][n]
###
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if len(word2) > len(word1):
            return self.minDistance(word2, word1)
        m = len(word1)
        n = len(word2)
        dp = [0] * (n+1)
        for i in xrange(1, m+1):
            tmp = [0] * (n+1)
            for j in xrange(1, n+1):
                if word1[i-1] == word2[j-1]:
                    tmp[j] = dp[j-1] + 1
                else:
                    tmp[j] = max(dp[j], tmp[j-1])
            dp = tmp
        return m + n - 2 * dp[n]

                                        
                            
                    