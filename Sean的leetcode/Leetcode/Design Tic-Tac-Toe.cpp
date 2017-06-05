//Time: O(1) Space:O(n)
class TicTacToe {
public:
    /** Initialize your data structure here. */
    TicTacToe(int n):rows(n), cols(n), diag(0), antidiag(0), total(n){}
    
    /** Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins. */
    int move(int row, int col, int player) {
        int add = player == 1 ? 1 : -1;
        rows[row] += add;
        cols[col] += add;
        diag += row == col ? add : 0;
        antidiag += row == total - 1 - col ? add : 0;
        if(abs(rows[row]) == total || abs(cols[col]) == total || abs(diag) == total || abs(antidiag) == total){
            return player;
        }
        return 0;
    }
private:
    vector<int> rows;
    vector<int> cols;
    int diag;
    int antidiag;
    int total;
};

/**
 * Your TicTacToe object will be instantiated and called as such:
 * TicTacToe obj = new TicTacToe(n);
 * int param_1 = obj.move(row,col,player);
 */