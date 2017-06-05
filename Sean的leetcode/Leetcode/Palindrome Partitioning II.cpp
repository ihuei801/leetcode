//1. refer to http://fisherlei.blogspot.tw/2013/03/leetcode-palindrome-partitioning-ii.html
//2. use recursive solution results in time limit exceeding.
//Time Complexity: O(n^2)
class Solution {
public:
    int minCut(string s) {
        int size = s.size();
        vector<int> cut(size, 0);
        vector<vector<bool>> isPalindrome(size, vector<bool>(size, false));
        //min number of cut from s[0....i]
        for (int i = 0; i < size; i++) {
            cut[i] = i;
        }
        
        for (int i = 0; i < size; i++) {
            for (int j = i; j >= 0; j--) {
                if (s[i] == s[j] && (i-j <= 2 || isPalindrome[j+1][i-1])) {
                    isPalindrome[j][i] = true;
                    if (j > 0) {
                        cut[i] = min(cut[i], cut[j-1] + 1);
                    } else {
                        cut[i] = 0;
                    }
                }
            }
        }
        return cut[size - 1];
    }
};


//Sean
class Solution {
public:
    int minCut(string s) {
        int len = s.size();
        //m_cut[i]: the minimum cut between s[i] to s[len-1]
        vector<int> m_cut(len+1, 0);
        vector<vector<bool>> p (len, vector<bool>(len, false));

        for (int i = 0; i <= len; i++)
            m_cut[i] = len - i - 1;

        for (int i = len-1; i >= 0; i--)
            for (int j = i; j < len; j++)
            {
                if (s[i] == s[j] && (j - i <= 2 || p[i+1][j-1]))
                {
                    p[i][j] = true;
                    m_cut[i] = min(m_cut[i], m_cut[j+1]+1);
                }
            }
        return m_cut[0];
    }
};