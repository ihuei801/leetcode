//refer http://blog.unieagle.net/2012/12/04/leetcode%E9%A2%98%E7%9B%AE%EF%BC%9Abest-time-to-buy-and-sell-stock-ii/
class Solution {
public:
    int maxProfit(vector<int> &prices) {
        int sum = 0;
        for (int i = 1; i < prices.size(); i++)
        {
            if (prices[i] - prices[i-1] > 0)
            {
                sum += prices[i] - prices[i-1];
            }
        }
        return sum;
    }
};