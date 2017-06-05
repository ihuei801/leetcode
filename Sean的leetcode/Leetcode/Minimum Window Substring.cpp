// Time Complexity:O(n)
class Solution {
public:
    string minWindow(string s, string t) {
        if (s.empty() || t.empty()) return "";
        int r = 0;
        int cnt = 0;
        int l = 0;
        int n = s.size();
        int required[256] = {0};
        int minlen = INT_MAX;
        int minst = 0;
        
        for (char c : t){
            required[c]++;
        }
        
        while (r < n) {
            required[s[r]]--;
            if (required[s[r]] >= 0) {
                cnt++;
            }
            while (cnt == t.size()) {
                int len = r - l + 1;
                if (len < minlen) {
                    minlen = len;
                    minst = l;
                }
                required[s[l]]++;
                if (required[s[l]] > 0) {
                    cnt--;
                }
                l++;
            }
            r++;
        }
        return minlen == INT_MAX? "" : s.substr(minst, minlen);
    }
};
//https://leetcode.com/discuss/20053/three-concise-implemetation-according-leetcode-oj-discuss

//use two pointers (left, right) to find the match region.
//1. advance right index to collect enough char.
//2. advance left index to shrink the (left, right) region.
//3. advance left index and right index to find the next possible solution.
//4. repeat step1-step3
class Solution {
public:
    string minWindow(string s, string t) {
        int left = 0, right = 0;
        unordered_map<char, int>t_map;
        int min_len = INT_MAX;
        int start_idx;
        int count = 0;
        for (auto c : t)
            t_map[c]++;

        while (right < s.size())
        {
            t_map[s[right]]--;

            if (t_map[s[right]] >= 0)
                count++;

            while (count == t.size())
            {
                if (right - left + 1 < min_len)
                {
                    min_len = right - left + 1;
                    start_idx = left;
                }
                t_map[s[left]]++;
                if (t_map[s[left]] > 0)
                    count--;
                left++;
            }
            right++;
        }

        return min_len == INT_MAX ? "" : s.substr(start_idx, min_len);
    }
};