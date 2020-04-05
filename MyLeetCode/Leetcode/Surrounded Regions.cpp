#if 1 //BFS
///https://leetcode.com/discuss/38891/simple-bfs-solution-easy-to-understand
//expand 'O' from 4 boundaries (top, bottom, left ,right)
class Solution {
public:
    void check(vector<vector<char>>& board, queue<pair<int, int>> &q, int row, int col)
    {
        int max_row = board.size() - 1;
        int max_col = board[0].size() - 1;
        if (row < 0 || col < 0 || row > max_row || col > max_col)
            return;

        if (board[row][col] == 'O')
        {
            board[row][col] = '#';
            q.push(make_pair(row, col));
        }
    }

    void solve(vector<vector<char>>& board) {

        if (board.size() == 0) return ;

        queue<pair<int, int>>q;
        int max_row = board.size() - 1;
        int max_col = board[0].size() - 1;

        for (int i = 0; i <= max_row; i++)
        {
            if (board[i][0] == 'O')
            {
                board[i][0] = '#';
                q.push(make_pair(i, 0));
            }
            if (board[i][max_col] == 'O')
            {
                board[i][max_col] = '#';
                q.push(make_pair(i, max_col));
            }
        }

        for (int i = 0; i <= max_col; i++)
        {
            if (board[0][i] == 'O')
            {
                board[0][i] = '#';
                q.push(make_pair(0, i));
            }
            if (board[max_row][i] == 'O')
            {
                board[max_row][i] = '#';
                q.push(make_pair(max_row, i));
            }
        }

        while (!q.empty())
        {
            int row = q.front().first;
            int col = q.front().second;
            q.pop();

            check(board, q, row+1, col);
            check(board, q, row-1, col);
            check(board, q, row, col+1);
            check(board, q, row, col-1);
        }
        for (int i = 0; i <= max_row; i++)
            for (int j = 0; j <= max_col; j++)
                board[i][j] = board[i][j] == '#' ? 'O' : 'X';
    }
};
#else //DFS
//http://blog.csdn.net/ojshilu/article/details/22600449
//http://translate.googleusercontent.com/translate_c?depth=1&hl=en&prev=search&rurl=translate.google.com&sl=zh-CN&u=http://zh.wikipedia.org/wiki/Flood_fill&usg=ALkJrhiUFB7zBvvy82xY1AXwgOLJ-P19vw
//flood algorithm
class Solution {
public:
    void dfs(vector<vector<char>>& board, int row, int col)
    {
        int max_row = board.size() - 1;
        int max_col = board[0].size() - 1;

        if (row < 0 || col < 0 || row > max_row || col > max_col)
            return;

        if (board[row][col] == 'O')
        {
            board[row][col] = '#';
            /* To prevent stack overflow:
            check down: ROW row-1  has been checked. So, no need to check the "down" direction for ROW max_row-2.So, start from ROW max_row-3.
            */
            if (row < max_row - 1)
                dfs(board, row+1, col);
            if (row > 1)
                dfs(board, row-1, col);
            if (col < max_row - 1)
                dfs(board, row, col+1);
            if (col > 1)
                dfs(board, row, col-1);
        }
    }

    void solve(vector<vector<char>>& board) {

        if (board.size() == 0) return;

        int max_row = board.size() - 1;
        int max_col = board[0].size() - 1;

        for (int i = 0; i <= max_row; i++)
        {
            if (board[i][0] == 'O')
                dfs(board, i, 0);
            if (board[i][max_col] == 'O')
                dfs(board, i, max_col);
        }
        for (int i = 0; i <= max_col; i++)
        {
            if (board[0][i] == 'O')
                dfs(board, 0, i);
            if (board[max_row][i] == 'O')
                dfs(board, max_row, i);
        }

        for (int i = 0; i <= max_row; i++)
            for (int j = 0; j <= max_col; j++)
                board[i][j] = board[i][j] == '#' ? 'O' : 'X';
    }
};
#endif