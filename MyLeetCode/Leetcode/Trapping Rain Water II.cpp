// from the borders, pick the shortest cell visited and check its neighbors:
// if the neighbor is shorter, collect the water it can trap and update its height as its height plus the water trapped
// add all its neighbors to the queue.
class Solution {
public:
    struct Cell{
        int r;
        int c;
        int h;
        Cell(int row, int col, int height) : r(row), c(col), h(height){}
    };
    struct cmp{
        bool operator()(Cell& a, Cell& b) {
            return a.h > b.h;
        }
    };
    int trapRainWater(vector<vector<int>>& heightMap) {
        priority_queue<Cell, vector<Cell>, cmp> pq;
        int rows = heightMap.size();
        int cols = rows? heightMap[0].size() : 0;
        vector<vector<bool>> visit(rows, vector<bool>(cols));
        for (int i = 0; i < rows; i++) {
            pq.push(Cell(i, 0, heightMap[i][0]));
            pq.push(Cell(i, cols-1, heightMap[i][cols-1]));
            visit[i][0] = true;
            visit[i][cols-1] = true;
        }
        for (int j = 0; j < cols; j++) {
            pq.push(Cell(0, j, heightMap[0][j]));
            pq.push(Cell(rows-1, j, heightMap[rows-1][j]));
            visit[0][j] = true;
            visit[rows-1][j] = true;
        }
        int res = 0;
        vector<pair<int, int>> dir = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};
        while (!pq.empty()) {
            Cell tmp = pq.top();
            pq.pop();
            for (auto d : dir) {
                int nb_r = tmp.r + d.first;
                int nb_c = tmp.c + d.second;
                if (nb_r >= 0 && nb_r < rows && nb_c >= 0 && nb_c < cols && !visit[nb_r][nb_c]) {
                    visit[nb_r][nb_c] = true;
                    int border = max(tmp.h, heightMap[nb_r][nb_c]);
                    res += border - heightMap[nb_r][nb_c];
                    pq.push(Cell(nb_r, nb_c, border));
                }
            }
        }
        return res;
    }
};