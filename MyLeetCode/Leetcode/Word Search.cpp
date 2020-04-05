//https://leetcode.com/discuss/30514/accepted-c-code-with-dfs
class Solution {
public:
    bool search(vector<vector<char>>& board, string word, int start, int row, int col)
    {
        int max_row = board.size() - 1;
        int max_col = board[0].size() - 1;

        if (start == word.size())
            return true;

        if (row < 0 || row > max_row || col < 0 || col > max_col)
            return false;

        char org_c = board[row][col];
        if (board[row][col] == word[start])
        {
            board[row][col] = 0;
            if (search(board, word, start+1, row, col+1)
                || search(board, word, start+1, row, col-1)
                || search(board, word, start+1, row+1, col)
                || search(board, word, start+1, row-1, col))
                return true;
        }
        board[row][col] = org_c;
        return false;
    }

    bool exist(vector<vector<char>>& board, string word) {

        if (board.size() == 0) return false;

        int r = board.size();
        int c = board[0].size();

        for (int i = 0; i < r; i++)
            for (int j = 0; j < c; j++)
                if (search(board, word, 0, i, j))
                    return true;
        return false;
    }
};