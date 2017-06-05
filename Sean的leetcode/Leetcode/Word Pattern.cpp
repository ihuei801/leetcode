//https://leetcode.com/discuss/62476/short-c-read-words-on-the-fly
class Solution {
public:
    bool wordPattern(string pattern, string str) {
        istringstream istr(str);
        unordered_map<string, int> s_map;
        unordered_map<char, int> c_map;

        int i = 0;
        int n = pattern.size();
        for (string w; istr >> w; i++)
        {
            if (i == n || c_map[pattern[i]] != s_map[w])
                return false;
            //to distinguish the default map value of 0.
            c_map[pattern[i]] = s_map[w] = i + 1;
        }
        return i == n;
    }
};