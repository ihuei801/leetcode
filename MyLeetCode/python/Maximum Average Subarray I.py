###
# Sliding Window - fixed size
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
        l = 0
        for r, e in enumerate(nums):
            cursum += e
            if r >= k-1:
                maxsum = max(maxsum, cursum)
                cursum -= nums[l]
                l += 1
        return float(maxsum) / k
            
                
                                        
                            
                    