###
# HashTable
# Time Complexity: O(n)
# Space Complexity: O(n)
###
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) < 2:
            return []
        d = {}
        for i, num in enumerate(nums):
            if target - num in d:
                return [d[target-num], i]
            d[num] = i
        return []
                