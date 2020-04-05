class Solution {
public:
    vector<int> cnt;
    string frequencySort(string s) {
        cnt.resize(256);
        int n = s.size();
        if (n <= 1) return s;
        for (char c : s) {
            cnt[c]++;
        }
        sort(s.begin(), s.end(), [&](char a, char b){ return cnt[b] < cnt[a] || (cnt[b] == cnt[a] && b > a); });
        return s;
    }
};