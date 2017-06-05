//the same solution of N-Queens. Only differs in output form.
class Solution {
public:

    int isValid(int row, int col, vector<int> &one_sol)
    {
        for (int i = 0; i < one_sol.size(); i++)
        {
            if (col == one_sol[i] || (row-i) == abs(one_sol[i]-col))
                return 0;
        }
        return 1;
    }
    
    void doNQueen(int row, int n, vector<vector<int> > &res, vector<int> &one_sol)
    {
        if (row == n)
        {
            res.push_back(one_sol);
            return;
        }            
        for (int col = 0; col < n; col++)
        {
            if (isValid(row, col, one_sol))
            {
                one_sol.push_back(col);
                doNQueen(row+1, n, res, one_sol);
                one_sol.pop_back();
            }
        }
    }
    
    int totalNQueens(int n) {
        vector<vector<int> > res;
        vector<int> one_sol;
        
        doNQueen(0, n , res, one_sol);
        return res.size();            
    }
};