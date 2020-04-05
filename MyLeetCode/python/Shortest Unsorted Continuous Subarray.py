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
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if not nums:
            return
        l_max = -float('inf')
        r_min = float('inf')
        l = r = -1
        for i, e in enumerate(nums):
            j = len(nums)-1-i
            l_max = max(e, l_max)
            r_min = min(nums[j], r_min)
            if e < l_max:
                r = i
            if nums[j] > r_min:
                l = j
        return r - l + 1 if r > l else 0
                            
                    