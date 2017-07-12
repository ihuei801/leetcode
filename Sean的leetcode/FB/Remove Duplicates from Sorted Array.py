###
# Time Complexit: O(n)
# Space Complexity: O(1)
###
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        l = i = 1
        while i < len(nums):
            if nums[i] != nums[l-1]:
                nums[l] = nums[i]
                l += 1
            i += 1
        return l
        
        