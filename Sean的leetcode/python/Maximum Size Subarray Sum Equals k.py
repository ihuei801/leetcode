###
# Time Complexity: O(n)
# Space Complexity: O(n)
##
class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0
        d = {0 : -1}
        accu = 0
        max_len = 0
        for i, num in enumerate(nums):
            accu += num
            if accu - k in d:
                max_len = max(max_len, i - d[accu - k])
            if accu not in d:       
                d[accu] = i
        return max_len
        
            