###
# DP
# Time Complexity: O(n^2)
# Space Complexity: O(n)
# State: dp[i] longest divisible subset include i
# Function: dp[i] = dp[j] + 1 if nums[i] % nums[j] == 0
# Initialization: dp[i] = 1 parents[i] = i
# Answer: global_max_len, global_max_idx
###
class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        nums.sort()
        dp = [1] * len(nums)
        parents = range(len(nums))
        max_len = 0
        max_idx = 0
        for j, n in enumerate(nums):
            for i in xrange(j):
                if nums[j] % nums[i] == 0 and dp[i] + 1 > dp[j]:
                    dp[j] = dp[i] + 1
                    parents[j] = i
            if dp[j] > max_len:
                max_len = dp[j]
                max_idx = j
        re = []
        for i in xrange(max_len):
            re.append(nums[max_idx])
            max_idx = parents[max_idx]
        return re
                    
                    