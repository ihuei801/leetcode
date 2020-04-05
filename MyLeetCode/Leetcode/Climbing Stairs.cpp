//Dynamic programming: f(n) = f(n-1) with 1-step + f(n-2) with 2-step,  n>2;
class Solution {
public:
    int climbStairs(int n) {
        if (n <= 1) return n;
        int fn_2 = 1;
        int fn_1 = 1;
        int fn;
        for (int i = 2; i <= n; i++)
        {
            fn = fn_1 + fn_2;
            fn_2 = fn_1;
            fn_1 = fn;
        }
        return fn;
    }
};