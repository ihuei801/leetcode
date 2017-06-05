class Solution {
public:
    void genIP(string s, int start, string &one_sol, vector<string> &res, int count)
    {
        if (count > 4)
            return;
        if (start == s.size())
        {
            if (count == 4)
                res.push_back(one_sol);
            return;
        }

        for (int i = start; i < s.size() && i < start + 3; i++)
        {
            string sub = s.substr(start, i-start+1);
            int num = stoi(sub);
            if (sub[0] == '0' && sub.size() > 1)
                break;
            if (num >= 0 && num <= 255)
            {
                int org_size = one_sol.size();
                if (org_size)
                    one_sol += ".";
                one_sol += sub;
                genIP(s, i+1, one_sol, res, count+1);
                one_sol.resize(org_size);
            }
        }
    }

    vector<string> restoreIpAddresses(string s) {
        vector<string> res;
        string one_sol;
        genIP(s, 0, one_sol, res, 0);
        return res;
    }
};