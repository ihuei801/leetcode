#if 1
//https://leetcode.com/discuss/11694/my-dp-solution-in-c
class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        int s1_len = s1.size();
        int s2_len = s2.size();

        //table[i][j] is true means that s3.substr(0, i+j) is interleaving string of s1.substr(0, i) and s2.substr(0, j)
        // i means s1 length is i and j means s2 length is j.
        bool table[s1_len+1][s2_len+1];

        if (s1_len + s2_len != s3.size())
            return false;

        for (int i = 0; i <= s1_len; i++)
            for (int j = 0; j <= s2_len; j++)
            {
                if (i == 0 && j == 0)
                    table[i][j] = true;
                else if (i == 0)
                    table[i][j] = table[i][j-1] && s3[i+j-1] == s2[j-1];
                else if (j == 0)
                    table[i][j] = table[i-1][j] && s3[i+j-1] == s1[i-1];
                else
                    table[i][j] = (table[i-1][j] && s3[i+j-1] == s1[i-1]) || (table[i][j-1] && s3[i+j-1] == s2[j-1]);
            }
        return table[s1_len][s2_len];
    }
};

#else //only use Space: O(n)
class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        int len_s1 = s1.size();
        int len_s2 = s2.size();

        if (len_s1 + len_s2 != s3.size())
            return false;

        bool dp[len_s2+1];

        for (int i = 0; i <= len_s1; i++)
            for (int j = 0; j <= len_s2; j++)
            {
                if (i == 0 && j == 0)
                    dp[j] = true;
                else if (i == 0)
                    dp[j] = dp[j-1] && (s2[j-1] == s3[j-1]);
                else if (j == 0)
                    dp[j] = dp[j] && (s1[i-1] == s3[i-1]);
                else
                    dp[j] = (dp[j] && s1[i-1] == s3[i+j-1]) || (dp[j-1] && s2[j-1] == s3[i+j-1]);
            }
        return dp[len_s2];
    }
};
#endif