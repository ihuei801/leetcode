###
# Reservoir Sampling
# Time Complexity: O(n)
# Space Complexity: O(1)
###
import random
class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums
        

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        idx = -1
        cnt = 0
        for i, num in enumerate(self.nums):
            if num != target:
                continue
            rm = random.randint(0, cnt)
            if rm == 0:
                idx = i
            cnt += 1
        return idx
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)