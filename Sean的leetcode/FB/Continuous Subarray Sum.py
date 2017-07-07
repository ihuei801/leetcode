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
        d = dict({0:-1})
        accu = 0
        for idx, num in enumerate(nums):
            accu += num
            if k != 0:
                accu %= k
            if accu in d:
                if idx - d[accu] >= 2:
                    return True
            else:
                d[accu] = idx
        return False