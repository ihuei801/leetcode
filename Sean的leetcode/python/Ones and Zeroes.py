###
# DP
# Method 2:
# State: dp[k][i][j] maximum number of strings from the first k strs using i '0's and j '1's.
# Formula: dp[k][i][j] = max(dp[k-1][i-numOfZero(strs[k-1])][i-numOfOnes(strs[k-1])] and dp[k-1][i][j])
# Initializaton: dp[0][i][j] = 0
# Answer: dp[l][m][n]
# Method 1:
# Rolling dp to reduce space to 2D:
# dp[i][j] = the max number of strings that can be formed with i 0's and j 1's
# from the first few strings up to the current string s
# Catch: have to go from bottom right to top left
# Why? If a cell in the dp is updated(because s is selected),
# we should be adding 1 to dp[i][j] from the previous iteration (when we were not considering s)
# If we go from top left to bottom right, we would be using results from this iteration => overcounting
# Time Complexity: O(lmn)
# Space Complexity: O(mn)
###
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        if not strs or (not m and not n):
            return 0
        l = len(strs)
        dp = [[0] * (n+1) for i in xrange(m+1)]
        for k in xrange(1, l+1):
            zeros, ones = self.count(strs[k-1])
            tmp = [[0] * (n+1) for i in xrange(m+1)]
            for i in xrange(m+1):
                for j in xrange(n+1):
                    if i >= zeros and j >= ones:
                        tmp[i][j] = max(dp[i][j], 1+dp[i-zeros][j-ones])
                    else:
                        tmp[i][j] = dp[i][j]
            dp = tmp
        return dp[m][n]
    
    def count(self, s):
        return sum(1 for c in s if c == '0'), sum(1 for c in s if c == '1')
        
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n+1) for i in xrange(m+1)]
        def count(s):
            return sum(1 for c in s if c == '0'), sum(1 for c in s if c == '1')
        for s in strs:
            z, o = count(s)
            for zeros in xrange(m, z-1, -1):
                for ones in xrange(n, o-1, -1):
                    dp[zeros][ones] = max(1 + dp[zeros - z][ones - o], dp[zeros][ones])
        return dp[m][n]
#Space Complexity: O(lmn)
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        if not strs or (not m and not n):
            return 0
        l = len(strs)
        dp = [[[0] * (n+1) for i in xrange(m+1)] for k in xrange(l+1)]
        for k in xrange(1, l+1):
            zeros, ones = self.count(strs[k-1])
            for i in xrange(m+1):
                for j in xrange(n+1):
                    if i >= zeros and j >= ones:
                        dp[k][i][j] = max(dp[k-1][i][j], 1+dp[k-1][i-zeros][j-ones])
                    else:
                        dp[k][i][j] = dp[k-1][i][j]
        return dp[l][m][n]
    
    def count(self, s):
        return sum(1 for c in s if c == '0'), sum(1 for c in s if c == '1')
           
                                        
#Memoize TLE                           
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        self.memo = {}
        return self.search(strs, len(strs), m, n)
    def search(self, strs, k, m, n):
        if (k, m, n) in self.memo:
            return self.memo[k, m, n]
        if k == 0:
            return 0
        def count(s):
            return sum(1 for c in s if c == '0'), sum(1 for c in s if c == '1')
        z, o = count(strs[k-1])
        maxcnt = 0
        if m - z >= 0 and n - o >= 0:
            maxcnt = max(maxcnt, self.search(strs, k-1, m-z, n-o) + 1)
        maxcnt = max(maxcnt, self.search(strs, k-1, m, n))
        self.memo[k, m, n] = maxcnt
        return maxcnt
            