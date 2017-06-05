class Solution {
public:
    vector<vector<string>> groupStrings(vector<string>& strings) {
        unordered_map<string, vector<string>> s_map;
        vector<vector<string>> res;
        for (auto s : strings)
        {
            string key;
            for (int i = 0; i < s.size(); i++)
            {
                int diff = s[i] - s[0];
                diff += diff < 0 ? 26 : 0;
                char c = 'a' + diff;
                key += c;
            }
            s_map[key].push_back(s);
        }
        for (auto m : s_map)
        {
            //sort(m.second.begin(), m.second.end());
            res.push_back(m.second);
        }
        return res;
    }
};