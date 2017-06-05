class Solution {
public:
    vector<string> generatePossibleNextMoves(string s) {
        vector<string> res;
        int n = s.size();
        if (n == 0) return res;
        for (int i = 0; i < n - 1; i++)
        {
            if (s[i] == '+' && s[i+1] == '+')
                res.push_back(s.substr(0,i)+"--"+s.substr(i+2));
        }
        return res;
    }
};