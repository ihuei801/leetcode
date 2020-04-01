###
# Time Complexity: O(nlogn+n^2)
# Space Complexity: O(n) for sorting
###
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return -1
        mindis = float('inf')
        result = None
        nums.sort()

        for i in xrange(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == target:
                    return s
                elif s < target:
                    if abs(s - target) < mindis:
                        mindis = abs(s - target)
                        result = s
                    l += 1
                else:
                    if abs(s - target) < mindis:
                        mindis = abs(s - target)
                        result = s
                    r -= 1
        return result