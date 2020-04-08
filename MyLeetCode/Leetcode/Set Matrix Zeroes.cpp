//https://leetcode.com/discuss/15997/any-shortest-o-1-space-solution
class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int rows = matrix.size();
        if(!rows) return;

        int cols = matrix[0].size();
        int col0 = 0;
        for (int i = 0; i < rows; i++)
        {
            if (matrix[i][0] == 0)
                col0 = 1;
            for (int j = 1; j < cols; j++)
            {
                if (matrix[i][j] == 0)
                {
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
             }
        }

        for (int i = rows-1; i >= 0; i--)
        {
            for (int j = cols-1; j >= 1; j--)
            {
                if (matrix[i][0] == 0 || matrix[0][j] == 0)
                    matrix[i][j] = 0;
            }
            if (col0)
                matrix[i][0] = 0;
        }
    }
};