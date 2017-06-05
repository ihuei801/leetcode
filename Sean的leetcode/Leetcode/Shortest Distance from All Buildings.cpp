//BFS
class Solution {
public:
    int shortestDistance(vector<vector<int>>& grid) {
        int rows = grid.size();
        int cols = rows? grid[0].size() : 0;
        if (!rows || !cols) return -1;
        vector<vector<int>> distance(rows, vector<int>(cols));
        vector<vector<int>> reach(rows, vector<int>(cols));
        vector<pair<int, int>> directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        int num = 0;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == 1) {
                    num++;
                    vector<vector<bool>> isVisited(rows, vector<bool>(cols));
                    queue<pair<int, int>> q;
                    q.push(make_pair(i, j));
                    int level = 1;
                    while (!q.empty()) {
                        int size = q.size();
                        for (int k = 0; k < size; k++) {
                            int r = q.front().first;
                            int c = q.front().second;
                            q.pop();
                            for (auto d : directions) {
                                int nb_r = r + d.first;
                                int nb_c = c + d.second;
                                if (nb_r >= 0 && nb_r < rows && nb_c >= 0 && nb_c < cols && grid[nb_r][nb_c] == 0 && !isVisited[nb_r][nb_c]) {
                                    distance[nb_r][nb_c] += level;
                                    reach[nb_r][nb_c]++;
                                    isVisited[nb_r][nb_c] = true;
                                    q.push(make_pair(nb_r, nb_c));
                                }
                            }
                        }
                        level++;
                    }
                    
                    
                }
            }
        }
        int mindis = INT_MAX;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == 0 && reach[i][j] == num) {
                    mindis = min(mindis, distance[i][j]);
                }
            }
        }
        return mindis == INT_MAX? -1 : mindis;
        
    }
};