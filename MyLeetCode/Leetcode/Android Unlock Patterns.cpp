//DFS
class Solution {
public:
    vector<vector<int>> skip;
    int numberOfPatterns(int m, int n) {
        skip.resize(10, vector<int>(10));
        skip[1][3] = skip[3][1] = 2;
        skip[1][7] = skip[7][1] = 4;
        skip[3][9] = skip[9][3] = 6;
        skip[7][9] = skip[9][7] = 8;
        skip[1][9] = skip[9][1] = skip[3][7] = skip[7][3] = skip[4][6] = skip[6][4] = skip[2][8] = skip[8][2] = 5;
        vector<bool> visit(10);
        int cnt = 0;
        for (int i = m; i <= n; i++) {
            cnt += dfs(visit, 1, i) * 4;
            cnt += dfs(visit, 2, i) * 4;
            cnt += dfs(visit, 5, i);
        }
        return cnt;
    }
    int dfs(vector<bool>& visit, int cur, int remain) {
        if (remain == 1) {
            return 1;
        }
        visit[cur] = true;
        remain--;
        int cnt = 0;
        for (int i = 1; i <= 9; i++) {
            if (!visit[i] && (!skip[i][cur] || visit[skip[i][cur]])) {
                cnt += dfs(visit, i, remain);
            }
        }
        visit[cur] = false;
        return cnt;
    }
};


class Solution {
public:
    int numberOfPatterns(int m, int n) {
        vector<vector<int>> skip(10, vector<int>(10));
        skip[1][3] = skip[3][1] = 2;
        skip[1][7] = skip[7][1] = 4;
        skip[3][9] = skip[9][3] = 6;
        skip[7][9] = skip[9][7] = 8;
        skip[1][9] = skip[9][1] = skip[3][7] = skip[7][3] = skip[2][8] = skip[8][2] = skip[4][6] = skip[6][4] = 5;
        vector<bool> visit(10);
        int res = 0;
        for (int i = m; i <= n; i++) {
            res += dfs(skip, visit, 1, i - 1) * 4;
            res += dfs(skip, visit, 2, i - 1) * 4;
            res += dfs(skip, visit, 5, i - 1);
        }
        return res;
    }
    int dfs(vector<vector<int>>& skip, vector<bool>& visit, int cur, int remain) {

        if (remain == 0) return 1;
        visit[cur] = true;
        int res = 0;
        for (int i = 1; i <= 9; i++) {
            if (!visit[i] && (skip[cur][i] == 0 || visit[skip[cur][i]]) && remain-1 >= 0) {
                res += dfs(skip, visit, i, remain - 1);
            }
        }
        visit[cur] = false;
        return res;
    } 
};