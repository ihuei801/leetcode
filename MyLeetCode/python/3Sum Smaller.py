###
# Two Pointer
# Time Complexity: O(nlogn) + O(n^2)
# Space Complexity: O(1)
###
class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return 0
        nums.sort()
        cnt = 0
        for i in xrange(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < target:
                    cnt += (r-l)
                    l += 1
                else:
                    r -= 1
        return cnt
        
        