//O(mn)
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> sol;
        int rows = matrix.size();
        int cols = rows? matrix[0].size() : 0;
        int left = 0;
        int right = matrix[0].size() - 1;
        int up = 0;
        int down = matrix.size() - 1;
        while(1){
            for(int j = left; j <= right; j++){
                sol.push_back(matrix[up][j]);
            }
            up++;
            if(up > down) break;
            for(int i = up; i <= down; i++){
                sol.push_back(matrix[i][right]);
            }
            right--;
            if(left > right) break;
            for(int j = right; j >= left; j--){
                sol.push_back(matrix[down][j]);
            }
            down--;
            if(up > down) break;
            for(int i = down; i >= up; i--){
                sol.push_back(matrix[i][left]);
            }
            left++;
            if(left > right) break;
        }
        return sol;
        
    }
};
//Sean's solution
//for 6x4 matrix: each row access 5 (6-1) elements and each col access 3 (4-1) elements.
//Then the origianl matrix become 4x2 (6-2)x(4-2) matrix
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> res;
        int row = matrix.size();

        if (!row) return res;

        int col = matrix[0].size();

        int start_row = 0;
        int start_col = 0;

        while (row > 0 && col > 0)
        {
            int max_col = start_col + col - 1;
            int max_row = start_row + row - 1;

            if (row == 1)
            {
                for (int j = start_col; j < max_col+1; j++)
                    res.push_back(matrix[start_row][j]);
                return res;
            }
            if (col == 1)
            {
                for (int i = start_row; i < max_row+1; i++)
                    res.push_back(matrix[i][start_col]);
                return res;
            }

            for (int j = start_col; j < max_col; j++)
                res.push_back(matrix[start_row][j]);
            for (int i = start_row; i < max_row; i++)
                res.push_back(matrix[i][max_col]);
            for (int j = max_col; j > start_col; j--)
                res.push_back(matrix[max_row][j]);
            for (int i = max_row; i > start_row; i--)
                res.push_back(matrix[i][start_col]);

            start_row++;
            start_col++;
            row -= 2;
            col -= 2;
        }
        return res;
    }
};