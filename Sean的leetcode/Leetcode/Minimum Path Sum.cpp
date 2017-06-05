#if 1
class Solution {
public:
    int minPathSum(vector<vector<int> > &grid) {
        int m = grid.size();
        int n;

        if (!m)
            return 0;

        n = grid[0].size();

        for (int i = 1; i < n; i++)
            grid[0][i] += grid[0][i-1];

        for (int i = 1; i < m; i++)
            grid[i][0] += grid[i-1][0];

        for (int i = 1; i < m; i++)
            for (int j = 1; j < n; j++)
            {
                grid[i][j] += std::min(grid[i][j-1], grid[i-1][j]);
            }

        return grid[m-1][n-1];
    }
};
#elif 1 //O(n) space
class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int rows = grid.size();

        if (!rows) return 0;

        int cols = grid[0].size();

        vector<int> dp(cols, 0);

        dp[0] = grid[0][0];
        for (int i = 0; i < rows; i++)
            for (int j = 0; j < cols; j++)
            {
                if (i == 0 && j == 0)
                    continue;
                else if (i == 0)
                    dp[j] = dp[j-1]+grid[i][j];
                else if (j == 0)
                    dp[j] += grid[i][j];
                else
                    dp[j] = min(dp[j-1], dp[j]) + grid[i][j];
            }

        return dp[cols-1];
    }
};
#endif