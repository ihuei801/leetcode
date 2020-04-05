//BFS
class Solution {
public:
    void wallsAndGates(vector<vector<int>>& rooms) {
        int rows = rooms.size();
        int cols = rows? rooms[0].size() : 0;
        if (!rows || !cols) return;
        queue<pair<int, int>> q;
        vector<pair<int, int>> dir = {{-1, 0}, {0, -1}, {1, 0}, {0, 1}};
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (rooms[i][j] == 0) {
                    q.push(make_pair(i,j));
                    
                }
            }
        }
        int level = 1;
        while (!q.empty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                auto tmp = q.front();
                q.pop();
                int r = tmp.first;
                int c = tmp.second;
                for (auto d : dir) {
                    int nb_r = r + d.first;
                    int nb_c = c + d.second;
                    if (nb_r >= 0 && nb_c >= 0 && nb_r < rows && nb_c < cols && rooms[nb_r][nb_c] == INT_MAX) {
                        rooms[nb_r][nb_c] = level;
                        q.push(make_pair(nb_r, nb_c));
                    }
                }
            }
            level++;
        }
    }
};
//Sean's solution
class Solution {
public:
    void wallsAndGates(vector<vector<int>>& rooms) {
        int rows = rooms.size();
        int cols = rows? rooms[0].size() : 0;
        if (rows == 0 || cols == 0) return;
        queue<pair<int, int>> q;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (!rooms[i][j]) {
                    q.push(make_pair(i,j));
                }
            }
        }
        while (!q.empty()) {
            int r = q.front().first;
            int c = q.front().second;
            q.pop();
            if (r > 0 && rooms[r-1][c] == INT_MAX) {
                rooms[r-1][c] = rooms[r][c] + 1;
                q.push(make_pair(r-1,c));
            }
            if (c > 0 && rooms[r][c-1] == INT_MAX) {
                rooms[r][c-1] = rooms[r][c] + 1;
                q.push(make_pair(r,c-1));
            }
            if (r + 1 < rows && rooms[r+1][c] == INT_MAX) {
                rooms[r+1][c] = rooms[r][c] + 1;
                q.push(make_pair(r+1,c));
            }
            if (c + 1 < cols && rooms[r][c+1] == INT_MAX) {
                rooms[r][c+1] = rooms[r][c] + 1;
                q.push(make_pair(r,c+1));
            }
        }
        
    }
};
//Sean's solution
//https://leetcode.com/discuss/60418/c-bfs-clean-solution-with-simple-explanations
class Solution {
public:
    void wallsAndGates(vector<vector<int>>& rooms) {
        int row = rooms.size();
        if (!row) return;

        int col = rooms[0].size();

        queue<pair<int,int>> q;

        for (int i = 0; i < row; i++)
            for (int j = 0; j < col; j++)
            {
                if (!rooms[i][j])
                    q.push(make_pair(i, j));
            }

        while (!q.empty())
        {
            int r_val = q.front().first;
            int c_val = q.front().second;
            q.pop();
            int dir[] = {0, 1, 0, -1, 0};
            for (int i = 0; i < 4; i++)
            {
                int r = r_val + dir[i];
                int c = c_val + dir[i+1];
                if (r < 0 || c < 0 || r >= row || c >= col
                    || rooms[r_val][c_val]+1 >= rooms[r][c])
                    continue;

                rooms[r][c] = rooms[r_val][c_val]+1;
                q.push(make_pair(r, c));
            }
        }
    }
};