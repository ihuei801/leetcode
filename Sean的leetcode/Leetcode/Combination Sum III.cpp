class Solution {
public:

    void do_combine(vector<vector <int>> &res, vector<int> &one_sol, int k, int remain_sum, int start, int end)
    {
        if (remain_sum < 0)
            return;

        if (remain_sum == 0 && one_sol.size() == k)
        {
            res.push_back(one_sol);
            return;
        }

        for (int i = start; i <= end; i++)
        {
            one_sol.push_back(i);
            do_combine(res, one_sol, k, remain_sum-i, i+1, end);
            one_sol.pop_back();
        }
    }

    vector<vector<int>> combinationSum3(int k, int n) {
        vector<vector <int>>res;
        vector<int> one_sol;
        do_combine(res, one_sol, k, n, 1, 9);
        return res;
    }
};