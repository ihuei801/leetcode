###
# DP
# Time Complexity: O(2^n)
# Space Complexity: O(2^n)
###
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        dp = {0:1}
        for num in nums:
            new_dp = collections.defaultdict(int)
            for s, c in dp.iteritems():
                new_dp[s + num] += c
                new_dp[s - num] += c
                
            dp = new_dp
        
        
        return dp[S]
   