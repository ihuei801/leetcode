###
# DP
# Time Complexity: O(n^3)
# Space Complexity: O(n^2)
# State: dp[i][j]: min cost from i to j
# Function: dp[i][j] = min(pivot + max(dp[i][pivot-1], dp[pivot+1][j]) i<=pivot<=[j]
# Initialization: dp[i][i] = 0 i = 1 to n
# Answer: dp
###
class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 0
        dp = [[0] * (n+1) for i in xrange(n+1)]
        for r in xrange(2, n+1):
            for l in xrange(r-1, -1, -1):
                global_min = float('inf')
                for k in xrange(l, r+1):
                    if k == l:
                        local = l + dp[k+1][r]
                    elif k == r:
                        local = r + dp[l][k-1]
                    else:
                        local = k + max(dp[l][k-1], dp[k+1][r])
                    global_min = min(global_min, local)
                dp[l][r] = global_min
        return dp[1][n]
        
        