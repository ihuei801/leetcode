###
# Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)
###
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        curr = 0
        min_len = float('inf')
        l = r = 0
        while r < len(nums):
            curr += nums[r]
            while curr >= s:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                curr -= nums[l]
                l += 1
            r += 1
        return 0 if min_len == float('inf') else min_len
            