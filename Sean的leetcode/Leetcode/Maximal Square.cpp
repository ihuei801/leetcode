//https://leetcode.com/discuss/38489/easy-solution-with-detailed-explanations-8ms-time-and-space
//O(max_row*max_col) time, O(max_col) space.
class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        int max_row = matrix.size();

        if (max_row == 0) return 0;

        int max_col = matrix[0].size();

        //the maximal size of the square that can be achieved at col(i) which is the previous row.
        vector<int>pre_row(max_col, 0);
        int max_size = 0;
        int curr_size;
        int left_size;
        for (int i = 0; i < max_row; i++)
            for (int j = 0; j < max_col; j++)
            {
                //first row/col: matrix[i][j] is 0: square size is 0.
                //               matrix[i][j] is 1: square size is 1.
                if (i == 0 || j == 0)
                    curr_size = matrix[i][j] - '0';
                else
                {
                    if (matrix[i][j] == '1')
                    {
                        curr_size = min(min(left_size, pre_row[j]), pre_row[j-1]) + 1;
                    }
                    else
                        curr_size = 0;

                    //update pre_row[j-1] to the previous curr_size
                    pre_row[j-1] = left_size;

                }

                //if j is the last col or i is the first row, update curr_size directly
                if (j == max_col - 1 || i == 0)
                    pre_row[j] = curr_size;

                max_size = max(max_size, curr_size);
                left_size = curr_size;
            }
        return max_size * max_size;
    }
};