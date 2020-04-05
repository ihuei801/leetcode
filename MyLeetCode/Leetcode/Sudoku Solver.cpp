//https://leetcode.com/discuss/44834/4ms-36line-c
//1. empty_cells: collect all '.' (row, col) pair
//2. use backtracking to try all possible '1' to '9' on each empty cell.
class Solution {
public:
    int r[9][9];
    int c[9][9];
    int s[9][9];
    void solveSudoku(vector<vector<char>>& board) {
        int rows = board.size();
        int cols = rows? board[0].size() : 0;
        vector<pair<int, int>> emp;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (board[i][j] != '.') {
                    int val = board[i][j] - '1';
                    int idx = i/3 * 3 + j/3;
                    r[i][val] = c[j][val] = s[idx][val] = 1;
                }
                else {
                    emp.push_back({i,j});
                }
            }
        }
        solve(board, emp, 0);
    }
    bool solve(vector<vector<char>>& board, vector<pair<int, int>>& emp, int pos) {
        if (pos == emp.size()) return true;
        int i = emp[pos].first;
        int j = emp[pos].second;
        for (char ch = '1'; ch <= '9'; ch++) {
            int val = ch - '1';
            int idx = i/3 * 3 + j/3;
            if (!r[i][val] && !c[j][val] && !s[idx][val]) {
                board[i][j] = ch;
                r[i][val] = c[j][val] = s[idx][val] = 1;
                if(solve(board, emp, pos+1)) return true;
                board[i][j] = '.';
                r[i][val] = c[j][val] = s[idx][val] = 0;
            }
        }
        return false;
        
    }
};

//https://leetcode.com/discuss/44834/4ms-36line-c
//1. empty_cells: collect all '.' (row, col) pair
//2. use backtracking to try all possible '1' to '9' on each empty cell.
class Solution {
public:

    int check_row[9][9];
    int check_col[9][9];
    int check_block[9][9];

    bool isValid(int row, int col, int c)
    {
        return !check_row[row][c-'1'] && !check_col[col][c-'1'] && !check_block[(row/3)*3+(col/3)][c-'1'];
    }

    bool solve(vector<vector<char>>& board, vector<pair<int, int> > &empty_cells, int idx)
    {
        if (idx == empty_cells.size())
            return true;

        int row = empty_cells[idx].first;
        int col = empty_cells[idx].second;

        for (char c = '1'; c <= '9'; c++)
        {
            if (isValid(row, col, c))
            {
                board[row][col] = c;
                check_row[row][c-'1'] =
                check_col[col][c-'1'] =
                check_block[(row/3)*3+(col/3)][c-'1'] = 1;
                if (solve(board, empty_cells, idx+1))
                    return true;
                //revert change
                board[row][col] = '.';
                check_row[row][c-'1'] =
                check_col[col][c-'1'] =
                check_block[(row/3)*3+(col/3)][c-'1'] = 0;
            }
        }
        return false;
    }

    void solveSudoku(vector<vector<char>>& board) {
        int max_row = board.size() - 1;
        int max_col = board[0].size() - 1;
        vector<pair<int, int> > empty_cells;

        for (int i = 0; i <= max_row; i++)
            for (int j = 0; j <= max_col; j++)
            {
                int c = board[i][j];
                if (c == '.')
                    empty_cells.push_back(make_pair(i, j));
                else
                {
                    check_row[i][c-'1'] = 1;
                    check_col[j][c-'1'] = 1;
                    check_block[(i/3)*3+(j/3)][c-'1'] = 1;
                }
            }
        solve(board, empty_cells, 0);
    }
};