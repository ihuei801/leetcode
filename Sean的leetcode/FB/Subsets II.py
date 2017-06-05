###
# Time Complexity: O(2^n)
# Space Complexity: O(n)
###
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        re = []
        nums.sort()
        self.dfs(nums, 0, [], re)
        return re
        
    def dfs(self, nums, idx, one_sol, re):
        if one_sol not in re:
            re.append(one_sol)
        for i in xrange(idx, len(nums)):
            if i == idx or nums[i] != nums[i-1]:
                self.dfs(nums, i+1, one_sol + [nums[i]], re)
        