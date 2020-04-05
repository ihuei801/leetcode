class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> appear(nums.begin(), nums.end());
        int maxlen = 0;
        for (int n : nums) {
            if (!appear.count(n)) continue;
            appear.erase(n);
            int r = n + 1;
            int l = n - 1;
            while (appear.count(r)) {
                appear.erase(r++);
            }
            while (appear.count(l)) {
                appear.erase(l--);
            }
            maxlen = max(maxlen, r - l - 1);
        }
        return maxlen;
    }
};
//Sean's solution
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> s(nums.begin(), nums.end());
        int max_len = 0;
        for (auto i : nums)
        {
            if (!s.count(i)) continue;

            s.erase(i);
            int j = i-1, k = i+1;
            while (s.count(j)) s.erase(j--);
            while (s.count(k)) s.erase(k++);
            max_len = max(max_len, k-j-1);
        }
        return max_len;
    }
};