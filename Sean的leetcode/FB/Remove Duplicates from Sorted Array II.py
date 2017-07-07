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
        if not nums:
            return 0
        l = 0
        for i, num in enumerate(nums):
            if i < 2 or num > nums[l-2]:
                nums[l] = num
                l += 1
        return l