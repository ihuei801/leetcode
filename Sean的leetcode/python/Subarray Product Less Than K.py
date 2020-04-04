###
# Sliding Window - dynamic size
# Time Complexity: O(n)
# Space Complexity: O(1)
###
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1:
            return 0
        prod = 1
        cnt = 0
        l = 0
        for r, n in enumerate(nums):
            prod *= n
            while prod >= k:
                prod /= nums[l]
                l += 1
            cnt += r - l + 1   # count the num of product from l to r: (nums[l] * nums[l+1] * ... * nums[r], nums[l+1] * ... * nums[r], ...)
        return cnt
