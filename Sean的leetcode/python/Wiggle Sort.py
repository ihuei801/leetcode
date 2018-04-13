###
# Array
# Time Complexity: O(n)
# Space Complexity: O(1)
###
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        for i in xrange(len(nums) - 1):
            if (i & 1 == 0 and nums[i] > nums[i+1]) or (i & 1==1 and nums[i] < nums[i+1]):
                nums[i], nums[i+1] = nums[i+1], nums[i]
        
        
        