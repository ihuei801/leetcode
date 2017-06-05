//Sliding Window
//O(n)
class Solution {
public:
    int lengthOfLongestSubstringKDistinct(string s, int k) {
        int n = s.size();
        if (n == 0 || k == 0) return 0;
        vector<int> cnt(256);
        int distinct = 0;
        int l = 0;
        int r = 0;
        int max_len = 0;
       
        for (; r < n; r++) {
            if (cnt[s[r]] == 0) {
                distinct++;
            }
            cnt[s[r]]++;
            while (distinct > k) {
                cnt[s[l]]--;
                if (cnt[s[l]] == 0) {
                    distinct--;
                }
                l++;
            }
            max_len = max(max_len, r - l + 1);
        }
        return max_len;
    }
};

class Solution {
public:
    int lengthOfLongestSubstringKDistinct(string s, int k) {
        int l = 0;
        int r = 0;
        int maxlen = 0;
        int dist = 0;
        vector<int> cnt(256, 0);
        while (r < s.size()) {
            if (cnt[s[r]]++ == 0) {
                dist++;
            }
            while (dist > k) {
                if(--cnt[s[l++]] == 0) {
                    dist--;
                }
            }
            maxlen = max(maxlen, r - l + 1);
            r++;
        }
        return maxlen;
        
    }
};