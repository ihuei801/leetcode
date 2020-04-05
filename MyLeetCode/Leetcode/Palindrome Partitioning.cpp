//use recursive solution.
class Solution {
public:

    bool isPalindrome(string s, int start, int end)
    {
        while (start < end)
        {
            if (s[start] != s[end])
                return false;
            start++, end--;
        }
        return true;
    }

    void findPalindrome(string s, int start, vector<string> &one_sol, vector<vector<string> > &res)
    {
        if (start == s.size())
            res.push_back(one_sol);
        for (int i = start; i < s.size(); i++)
        {
            if (isPalindrome(s, start, i))
            {
                one_sol.push_back(s.substr(start, i-start+1));
                findPalindrome(s, i+1, one_sol, res);
                one_sol.pop_back();
            }
        }
    }

    vector<vector<string>> partition(string s) {
        vector<string>one_sol;
        vector<vector<string> >res;
        findPalindrome(s, 0, one_sol, res);
        return res;
    }
};