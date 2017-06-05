//DFS
class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<vector<int>> sol;
        vector<int> path;
        sort(candidates.begin(), candidates.end());
        comb(candidates, 0, 0, target, path, sol);
        return sol;
    }
    void comb(vector<int>& candidates, int pos, int sum, int target, vector<int>& path, vector<vector<int>>& sol){
        if (sum > target) return;
        if (sum == target) {
            sol.push_back(path);
            return;
        }
        for (int i = pos; i < candidates.size(); i++) {
            path.push_back(candidates[i]);
            comb(candidates, i+1, sum + candidates[i], target, path, sol);
            path.pop_back();
            i++;
            while (i < candidates.size() && candidates[i] == candidates[i-1]){
                i++;
            }
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
            
            //difference between Combination Sum: (i to i+1)
            do_combine(candidates, res, solution, target, curr_sum, i+1);
            *curr_sum -= candidates[i];
            solution.pop_back();
            
            //difference between Combination Sum: skip the repeating elements
            while (i < candidates.size() - 1 && candidates[i] == candidates[i+1])
                i++;
        }
    }
    
    vector<vector<int> > combinationSum2(vector<int> &candidates, int target) {
        
        vector<vector<int> >res;
        vector<int>solution;
        int curr_sum = 0;
        
        sort(candidates.begin(), candidates.end());
        do_combine(candidates, res, solution, target, &curr_sum, 0);
        return res;                
    }
};