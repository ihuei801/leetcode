class Solution {
public:
    vector<string> table = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
    vector<string> letterCombinations(string digits) {
        vector<string> res;
        string path;
        if (digits.empty()) return res;
        dfs(digits, 0, path, res);
        return res;
    }
    void dfs(string& digits, int pos, string& path, vector<string>& res) {
        if (pos == digits.size()) {
            res.push_back(path);
            return;
        }
        string s = table[digits[pos] - '0'];
        for (char c : s) {
            path += c;
            dfs(digits, pos+1, path, res);
            path.pop_back();
        }
    }
};

//Back Tracking
//Backtracking is a more general purpose algorithm.
//Depth-First search is a specific form of backtracking related to searching tree structures. From Wikipedia:
//One starts at the root (selecting some node as the root in the graph case) and explores as far as possible along each branch before backtracking.
//It uses backtracking as part of its means of working with a tree, but is limited to a tree structure.
//Backtracking, though, can be used on any type of structure where portions of the domain can be eliminated - whether or not it is a logical tree. The Wiki example uses a chessboard and a specific problem - you can look at a specific move, and eliminate it, then backtrack to the next possible move, eliminate it, etc.
class Solution {
public:
    void doComb(string s, int start, string &one_sol, vector<string> &res)
    {
        vector<string> dict = {" ", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};

        /*
           note: need to consider if '1' is the last character.
           We need to push one_sol to res. Because '1' is mapping to empty string,
           the following "for-loop" won't be executed.
           However, leetcode test data don't cover this test case.
        */
        if (start == s.size() || (start == s.size() - 1 && s[start] == '1'))
        {
            res.push_back(one_sol);
            return;
        }

        string m_str = dict[s[start]-'0'];
        for (int j = 0; j < m_str.size(); j++)
        {
            one_sol += m_str[j];
            doComb(s, start+1, one_sol, res);
            one_sol.pop_back();
        }
    }

    vector<string> letterCombinations(string digits) {
        string one_sol;
        vector<string> res;
        if (digits == "")
            return res;
        doComb(digits, 0, one_sol, res);
        return res;
    }
};