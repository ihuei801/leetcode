###
# Time Complexity: O(n) 
# Space Complexity: O(1)
###
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return len(nums)
        i = l = 2
        while i < len(nums):
            if nums[i] > nums[l-2]:
                nums[l] = nums[i]
                l += 1
            i += 1
        return l