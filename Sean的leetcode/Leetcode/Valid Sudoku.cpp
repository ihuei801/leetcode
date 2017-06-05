class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        int r[9][9] = {0};
        int c[9][9] = {0};
        int s[9][9] = {0};
        int rows = board.size();
        int cols = rows? board[0].size() : 0;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (board[i][j] != '.') {
                    int val = board[i][j] - '1';
                    int idx = i / 3 * 3 + j / 3;
                    if (r[i][val] || c[j][val] || s[idx][val]) {
                        return false;
                    }
                    r[i][val] = c[j][val] = s[idx][val] = 1;
                }
            }
        }
        return true;
        
    }
};

//https://oj.leetcode.com/discuss/14929/very-simple-c-solution
class Solution {
public:
    bool isValidSudoku(vector<vector<char> > &board) {
        vector<vector<int> > check(3, vector<int>(9, 0));

        for (int i = 0; i < 9; i++)
        {
            for (int j = 0; j < 9; j++)
            {
                int row, col;
                if (board[i][j] != '.' && ++check[0][board[i][j]-'1'] > 1) return false;
                if (board[j][i] != '.' && ++check[1][board[j][i]-'1'] > 1) return false;

                row = j/3 + 3*(i/3);
                col = j%3 + 3*(i%3);
                if (board[row][col] != '.' && ++check[2][board[row][col]-'1'] > 1) return false;
            }

            for (int k = 0; k < 3; k++)
                check[k].assign(9, 0);
        }
        return true;
    }
};