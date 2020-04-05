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
                    dp[i][j] = dp[i][j-1] || (i > 0 && dp[i-1][j]);
                else
                    dp[i][j] = (i > 0) && (s[i-1] == p[j-1] || p[j-1] == '?') && dp[i-1][j-1];
            }
        return dp[m][n];
    }
};
#endif
v#if 1//recursive solution
//http://fisherlei.blogspot.com/2013/01/leetcode-wildcard-matching.html
class Solution {
public:
    bool isMatch(string s, string p) {
        const char *str = s.c_str();
        const char *ptr = p.c_str();
        const char *p_ptr, *s_ptr;

        int star = 0;

        while (*str)
        {
            if (*str == *ptr || *ptr == '?')
            {
                str++;
                ptr++;
            }
            else if (*ptr == '*')
            {
                s_ptr = str;
                while (*ptr == '*')
                    ptr++;

                if (*ptr == 0) return true;

                p_ptr = ptr;
                star = 1;
            }
            else
            {
                if (star)
                {
                    ptr = p_ptr;
                    str = s_ptr;
                    s_ptr++;
                }
                else
                    return false;
            }
        }

        while (*ptr == '*')
            ptr++;

        return *str == 0 && *ptr == 0;
    }
};
#elif 1
//http://collabedit.com/egxb6
