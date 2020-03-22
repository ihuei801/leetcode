###
# Array sliding window
# Time Complexity: O(n)
# Space Complexity: O(1)
###
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if k == 0:
            return -1
        cursum = 0
        maxsum = -float('inf')
        for i, e in enumerate(nums):
            if i >= k:
                cursum -= nums[i-k]
            cursum += e
            if i >= k-1:
                maxsum = max(maxsum, cursum)
        return float(maxsum) / k
            
                
                                        
                            
                    