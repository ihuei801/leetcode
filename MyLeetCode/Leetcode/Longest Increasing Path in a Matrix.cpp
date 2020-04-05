/*
 DFS
 */
class Solution {
public:
    vector<vector<int>> dis;
    int dfs(vector<vector<int>>& matrix, int r, int c) {
        vector<pair<int, int>> dir = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        int rows = matrix.size();
        int cols = rows? matrix[0].size() : 0;
        
        if (dis[r][c] != 0) return dis[r][c];
        
        int curr = 1;
        for (auto d : dir) {
            int nb_r = r + d.first;
            int nb_c = c + d.second;
            if (nb_r >= 0 && nb_r < rows && nb_c >= 0 && nb_c < cols && matrix[nb_r][nb_c] > matrix[r][c]) {
                curr = max(curr, 1 + dfs(matrix, nb_r, nb_c));
            }
        }
        dis[r][c] = curr;
        
        return curr;
    }
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        int rows = matrix.size();
        int cols = rows? matrix[0].size() : 0;
        if(!rows || !cols) return 0;
        dis.resize(rows, vector<int>(cols));
        int maxlen = 1;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                maxlen = max(maxlen, dfs(matrix, i, j));
            }
        }
        return maxlen;
        
    }
};