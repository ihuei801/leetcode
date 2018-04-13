###
# Binary Search
# Time Complexity: O(logn)
# Space Complexity: O(1)
###
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        l = 0
        r = len(nums) - 1
        while l + 1 < r:
            mid = (l + r) / 2
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid
            elif nums[mid] > nums[mid+1]:
                r = mid
            else:
                l = mid
        if nums[l] < nums[r]:
            return r
        else:
            return l
        
        