###
# DP
# Time Complexity: O(n)
# Space Complexity: O(1)
###
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        m1 = m2 = float('inf')
        for num in nums:
            if num <= m1:
                m1 = num
            elif num <= m2:
                m2 = num
            else:
                return True
        return False
                