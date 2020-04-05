/*
amount[i][j]:money that need to guarantee a win in range(i,j)
set a l and h boundary and pick every number between l and h to calculate the money needed
Time complexity:O(n^2)
*/
// Forward declaration of guess API.
// @param num, your guess
// @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
class Solution {
public:
    int getMoneyAmount(int n) {
        vector<vector<int>> amount(n+1, vector<int>(n+1));
        for (int h = 2; h <= n; h++) {
            for (int l = h-1; l > 0; l--) {
                int globalmin = INT_MAX;
                for (int k = l; k <= h; k++) {
                    int local;
                    if (k == l) {
                        local = k + amount[k+1][h];
                    }
                    else if (k == h) {
                        local = k + amount[l][k-1];
                    }
                    else {
                        local = k + max(amount[l][k-1], amount[k+1][h]);
                    }
                    globalmin = min(globalmin, local);
                }
                amount[l][h] = globalmin;
            }
        }
        return amount[1][n];
    }
};