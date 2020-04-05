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
        if len(nums) <= 1:
            return len(nums)
        p = 0
        for i, e in enumerate(nums):
            if nums[i] > nums[p]:
                p += 1
                nums[p] = nums[i]
        return p + 1