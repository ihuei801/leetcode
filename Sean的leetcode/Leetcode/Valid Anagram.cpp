//https://leetcode.com/discuss/49374/2-c-solutions-with-explanations
class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int>table;
        int len = s.size();
        for (int i = 0; i < len; i++)
        {
            if (!table.count(s[i]))
                table[s[i]] = 1;
            else
                table[s[i]]++;
        }

        for (int i = 0; i < t.size(); i++)
        {
            if (table.count(t[i]) && table[t[i]] > 0)
            {
                table[t[i]]--;
                len--;
            }
            else
                return false;
        }
        return len == 0;
    }
};