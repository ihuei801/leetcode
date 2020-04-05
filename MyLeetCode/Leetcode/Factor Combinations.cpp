//https://leetcode.com/discuss/51257/share-simple-c-dfs-accepted-solution
class Solution {
public:
    void dfs(int n, vector<int> &one_sol, vector<vector<int>> &res)
    {
        //note: because we don't want to generate duplicate answer.
        //i should be start from one_sol.back();
        int i = one_sol.empty() ? 2 : one_sol.back();

        for (; i*i <= n; i++)
        {
            if ((n % i) == 0)
            {
                one_sol.push_back(i);
                one_sol.push_back(n/i);
                res.push_back(one_sol);
                one_sol.pop_back();
                dfs(n/i, one_sol, res);
                one_sol.pop_back();
            }
        }
    }

    vector<vector<int>> getFactors(int n) {
        vector<int> one_sol;
        vector<vector<int>> res;
        dfs(n, one_sol, res);
        return res;
    }
};