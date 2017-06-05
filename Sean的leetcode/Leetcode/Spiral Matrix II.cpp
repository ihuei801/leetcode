/*
n = 3, process 2 (i.e. n-1) elements in each direction.

a a b
d e b
d c c

*/
class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int> > res(n, vector<int>(n, 0));
        int start_row = 0;
        int start_col = 0;
        int num = 1;

        while (n > 0)
        {
            if (n == 1)
                res[start_row][start_col] = num;
            else
            {
                int max_row = start_row + n - 1;
                int max_col = start_col + n - 1;

                for (int i = start_col; i < max_col; i++)
                    res[start_row][i] = num++;
                for (int i = start_row; i < max_row; i++)
                    res[i][max_col] = num++;
                for (int i = max_col; i > start_col; i--)
                    res[max_row][i] = num++;
                for (int i = max_row; i > start_row; i--)
                    res[i][start_col] = num++;
            }
            n -= 2;
            start_row++;
            start_col++;
        }
        return res;
    }
};