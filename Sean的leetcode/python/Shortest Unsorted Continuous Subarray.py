###
# DP
# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/solution/
# Iterate from beginning of array, find the last element which is smaller than the last seen max from 
# its left side and mark it as end
# Iterate from end of array, find the last element which is bigger than the last seen min from 
# its right side and mark it as begin
# Time Complexity: hasNext:  O(n)
# Space Complexity: O(1)
###
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        start = -1
        end = -1
        minv = float('inf')
        maxv = -float('inf')
        for i in xrange(len(nums)):
            maxv = max(maxv, nums[i])
            minv = min(minv, nums[len(nums)-1-i])
            if nums[i] < maxv:
                end = i
            if nums[len(nums)-1-i] > minv:
                start = len(nums)-1-i

        return end - start + 1 if end > start else 0
                            
                    