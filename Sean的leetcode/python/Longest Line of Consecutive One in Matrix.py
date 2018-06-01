###
# DP
# State:
# dp[i][j][0]: longest consecutive ones from left
# dp[i][j][1]: longest consecutive ones from up          -> reduce to 2D
# dp[i][j][2]: longest consecutive ones from diag
# dp[i][j][3]: longest consecutive ones from anti-diag
# Functions: 
# if M[i][j] == 1:
# dp[i][j][0] = dp[i][j-1][0] + 1
# dp[i][j][1] = dp[i-1][j][1] + 1        -> reduce to 2D
# dp[i][j][2] = dp[i-1][j-1][2] + 1
# dp[i][j][3] = dp[i-1][j+1][3] + 1
# else:
# dp[i][j][0] = dp[i][j][1] = dp[i][j][2] = dp[i][j][3] = 0
# Initialize:
# i == 0: same as M[i][j] 
# Answer: max(dp[i][j])
# Time Complexity: O(mn)
# Space Complexity: O(n)
###
class Solution(object):
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M or not M[0]:
            return 0
        rows = len(M)
        cols = len(M[0])
    
        dp = [[0] * 4 for _ in xrange(cols)]
        maxlen = 0
        for i in xrange(rows):
            tmp = [[0] * 4 for _ in xrange(cols)]
            for j in xrange(cols):
                if M[i][j] == 1:
                    tmp[j][0] = tmp[j-1][0] + 1 if j > 0 else 1
                    tmp[j][1] = dp[j][1] + 1
                    tmp[j][2] = dp[j-1][2] + 1 if j > 0 else 1
                    tmp[j][3] = dp[j+1][3] + 1 if j < cols-1 else 1
                else:
                    tmp[j][0] = tmp[j][1] = tmp[j][2] = tmp[j][3] = 0
                maxlen = max(maxlen, max(tmp[j]))
            dp = tmp
        return maxlen
                                        
                            
                    