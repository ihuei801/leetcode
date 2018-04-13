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
        max_profit = 0
        cur_min = float('inf')
        for p in prices:
            cur_min = min(cur_min, p)
            max_profit = max(p-cur_min, max_profit)
        return max_profit