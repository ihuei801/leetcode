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
        l , r = 0, 0
        tmp = 0
        min_len = float('inf')
        while r < len(nums):
            tmp += nums[r]
            while tmp >= s:
                min_len = min(min_len, r - l + 1)
                tmp -= nums[l]
                l += 1
            r += 1
        return min_len if min_len != float('inf') else 0
            