//DP
//buy[i] : max profit that can be made by the sequence ending with buy before i (included)
//sell[i] : max profit that can be made by the sequence ending with sell before i (included)
//buy[i] = max(sell[i-2] - price[i], buy[i-1])
//sell[i] = max(buy[i-1] + price[i], sell[i-1])
//reduce to keep track of only two elements
//https://discuss.leetcode.com/topic/30421/share-my-thinking-process
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        if (n <= 1) return 0;
        int buy = INT_MIN;
        int presell = 0;
        int sell = 0;
        for (int i = 0; i < n; i++) {
            int tmp = buy;
            buy = max(presell - prices[i], buy);
            presell = sell;
            sell = max(tmp + prices[i], sell);
        }
        return sell;
        
    }
};