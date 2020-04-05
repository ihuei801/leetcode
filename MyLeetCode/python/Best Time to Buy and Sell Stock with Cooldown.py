###
# DP
# Time Complexity: O(n) 
# Space Complexity: O(1)
# State:
# buy[i] first i transaction sequence ending with Buy
# sell[i] first i transaction sequence ending with Sell or Rest
# Function
# buy[i] = max(sell[i-2]-price, buy[i-1]) 
# sell[i] = max(buy[i-1]+price, sell[i-1]) 
# Initialization:
# buy[0] = -price[0]
# sell[0] = 0
# presell[0] = 0
# Answer:
# sell[n]
###
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        
        presell = 0
        sell = 0
        buy = -prices[0]
        for i in xrange(1, len(prices)):
            tmp = buy
            buy = max(presell - prices[i], buy)
            presell = sell
            sell = max(tmp + prices[i], sell)
        return sell
