#if 1
//non-DP solution
//https://leetcode.com/discuss/40559/accepted-4ms-c-solution
//Time: O(n^2)
class Solution {
public:
    string longestPalindrome(string s) {
        int left, right, start;
        int max_len = 0;
        int start_index = 0;

        int len = s.size();

        //each index may be the central position of the palindrome.
        for (start = 0; start < len - (max_len >> 1);)
        {
            left = right = start;

            while (right + 1 < len && s[right] == s[right+1])
                right++;

            //next central position
            start = right + 1;

            while (left - 1 >= 0 && right + 1 < len && s[left-1] == s[right+1])
                left--, right++;

            if (right - left + 1 > max_len)
            {
                max_len = right - left + 1;
                start_index = left;
            }
        }
        return s.substr(start_index, max_len);
    }
};
#else //DP solution
class Solution {
public:
    string longestPalindrome(string s) {

        char table[1000][1000] = {0};
        int max_len = 0;
        int start_index;
        int i, len;

        for (i = 0; i < s.size(); i++)
        {
            table[i][i] = 1;
            max_len = 1;
            start_index = i;
        }

        for (i = 0; i < s.size() - 1; i++)
        {
            if (s[i] == s[i+1])
            {
                table[i][i+1] = 1;
                max_len = 2;
                start_index = i;
            }
        }

        for (len = 3; len <= s.size(); len++)
            for (i = 0; i < s.size() - (len-1); i++)
            {
                if (table[i+1][i+len-2] == 1 && s[i] == s[i+len-1])
                {
                    table[i][i+len-1] = 1;
                    if (len > max_len)
                    {
                        max_len = len;
                        start_index = i;
                    }
                }
            }

        return s.substr(start_index, max_len);
    }
};
#endif