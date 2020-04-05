###
# DP
# Time Complexity: O(k*n^2)
# Space Complexity: O(n*k)
# State: dp[i][k]: The max average for the first i elements with at most k partitions
# Function: dp[i][k] = dp[j][k-1] + average(j, i) for all j < i
# Initialization: dp[i][1] = average(0, i) 
# Answer: dp[n][k]
###
# Method 1: Top down
class Solution(object):
    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        if K == 0 or not A:
            return 0
        accu = [0] * (len(A) + 1)
        dp =[[0] * (K+1) for i in xrange(len(A)+1) ]
        for i, n in enumerate(A):
            accu[i+1] = accu[i] + n
            dp[i+1][1] = accu[i+1] / float(i+1)
        def avg(i, j):
            return (accu[j] - accu[i]) / float(j - i)
        for k in xrange(2, K+1):
            for i in xrange(2, len(A)+1):
                maxv = -float('inf')
                for j in xrange(1, i):
                    maxv = max(maxv, avg(j, i) + dp[j][k-1])
                dp[i][k] = maxv
        return dp[len(A)][K]
        
#Method 2: Buttom up
class Solution(object):
    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        self.memo = {}
        accu = [0]
        for n in A:
            accu.append(accu[-1] + n)
        return self.dp(accu, len(A), K)
    
    def dp(self, accu, n, k):
        if (n, k) in self.memo:
            return self.memo[n, k]
        if n < k:
            return 0
        ans = -float('inf')
        if k == 1:
            ans = accu[n] / float(n)
        for i in xrange(1, n):
            ans = max(ans, self.dp(accu, i, k-1) + self.avg(accu, i, n))
        self.memo[n, k] = ans
        return ans
    
    def avg(self, accu, i, j):
        return (accu[j] - accu[i]) / float(j - i)
            

                    