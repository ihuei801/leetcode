###
# Time Complexity: O(n^2)
# Space Complexity: O(1)
###

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ln = len(nums)
        if ln < 3:
            return []
        re = []
        nums.sort()
        i = 0
        while i < ln-2:
            l = i + 1
            r = ln - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    re += [nums[i], nums[l], nums[r]],
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
            i += 1
            while i < ln-2 and nums[i] == nums[i-1]:
                i += 1
        return re