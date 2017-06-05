class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string> > res;
        unordered_map<string, multiset<string> >s_map;

        for (auto str : strs)
        {
            string s = str;
            sort(s.begin(), s.end());
            s_map[s].insert(str);
        }

        for (auto m : s_map)
        {
            vector<string> vs;
            for (auto s : m.second)
                vs.push_back(s);
            res.push_back(vs);
        }
        return res;
    }
};