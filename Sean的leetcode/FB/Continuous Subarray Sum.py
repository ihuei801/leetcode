###
# Time Complexity: O(n)
# Space Complexity: O(n)
###
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums:
            return False
        d = {0: -1}
        accu = 0
        for i, num in enumerate(nums):
            accu += num
            if k:
                accu %= k
            if accu in d:
                if i - d[accu] >= 2: 
                    return True
            else:
                d[accu] = i
        return False
                