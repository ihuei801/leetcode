/*
Walk through the matrix. At the start of each non-wall-streak (row-wise or column-wise), count the number of hits in that streak and remember it. 
Time Comlexity: O(mn), Space Complexity: O(n).
*/
class Solution {
public:
    int maxKilledEnemies(vector<vector<char>>& grid) {
        int rows = grid.size();
        int cols = rows? grid[0].size() : 0;
        vector<int> colhits(cols);
        int rowhits = 0;
        int maxhits = 0;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (!j || grid[i][j-1] == 'W') {
                    rowhits = 0;
                    for (int k = j; k < cols && grid[i][k] != 'W'; k++) {
                        rowhits += grid[i][k] == 'E';
                    }
                }
                if (!i || grid[i-1][j] == 'W') {
                    colhits[j] = 0;
                    for (int k = i; k < rows && grid[k][j] != 'W'; k++) {
                        colhits[j] += grid[k][j] == 'E';
                    }
                }
                if (grid[i][j] == '0') {
                    maxhits = max(maxhits, rowhits + colhits[j]);
                }
            }
        }
        return maxhits;
    }
};