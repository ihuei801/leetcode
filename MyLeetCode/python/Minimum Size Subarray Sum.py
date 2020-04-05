###
# Sliding Window
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
        l = 0
        cursum = 0
        minlen = float('inf')
        for r, e in enumerate(nums):
            cursum += e
            while cursum >= s:
                minlen = min(minlen, r - l + 1)
                cursum -= nums[l]
                l += 1
        return minlen if minlen != float('inf') else 0



