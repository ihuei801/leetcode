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
        if not nums:
            return 0
        nums = set(nums)
        maxlen = 0       
        for n in nums:
            if n-1 not in nums:
                nxt = n+1
                while nxt in nums:
                    nxt += 1
                maxlen = max(maxlen, nxt - n)
        return maxlen