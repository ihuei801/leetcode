/** DFS approach to mark position that can meet pacific and atlantic
 */
cclass Solution {
public:
    vector<pair<int, int>> pacificAtlantic(vector<vector<int>>& matrix) {
        vector<pair<int, int>> res;
        int rows = matrix.size();
        int cols = rows? matrix[0].size() : 0;
        if (!rows || !cols) return res;
        vector<vector<bool>> pacific(rows, vector<bool>(cols));
        vector<vector<bool>> atlantic(rows, vector<bool>(cols));
        for (int i = 0; i < rows; i++) {
            dfs(matrix, pacific, i, 0);
            dfs(matrix, atlantic, i, cols-1);
        }
        for (int j = 0; j < cols; j++) {
            dfs(matrix, pacific, 0, j);
            dfs(matrix, atlantic, rows-1, j);
        }
        
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (pacific[i][j] && atlantic[i][j]){
                    res.push_back({i, j});
                }
            }
        }
        return res;
    }
    void dfs(vector<vector<int>>& matrix, vector<vector<bool>>& visit, int r, int c) {
        int rows = matrix.size();
        int cols = rows? matrix[0].size() : 0;
        vector<pair<int, int>> dir = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};
        visit[r][c] = true;
        for (auto d : dir) {
            int nb_r = r + d.first;
            int nb_c = c + d.second;
            if (nb_r >= 0 && nb_r < rows && nb_c >= 0 && nb_c < cols && !visit[nb_r][nb_c] && matrix[nb_r][nb_c] >= matrix[r][c])
            dfs(matrix, visit, nb_r, nb_c);
        }
    }
};