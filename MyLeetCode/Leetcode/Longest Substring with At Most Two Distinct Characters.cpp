#if 1 //Time: O(N), Space: O(1)
//https://leetcode.com/discuss/31292/clean-11-lines-ac-answer-o-1-space-o-n-time
class Solution {
public:
    int lengthOfLongestSubstringTwoDistinct(string s) {
        int max_len = 0;
        int last_diff = -1;
        int start = 0;
        for (int i = 1; i < s.size(); i++)
        {
            if (s[i] == s[i-1])
                continue;
            if (last_diff != -1 && s[i] != s[last_diff])
            {
                max_len = max(max_len, i - start);
                start = last_diff + 1;
            }
            last_diff = i - 1;
        }
        return max_len  > s.size() - start ? max_len : s.size() - start;
    }
};
#elif 1
class Solution {
public:
    int lengthOfLongestSubstringTwoDistinct(string s) {
        int n = s.size();
        if (n == 0) return 0;
        vector<int> cnt(256);
        int l = 0;
        int r = 0;
        int distinct = 0;
        int max_len = 0;
        for (; r < n; r++) {
            if (cnt[s[r]] == 0) {
                distinct++;
            }
            cnt[s[r]]++;
            while (distinct > 2) {
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
    int lengthOfLongestSubstringTwoDistinct(string s) {
        vector<int> count(256, 0);
        int num = 0;
        int i = 0;
        int len = 0;
        for (int j = 0; j < s.size(); j++){
            if(count[s[j]]++ == 0){
                num++;
            }
            if(num > 2){
                while(--count[s[i++]] > 0);
                num--;
            }
            len = max(len, j - i + 1);
        }
        return len;
    }
};
#elif 2// Time: O(N), Space: O(N)
class Solution {
public:
    int lengthOfLongestSubstringTwoDistinct(string s) {
        unordered_map<char, int> c_map;
        int max_len = 0;
        int left = 0;
        int right;
        int count = 0;
        for (right = 0; right < s.size(); right++)
        {
            if (!c_map.count(s[right]) || !c_map[s[right]])
                count++;

            c_map[s[right]]++;
            while (count > 2)
            {
                c_map[s[left]]--;
                if (c_map[s[left]] == 0)
                    count--;
                left++;
            }
            max_len = max(max_len, right - left + 1);
        }
        return max_len;
    }
};
#endif