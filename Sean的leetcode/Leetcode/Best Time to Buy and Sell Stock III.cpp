//special case in Best Time to Buy and Sell Stock IV
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int max_sum = 0;
        int num = prices.size();
        if (num <= 4)
        {
            for (int i = 1; i < num; i++)
            {
                if (prices[i] - prices[i-1] > 0)
                    max_sum += prices[i] - prices[i-1];
            }
            return max_sum;
        }

        vector<int>k_sum(4, INT_MIN);
        vector<int>pre_k_sum;

        for (int i = 0; i < num; i++)
        {
            pre_k_sum = k_sum;
            for (int j = 0, sign = -1; j < 4 && j <= i; j++, sign *= -1)
            {
                int sum = sign * prices[i] + (j == 0 ? 0 : pre_k_sum[j-1]);
                max_sum = max(max_sum, sum);
                k_sum[j] = max(k_sum[j], sum);
            }
        }
        return max_sum;
    }
};