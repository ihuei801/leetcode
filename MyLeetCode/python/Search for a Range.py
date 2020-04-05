###
# Binary Search
# Time Complexity: O(logn)
# Space Complexity: O(1)
###
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        n = len(nums)
        l, r = 0, n-1
        while l + 1 < r:
            mid = (l + r) / 2
            print target, mid, nums[mid]
            if target <= nums[mid]:
                r = mid
            else:
                l = mid
        left = -1
        if nums[l] == target:
            left = l
        elif nums[r] == target:
            left = r
        l, r = 0, n-1
        while l + 1 < r:
            mid = (l + r) / 2
            if target >= nums[mid]:
                l = mid
            else:
                r = mid
        right = -1
        if nums[r] == target:
            right = r
        elif nums[l] == target:
            right = l
        return [left, right]
                                        
                            
                    