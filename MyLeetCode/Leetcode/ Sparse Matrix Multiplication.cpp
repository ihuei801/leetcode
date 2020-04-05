/* For brute force solution, for each C[ i ] [ j ], it uses C[ i ] [ j ] += A[ i ] [ k ] * B[ k ] [ j ] where k = [ 0, n].
 * Note: even A[ i ] [ k ] or B[ k ] [ j ] is 0, the multiplication is still executed.
 * For the above smart solution, if A[ i ] [ k ] == 0 or B[ k ] [ j ] == 0, it just skip the multiplication . 
 * This is achieved by moving for-loop" for ( k = 0; k < n; k++ ) " from inner-most loop to middle loop, 
 * so that we can use if-statement to tell whether A[ i ] [ k ] == 0 or B[ k ] [ j ] == 0. This is really smart.
 */
class Solution {
public:
    vector<vector<int>> multiply(vector<vector<int>>& A, vector<vector<int>>& B) {
        int r = A.size(), c = B[0].size();
        int n = A[0].size();
        vector<vector<int>> res(r, vector<int>(c));
        for (int i = 0; i < r; i++) {
            for (int k = 0; k < n; k++) {
                if (A[i][k]) {
                    for (int j = 0; j < c; j++) {
                        if (B[k][j]) {
                            res[i][j] += A[i][k] * B[k][j];
                        }
                    }
                }
            }
        }
        return res;
    }
};