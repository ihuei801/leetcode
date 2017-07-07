###
# Time Complexit: O(n)
# Space Complexity: O(n)
###
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        l = 0
        for num in nums:
            if num-1 not in nums:
                next = num+1
                while next in nums:
                    next += 1
                l = max(l, next-num)
        return l