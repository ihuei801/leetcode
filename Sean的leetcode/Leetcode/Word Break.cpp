//refer http://fisherlei.blogspot.tw/2013/11/leetcode-word-break-solution.html
//Time complexity:O(n^2)
class Solution {
public:
    bool wordBreak(string s, unordered_set<string>& wordDict) {
        int n = s.size();
        if (n == 0) return false;
        vector<bool> dp(n+1, false);

        dp[0] = true;
        //dp[i] is true means s.substr(0, i) (length is i) is a valid word Break.
        for (int i = 1; i <= n; i++)
            for (int j = 0; j < i; j++)
            {
                if (dp[j] && wordDict.count(s.substr(j, i-j))) {
                    dp[i] = true;
                    break;
                }
            }
        return dp[n];
    }
};