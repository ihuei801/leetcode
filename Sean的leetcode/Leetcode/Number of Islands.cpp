/* DFS
*/
class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int rows = grid.size();
        int cols = rows? grid[0].size() : 0;
        if (!rows || !cols) return 0;
        int num = 0;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == '1') {
                    num++;
                    dfs(grid, i, j);
                }
            }
        }
        return num;
    }
    void dfs(vector<vector<char>>& grid, int r, int c) {
        int rows = grid.size();
        int cols = rows? grid[0].size() : 0;
        vector<pair<int, int>> dir = {{-1, 0}, {0 , -1}, {1, 0}, {0 ,1}};
       
            grid[r][c] = '0';
            for (auto d : dir) {
                int nb_r = r + d.first;
                int nb_c = c + d.second;
                if (nb_r >= 0 && nb_r < rows && nb_c >= 0 && nb_c < cols && grid[nb_r][nb_c] == '1') {
                    dfs(grid, nb_r, nb_c);
                }
            }
    
        
    }
};
//Sean's solution
//https://leetcode.com/discuss/32374/short-dfs-java-solution
//1. When finding one '1', recursively change the connected '1' to '0'.
//2. When finding a new '1', this should be another new island because all old connected '1' are changed to '0'.
struct Direction
{
    int x;
    int y;
};

class Solution {
public:
    void dfs(vector<vector<char>> &grid, int row, int col)
    {
        Direction dir[4] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        int max_row = grid.size();
        int max_col = grid[0].size();

        if (row >= 0 && row < max_row && col >= 0 && col < max_col && grid[row][col] == '1')
        {
            grid[row][col] = '0';
            for (int i = 0; i < 4; i++)
                dfs(grid, row+dir[i].y, col+dir[i].x);
        }
    }

    int numIslands(vector<vector<char>> &grid) {
        int max_row;
        int max_col;
        int num = 0;

        max_row = grid.size();

        if (!max_row) return 0;

        max_col = grid[0].size();
        for (int i = 0; i < max_row; i++)
            for (int j = 0; j < max_col; j++)
            {
                if (grid[i][j] == '1')
                {
                    num++;
                    dfs(grid, i, j);
                }
            }
        return num;
    }
};