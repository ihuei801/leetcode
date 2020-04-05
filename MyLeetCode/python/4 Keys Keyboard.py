###
# DP
# We use i steps to reach maxA(i) then use the remaining n - i steps to reach n - i - 1 copies of maxA(i)
# For example:
# A, A, A, Ctrl A, Ctrl C, Ctrl V, Ctrl V
# Here we have n = 7 and we used i = 3 steps to reach AAA
# Then we use the remaining n - i = 4 steps: 
# Ctrl A, Ctrl C, Ctrl V, Ctrl V, to reach n - i - 1 = 3 copies of AAA
# We either don't make copies at all, in which case the answer is just n, 
# or if we want to make copies, we need to have 3 steps reserved for Ctrl A, Ctrl C, Ctrl V
# so i can be at most n - 3
# State: dp[i] max number of A for i numbers of keys
# Formula: dp[i] = max(i, dp[j]*(i-j-1)) for j from 1 to i-3
# Initialization: dp[i] = i
# Answer: dp[n] 
# Time Complexity: O(n^2)
# Space Complexity: O(n)
###
class Solution(object):
    def maxA(self, N):
        """
        :type N: int
        :rtype: int
        """
        dp = range(N+1)
        for i in xrange(1, N+1):
            for j in xrange(1, i-2):
                dp[i] = max(dp[i], dp[j] * (i-j-1))
        return dp[N]
# Reference                                     
# Java soln
# Time Complexity: O(n)
# Space Complexity: O(1)                            
public int maxA(int N) {
    int[] dp = new int[7];
        
    for (int i = 1; i <= N; i++) {
        dp[0] = i;
            
        for (int k = 6; k > 2; k--) {
            dp[0] = Math.max(dp[0], dp[k] * (k - 1));
        }
            
        for (int k = 6; k > 0; k--) {
            dp[k] = dp[k - 1];
        }
    }
        
    return dp[0];
}                  