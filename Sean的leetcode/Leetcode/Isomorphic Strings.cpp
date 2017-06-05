class Solution {
public:
    bool isIsomorphic(string s, string t) {
        int len = s.size();
        map<char, char>m_table;
        set<char>used;

        for (int i = 0; i < len; i++)
        {
            if (m_table.count(s[i]) == 0)
            {
                if (used.count(t[i]) == 0)
                {
                    m_table[s[i]] = t[i];
                    used.insert(t[i]);
                }
                else
                    return false;
            }
            else
            {
                if (m_table[s[i]] != t[i])
                    return false;
            }
        }
        return true;
    }
};