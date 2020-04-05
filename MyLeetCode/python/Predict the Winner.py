###
# DP
# Time Complexit: O(n^2)
# Space Complexity: O(n^2) -> O(n)
# State: dp[i][j]: how much more scores that the first-in-action player will get from i to j than the second player
# Function: dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
# Initialization: dp[i][i] = nums[i]
# Answer: dp[0][n-1] >= 0
###
class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        dp = [0] * n 
        for i in xrange(n-1, -1, -1):
            for j in xrange(i, n):
                if i == j:
                    dp[j] = nums[j]
                else:
                    dp[j] = max(nums[i] - dp[j], nums[j] - dp[j-1])
        return dp[n-1] >= 0

class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        dp = [[0] * n for i in xrange(n)]
        for i in xrange(n):
            dp[i][i] = nums[i]
        for l in xrange(1, n):
            for i in xrange(n-l):
                j = i + l
                dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])
        return dp[0][n-1] >= 0
#memoize
class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        memo = [[None] * n for i in xrange(n)]
        return self.dfs(nums, 0, n-1, memo) >= 0
    def dfs(self, nums, i, j, memo):
        if i == j:
            return nums[i]
        if memo[i][j] != None:
            return memo[i][j]
        memo[i][j] = max(nums[i] - self.dfs(nums, i+1, j, memo), nums[j] - self.dfs(nums, i, j-1, memo))
        return memo[i][j]
            