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
        for i, n in enumerate(nums):
            l = i+1
            r = len(nums) - 1
            while l < r:
                summ = n + nums[l] + nums[r]
                if summ >= target:
                    r -= 1
                else:
                    cnt += r - l 
                    l += 1
        return cnt
        
        