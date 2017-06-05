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
        d = {0:-1}
        accu = 0
        maxlen = 0
        for i in xrange(len(nums)):
            accu += nums[i]
            if accu not in d:
                d[accu] = i
            if accu - k in d:
                maxlen = max(maxlen, i - d[accu - k])
        return maxlen
        