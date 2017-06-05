//http://collabedit.com/egxb6
//https://leetcode.com/discuss/43860/9-lines-16ms-c-dp-solutions-with-explanations
//DP solution, O(MN) time
class Solution {
public:
    bool isMatch(string s, string p) {
        int m = s.size();
        int n = p.size();
        //dp[i][j] : true: s of length i matches p of length of j.
        vector<vector<bool>> dp(m+1, vector<bool>(n+1, false));

        dp[0][0] = true;
        for (int i = 0; i <= m; i++)
            for (int j = 1; j <= n; j++)
            {
                if (p[j-1] == '*')
                    //not match '*' or match '*'
                    dp[i][j] = dp[i][j-2] || (i > 0 && (s[i-1] == p[j-2] || p[j-2] == '.') && dp[i-1][j]);
                else
                    dp[i][j] = (i > 0) && (s[i-1] == p[j-1] || p[j-1] == '.') && dp[i-1][j-1];
            }
        return dp[m][n];
    }
};
#if 1 //recursive solution
/*

1. current math
    a. the next is '*':  skip '*' or match '*'
    b. the next is not '*'
2. current not match
    c. the next is '*': skip '*'
    d. the next is not '*'

*/
class Solution {
public:
    bool match(const char *s, const char *p)
    {
        while (*s)
        {
            if (*s == *p || *p == '.')
            {
                if (*(p+1) == '*')
                {
                    if (match(s, p+2))
                        return true;
                    s++;
                }
                else
                {
                    s++;
                    p++;
                }
            }
            else
            {
                if (*(p+1) == '*')
                    p += 2;
                else
                    return false;
            }
        }
        while (*p && *(p+1) == '*')
            p += 2;
        return *p == 0;
    }
    bool isMatch(string s, string p) {
        return match(s.c_str(), p.c_str());
    }
};
#elif 1

#endif