/*
n = 4, all number below are index

(0, 1) = (2, 0)
 *           *

(2, 0) = (3, 2)
 *           *

(3, 2) = (1, 3)
 *           *

(1, 3) = (0, 1)
 *           *

*/

class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();
        int start_pos = 0;
        int max_pos = n-1;

        while (n > 1)
        {
            //note: i < n-1 not i < n
            for (int i = 0; i < n-1; i++)
            {
                int p = start_pos + i;
                int q = max_pos - p;
                int r = max_pos - start_pos;
                int temp = matrix[start_pos][p];

                matrix[start_pos][p] = matrix[q][start_pos];
                matrix[q][start_pos] = matrix[r][q];
                matrix[r][q] = matrix[p][r];
                matrix[p][r] = temp;
            }
            n -= 2;
            start_pos++;
        }
    }
};