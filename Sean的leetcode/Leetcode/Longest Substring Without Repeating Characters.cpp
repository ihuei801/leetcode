//https://leetcode.com/discuss/23883/11-line-simple-java-solution-o-n-with-explanation
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int max_len = 0;
        int left, right;
        int n = s.size();
        unordered_map<char, int> c_map;

        for (left = right = 0; right < n; right++)
        {
            char c = s[right];
            if (c_map.count(c))
                left = max(left, c_map[c] + 1);
            c_map[c] = right;
            max_len = max(max_len, right - left + 1);
        }
        return max_len;
    }
};