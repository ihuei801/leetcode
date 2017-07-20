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
        re = [[]]
        self.dfs(nums, 0, [], re)
        return re
    
    def dfs(self, nums, idx, cur, re):
        for i in xrange(idx, len(nums)):
            re.append(cur + [nums[i]])
            self.dfs(nums, i + 1, cur + [nums[i]], re)
            
        