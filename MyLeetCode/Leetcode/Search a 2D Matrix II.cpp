//Time: O(row+col)
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int rows = matrix.size();
        int cols = rows? matrix[0].size() : 0;
        int r = rows - 1;
        int c = 0;
        while (r >= 0 && c < cols) {
            if (matrix[r][c] == target) {
                return true;
            }
            else if (matrix[r][c] > target) {
                r--;
            }
            else {
                c++;
            }
        }
        return false;
    }
};
//https://leetcode.com/discuss/47528/c-with-o-m-n-complexity
//Time: O(row+col)
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {

        if (matrix.size() == 0) return false;

        int row = matrix.size();
        int col = matrix[0].size();

        int i = 0;
        int j = col-1;

        while (i < row && j >= 0)
        {
            if (matrix[i][j] == target)
                return true;
            else if (matrix[i][j] < target)
                i++;
            else
                j--;
        }
        return false;
    }
};