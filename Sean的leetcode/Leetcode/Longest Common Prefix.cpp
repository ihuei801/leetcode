class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string res;
        if (strs.size() == 0) return res;

        for (int i = 0; i < strs[0].size(); i++)
        {
            char c = strs[0][i];
            int j;
            for (j = 1; j < strs.size(); j++)
            {
                if (i >= strs[j].size() || strs[j][i] != c)
                    break;
            }
            if (j == strs.size())
                res += c;
            else
                break;
        }
        return res;
    }
};