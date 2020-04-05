###
# DP
# Time Complexity: O(n^3)
# Space Complexity: O(n^2)
# State: dp[l][r] max coins for left, right boundary at l and r (could not burst l and r)
# Function: dp[l][r] = max(nums[l] * nums[r] * nums[k] + dp[l][k] + dp[k][r])
# Initialization: dp[i][i] = dp[i][i+1] = 0
# Answer: dp[0][len(nums)-1]
###
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums = [1] + nums + [1]
        dp = [[0] * len(nums) for i in xrange(len(nums))]
        for r in xrange(2, len(nums)):
            for l in xrange(r-1, -1, -1):
                for k in xrange(l+1, r):
                    dp[l][r] = max(dp[l][r], nums[l] * nums[r] * nums[k] + dp[l][k] + dp[k][r])
        return dp[0][len(nums)-1]
                    
                    
                    
        