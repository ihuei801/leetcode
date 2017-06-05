class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int> > &obstacleGrid) {
        int row = obstacleGrid.size();
        int col = obstacleGrid[0].size();
        vector<int>count (col, 0);

        if (!row || !col)
            return 0;

        count[0] = !obstacleGrid[0][0];

        for (int i = 0; i < row; i++)
            for (int j = 0; j < col; j++)
            {
                //reset current count[j] to zero when encountering obstacle.
                if (obstacleGrid[i][j] == 1)
                    count[j] = 0;
                else
                {
                    if (j > 0)
                        count[j] += count[j-1];
                }
            }
        return count[col-1];
    }
};