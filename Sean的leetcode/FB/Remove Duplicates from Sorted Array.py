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
        if not nums:
            return 0
        l = 0
        for i, num in enumerate(nums):
            if i < 1 or num != nums[l-1]:
                nums[l] = num
                l += 1
        return l       
        
        