//add map<int, int>duplicate to record duplicate num at the same position.
class Solution {
public:

    void do_permute(vector<int> &num, vector<vector<int> > &res, vector<int> &one_sol, vector<int> &selected)
    {
        map<int, int>duplicate;        
        
        if (one_sol.size() == num.size())
        {
            res.push_back(one_sol);
            return;
        }
        
        for (int i = 0; i < num.size(); i++)
        {
            if (selected[i] || duplicate.find(num[i]) != duplicate.end())
                continue;
                
            duplicate[num[i]] = 1;
            selected[i] = 1;
            one_sol.push_back(num[i]);
            do_permute(num, res, one_sol, selected);
            one_sol.pop_back();
            selected[i] = 0;
        }
        return;
    }
    
    
    vector<vector<int> > permuteUnique(vector<int> &num) {
        vector<vector<int> >res;
        vector<int>one_sol;
        vector<int>selected(num.size(), 0);
        do_permute(num, res, one_sol, selected);
        return res;
    }
};