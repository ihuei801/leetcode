class Solution {
public:

    int do_combine(vector<vector<int> > &res, vector<int> &one_sol, int start, int end, int k)
    {
        if (one_sol.size() == k)
        {
            res.push_back(one_sol);
            return 0;
        }

        for (int i = start; i <= end; i++)
        {
            one_sol.push_back(i);
            do_combine(res, one_sol, i+1, end, k);
            one_sol.pop_back();
        }
        return 0;
    }

    vector<vector<int> > combine(int n, int k) {
        vector<vector<int> > res;
        vector<int> one_sol;
        do_combine(res, one_sol, 1, n, k);
        return res;
    }
};