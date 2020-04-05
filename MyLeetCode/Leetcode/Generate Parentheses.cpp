//Backtracking
class Solution {
public:
    void dfs(int l_cnt, int r_cnt, string& one_sol, vector<string>& res) {
        if (l_cnt == 0 && r_cnt == 0) {
            res.push_back(one_sol);
            return;
        }
        if (l_cnt > 0) {
            one_sol += "(";
            dfs(l_cnt - 1, r_cnt + 1, one_sol, res);
            one_sol.pop_back();
        }
        if (r_cnt > 0) {
            one_sol += ")";
            dfs(l_cnt, r_cnt - 1, one_sol, res);
            one_sol.pop_back();
        }
    }
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        string one_sol;
        dfs(n, 0, one_sol, res);
        return res;
    }
};
//http://fisherlei.blogspot.tw/2012/12/leetcode-generate-parentheses.html
class Solution {
public:
    void genParen(int n, int remain_n, int open_left, string &one_sol, vector<string> &res)
    {
        if (one_sol.size() == n * 2)
        {
            res.push_back(one_sol);
            return;
        }

        if (open_left)
        {
            one_sol += ")";
            genParen(n, remain_n, open_left-1, one_sol, res);
            one_sol.pop_back();
        }

        if (remain_n)
        {
            one_sol += "(";
            genParen(n, remain_n-1, open_left+1, one_sol, res);
            one_sol.pop_back();
        }
    }

    vector<string> generateParenthesis(int n) {
        vector<string> res;
        string one_sol;
        genParen(n, n, 0, one_sol, res);
        return res;
    }
};
