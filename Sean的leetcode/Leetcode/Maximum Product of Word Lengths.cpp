//Time:O(n^2)
class Solution {
public:
    int maxProduct(vector<string>& words) {
        unordered_map<int, int> table;
        int n = words.size();
        if (n == 0) return 0;
        int re = 0;
        for (auto s : words) {
            int mask = 0;
            for (auto c : s) {
                mask |= 1 << (c - 'a');
            }
            table[mask] = max(table[mask], (int)s.size());
            for (auto entry : table) {
                if (! (mask & entry.first)) {
                    re = max(re, entry.second * (int)s.size());
                }
            }
        }
        return re;
    }
}; 