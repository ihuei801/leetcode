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
        n = len(nums)
        l, r = 0, n-1
        while l + 1 < r:
            mid = (l + r) / 2
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid
            if nums[mid] > nums[mid+1]:
                r = mid
            else:
                l = mid
        return l if nums[l] > nums[r] else r 
        
        