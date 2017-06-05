/*
Time Complexity:O(n)
*/
class Solution {
public:
    bool canPermutePalindrome(string s) {
        vector<int> cnt(256,0);
        int n = s.size();
        if (n == 0) return true;
        int oddcnt = 0;
        for (char c: s) {
            cnt[c]++;
            if (cnt[c] & 1) {
                oddcnt++;
            }
            else {
                oddcnt--;
            }
        }
        
        return oddcnt <= 1;
    }
};
//Sean's solution
class Solution {
public:
    bool canPermutePalindrome(string s) {
        unordered_map<char, int> c_map;
        int odd = 0;
        for (auto c : s)
        {
            c_map[c]++;
            if (c_map[c] & 1)
                odd++;
            else
                odd--;
        }
        return odd <= 1;
    }
};