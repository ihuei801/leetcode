class Solution {
public:
    bool isOneEditDistance(string s, string t) {
        int m = s.size();
        int n = t.size();
        for (int i = 0; i < min(m,n); i++) {
            if (s[i] != t[i]) {
                return s.substr(i + (m < n? 0 : 1)) == t.substr(i + (n < m? 0 : 1));
            }
        }
        return abs(m-n) == 1;
}
};
//https://leetcode.com/discuss/17897/my-c-solution
class Solution {
public:
    bool isOneEditDistance(string s, string t) {
        //let s be the longer one.
        if (s.size() < t.size())
            return isOneEditDistance(t, s);
        int sz = s.size();
        int tz = t.size();
        int len_diff = sz - tz;
        if (len_diff > 1) return false;

        int diff_count = 0;
        int i;
        for (i = 0; i < sz; i++)
        {
            if (s[i] != t[i-len_diff*diff_count])
                diff_count++;
            if (diff_count > 1)
                return false;
        }
        return diff_count == 1;
    }
};