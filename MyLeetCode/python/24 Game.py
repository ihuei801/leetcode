###
# Back Tracking
# Time Complexity: O(1)
# Space Complexity: O(1)
###
from operator import truediv, mul, add, sub
class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        n = len(nums)
        if n == 1:
            return abs(nums[0] - 24) < 1e-7
        for i in xrange(n):
            for j in xrange(n):
                if i == j:
                    continue
                nxt = [e for k, e in enumerate(nums) if k != i and k != j]
                for op in (truediv, mul, add, sub):
                        if (op is add or op is mul) and j > i: continue
                        if op is not truediv or nums[j]:    
                            if self.judgePoint24(nxt + [op(nums[i], nums[j])]): return True

        return False
                    
                                        
                            
                    