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
        if len(nums) < 3:
            return False
        m1 = m2 = float('inf')
        for n in nums:
            if n <= m1:
                m1 = n # m1 : min seen so far
            elif n <= m2:
                m2 = n # x is better than current m2, store it
            else:
                return True
        return False