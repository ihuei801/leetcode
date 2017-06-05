###
# DFS
# Time Complexity: O(2^n)
# Space Complexity: O(n)
###
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        re = []
        self.dfs(nums, 0, [], re)
        return re
    def dfs(self, nums, idx, one_sol, re):
        re.append(one_sol)
        for i in xrange(idx, len(nums)):
            self.dfs(nums, i+1, one_sol + [nums[i]], re)
        
        