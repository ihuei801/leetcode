###
# Swap in python: a, b = b, a
# Time Complexity: O(n)
# Space Complexity: O(1)
###

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        idx = 0
        for i in xrange(len(nums)):
            if nums[i]:
                nums[idx], nums[i] = nums[i], nums[idx]
                idx += 1
                