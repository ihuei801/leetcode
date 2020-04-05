###
# DP
# Time Complexity: O(nlogn + target*n)
# Space Complexity: O(target)
# State: dp[i] number of ways that can sum to i
# Function: dp[i] += dp[j-num] for num in nums
# Initialization: dp[0] = 1
# Answer: dp[target]
###
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        dp = [0] * (target + 1)
        nums.sort()
        dp[0] = 1
        for i in xrange(1, target + 1):
            for e in nums:
                if e <= i:
                    dp[i] += dp[i-e]
                else:
                    break
        return dp[target]