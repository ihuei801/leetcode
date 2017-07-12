###
# Time Complexity: O(n)
# Space Complexity: O(n)
##
class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        d = {0 : -1}
        accu = 0
        max_len = 0
        for i, num in enumerate(nums):
            accu += num if num == 1 else -1
            if accu in d:
                max_len = max(max_len, i - d[accu])
            else:
                d[accu] = i
        return max_len
        