class Solution {
public:
    int count(vector<vector<int>>& board, int r, int c) {
        
        int rows = board.size();
        int cols = rows? board[0].size() : 0;
        int cnt = 0;
        for (int i = r-1; i <= r+1; i++) {
            for (int j = c-1; j <= c+1; j++) {
                if (i < 0 || i >= rows || j < 0 || j >= cols) continue;
                cnt += board[i][j] & 1;
            }
        }
        cnt -= board[r][c] & 1;
        return cnt;
    }
    void gameOfLife(vector<vector<int>>& board) {
        int rows = board.size();
        int cols = rows? board[0].size() : 0;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                int cnt = count(board, i, j);
                if (cnt == 3 || (cnt == 2 && board[i][j] == 1)) {
                    board[i][j] |= 2;
                }
            }
        }
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                board[i][j] >>= 1;
            }
        }
    }
};

//https://discuss.leetcode.com/topic/29054/easiest-java-solution-with-explanation
//[next, curr] 1:live 0:dead
//00 01 : initial
class Solution {
public:
    int check(vector<vector<int>>& board, int r, int c) {
        int rows = board.size();
        int cols = rows? board[0].size() : 0;
        int cnt = 0;
        for (int i = r-1; i <= r+1; i++) {
            for (int j = c-1; j <= c+1; j++) {
                if (i < 0 || i >= rows || j < 0 || j >= cols) {
                    continue;
                }
                cnt += board[i][j] & 1;
            }
        }
        cnt -= board[r][c] & 1;
        return cnt;
    }
    void gameOfLife(vector<vector<int>>& board) {
        int row = board.size();
        int col = row? board[0].size() : 0;
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                int count = check(board, i, j);
                if (board[i][j] == 1 && (count == 2 || count == 3)) {
                    board[i][j] = 3;
                }
                else if (board[i][j] == 0 && count == 3) {
                    board[i][j] = 2;
                }
            }
        }
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                board[i][j] >>= 1;
            }
        }
    }
};
//Sean's solution
class Solution {
public:
    void check(vector<vector<int>> &board, int row, int col)
    {
        int max_row = board.size();
        int max_col = board[0].size();
        int live = board[row][col] & 0x1;
        int dir[8][2]= {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};
        int live_count = 0;

        for (int i = 0; i < 8; i++)
        {
            int r = row + dir[i][0];
            int c = col + dir[i][1];

            if (r < 0 || c < 0 || r >= max_row || c >= max_col)
                continue;
            live_count += board[r][c] & 0x1;
        }

        if (live_count == 3 || (live && live_count == 2))
            board[row][col] |= 0x80000000;
    }

    void gameOfLife(vector<vector<int>>& board) {
        int row = board.size();

        if (!row) return;

        int col = board[0].size();

        for (int i = 0; i < row; i++)
            for (int j = 0; j < col; j++)
                check(board, i, j);

        for (int i = 0; i < row; i++)
            for (int j = 0; j < col; j++)
                board[i][j] = board[i][j] & 0x80000000 ? 1 : 0;
    }
};