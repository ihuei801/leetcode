### 
# Time Complexity: O(n)
# Space Complexity: O(1)
###
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        re = [1] * len(nums)
        lp = 1
        rp = 1
        for i in xrange(len(nums)):
            re[i] *= lp
            re[len(nums)-1-i] *= rp
            lp *= nums[i]
            rp *= nums[len(nums)-1-i]
            
        return re
        