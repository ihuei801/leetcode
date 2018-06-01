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
        summ = 0  
        res = -float('inf')
        for i in xrange(len(nums)):
            if i >= k:
                summ -= nums[i-k]
            summ += nums[i]
            if i >= k-1:
                res = max(res,summ)  
        return float(res)/k;
            
                
                                        
                            
                    