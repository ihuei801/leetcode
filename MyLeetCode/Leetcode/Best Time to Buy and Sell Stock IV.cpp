#if 1
class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {
        int num = prices.size();
        int max_profit = 0;
        int count = k << 1;

        if (k == 0) return 0;

        if (count >= num)
        {
            for (int i = 1; i < num; i++)
                max_profit += prices[i] > prices[i-1] ? prices[i] - prices[i-1] : 0;
            return max_profit;
        }

        vector<int> profit(num, INT_MIN);
        vector<int> pre_profit(num, 0);

        //max_profit(K-th transaction on i-th number) is max_profit(K-1 th transaction on i-th number) + K-th transaction.
        /*
                [1, 2, 3]
             -  -1, -1, -1
             +   0,  1, 2
             -  -1, -1, -1
             +   0,  1, 2,
             -  -1, -1, -1
             +   0,  1, 2

        */
        for (int i = 0, op = -1; i < count; i++, op *= -1)
        {
            for (int j = 0; j < num; j++)
            {
                int p = op * prices[j] + pre_profit[j];
                if (j == 0)
                    profit[j] = p;
                else
                    profit[j] = max(profit[j-1], p);
                max_profit = max(max_profit, profit[j]);
            }
            pre_profit = profit;
        }
        return max_profit;
    }
};
#elif 1
//refer EPI p.186, solution 6.4
class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {
        int max_sum = 0;

        if (prices.size() == 0 || k == 0) return 0;

        //k transactions have 2k numbers because each transaction include 2 numbers.
        //So, if 2k is larger than prices.size(), the problem is reduced to k be a unlimited number.
        if (k << 1 >= prices.size())
        {
            for (int i = 1; i < prices.size(); i++)
            {
                if (prices[i] - prices[i-1] > 0)
                    max_sum += prices[i] - prices[i-1];
            }
            return max_sum;
        }

        vector<int> k_sum(k << 1, INT_MIN);
        vector<int> pre_k_sum;

        //iterate each i as the last transaction number.
        for (int i = 0; i < prices.size(); i++)
        {
            pre_k_sum = k_sum;
            //iterate prices[i] at each possible buy/sell to see if better than the previous max value.
            for (int j = 0, sign = -1; j < pre_k_sum.size() && j <= i; j++, sign *= -1)
            {
                int curr_sum = prices[i] * sign + ((j == 0) ? 0 : pre_k_sum[j-1]);
                k_sum[j] = max(k_sum[j], curr_sum);
                max_sum  = max(max_sum, curr_sum);
            }
        }
        return max_sum;
    }
};
#endif