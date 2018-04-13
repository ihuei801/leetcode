###
# DP
# Time Complexity: O(n*sqrt(n)) 
# Space Complexity: O(n)
###
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        for i in xrange(1, n+1):
            j = 1     
            while j * j <= i:
                dp[i] = min(dp[i], dp[i-j*j] + 1)
                j += 1           
        return dp[n]               
        
        