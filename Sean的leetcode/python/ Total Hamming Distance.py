###
# Time Complexity: O(n)
# Space Complexity: O(1)
###
class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        tot = 0
        l = len(nums)
        for i in xrange(32):
            cnt = 0
            for n in nums:
                cnt += (n >> i & 1)
            tot += cnt * (l-cnt)
        return tot