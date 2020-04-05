//http://yucoding.blogspot.tw/2013/01/leetcode-question-59-n-queens.html
//one_sol[i] = j,  means put a queen at (row, col) = (i, j)
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
    
    vector<vector<string> > solveNQueens(int n) {
        vector<vector<int> > res;
        vector<int> one_sol;
        vector<vector<string> > answer;
        vector<string> one_answer;
        
        doNQueen(0, n, res, one_sol);
        
        for (int i = 0; i < res.size(); i++)
        {
            one_answer.clear();
            for (int j = 0; j < res[i].size(); j++)
            {
                string str(n, '.');
                str[res[i][j]] = 'Q';
                one_answer.push_back(str);
            }
            answer.push_back(one_answer);
        }
        return answer;
    }
};