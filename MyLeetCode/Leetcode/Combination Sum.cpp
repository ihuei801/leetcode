class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        if (candidates.empty()) return res;
        sort(candidates.begin(), candidates.end());
        vector<int> path;
        dfs(candidates, 0, target, path, res);
        return res;
    }
    void dfs(vector<int>& candidates, int start, int target, vector<int>& path, vector<vector<int>>& res) {
        if (target == 0) {
            res.push_back(path);
            return;
        }
        for (int i = start; i < candidates.size() && candidates[i] <= target; i++) {
            path.push_back(candidates[i]);
            dfs(candidates, i, target - candidates[i], path, res);
            path.pop_back();
        }
    }
};
//Sean's solution
class Solution {
public:

    void do_combine(vector<int> candidates,
                    vector<vector<int> > &res, 
                    vector<int> &solution, 
                    int target, 
                    int *curr_sum,
                    int start)
    {
        
        if (*curr_sum > target)
            return;
        else if (*curr_sum == target)
        {
            res.push_back(solution);
            return;
        }
        
        for (int i = start; i < candidates.size(); i++)
        {
            solution.push_back(candidates[i]);
            *curr_sum += candidates[i];
            do_combine(candidates, res, solution, target, curr_sum, i);
            *curr_sum -= candidates[i];
            solution.pop_back();
        }
    }
    
    vector<vector<int> > combinationSum(vector<int> &candidates, int target) {
        
        vector<vector<int> >res;
        vector<int>solution;
        int curr_sum = 0;
        
        sort(candidates.begin(), candidates.end());
        do_combine(candidates, res, solution, target, &curr_sum, 0);
        return res;                
    }
};