//https://leetcode.com/discuss/56983/simple-java-dp-solution
//DP solution: dp[i] the min number of sqaures whose total sum is i.
//Time: O(n*sqrt(n)), Space: O(n)
class Solution {
public:
    int numSquares(int n) {
        vector<int> dp(n+1, INT_MAX);
        //note: dp[0] is 0 because starting from 1.
        dp[0] = 0;
        for (int i = 1; i <= n; i++)
            for (int j = 1; j*j <= i; j++)
                dp[i] = min(dp[i], dp[i-j*j]+1);

        return dp[n];
    }
};