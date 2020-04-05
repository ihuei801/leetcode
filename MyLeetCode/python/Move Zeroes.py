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
        if len(nums) <= 1:
            return
        l = 0
        i = 0
        while i < len(nums):
            if nums[i] != 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
            i += 1
          
            
 