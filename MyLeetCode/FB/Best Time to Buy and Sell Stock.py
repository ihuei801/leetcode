###
# DP
# Time Complexity: O(n)
# Space Complexity: O(1)
###
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        min_p = float('inf')
        max_pro = 0
        for p in prices:
            min_p = min(p, min_p) 
            max_pro = max(p - min_p, max_pro)
        return max_pro
        