class Solution {
public:
    void genSub(vector<int>& nums, int start, vector<int> &one_sol, vector<vector<int> > &res)
    {
        for (int i = start; i < nums.size(); i++)
        {
            one_sol.push_back(nums[i]);
            res.push_back(one_sol);
            genSub(nums, i+1, one_sol, res);
            one_sol.pop_back();

            while (i + 1 < nums.size() && nums[i] == nums[i+1])
                i++;
        }
    }

    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<int> one_sol;
        vector<vector<int> > res;

        res.push_back(one_sol);
        sort(nums.begin(), nums.end());

        genSub(nums, 0, one_sol, res);
        return res;
    }
};