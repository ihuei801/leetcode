###
# Binary Search
# Time Complexity: O(logn)
# Space Complexity: O(1)
###
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        l, r = 0, len(nums)-1
        while l+1 < r:
            mid = (l + r) / 2
            if target == nums[mid]:
                return mid
            if nums[l] < nums[mid]:
                if target >= nums[l] and target <= nums[mid]:
                    r = mid
                else:
                    l = mid
            else:
                if target >= nums[mid] and target <= nums[r]:
                    l = mid
                else:
                    r = mid
        
        if nums[l] == target:
            return l
        elif nums[r] == target:
            return r
        else:
            return -1