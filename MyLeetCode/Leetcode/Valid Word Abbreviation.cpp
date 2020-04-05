class Solution {
public:
    bool validWordAbbreviation(string word, string abbr) {
        int n = word.size();
        int m = abbr.size();
        int ptr1 = 0;
        int ptr2 = 0;
        while (ptr2 < m && ptr1 < n) {
            if (isdigit(abbr[ptr2])) {
                if (abbr[ptr2] == '0') return false;
                int cnt = 0;
                while (ptr2 < m && isdigit(abbr[ptr2])) {
                    cnt = cnt * 10 + (abbr[ptr2] - '0');
                    ptr2++;
                }
                ptr1 += cnt;
                if (ptr1 > n) return false;
            }
            else {
                if (word[ptr1] != abbr[ptr2]) return false;
                ptr1++;
                ptr2++;
            }
        }
        return ptr1 == n && ptr2 == m;
    }
};