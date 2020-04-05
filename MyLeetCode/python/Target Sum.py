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
        if not nums:
            return 0
        dp = {0:1}
        for n in nums:
            dp_next = collections.defaultdict(int)
            for k, v in dp.iteritems():
                dp_next[k + n] += v
                dp_next[k - n] += v
            dp = dp_next
        return dp[S]
                
        