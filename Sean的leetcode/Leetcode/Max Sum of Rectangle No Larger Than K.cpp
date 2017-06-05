/* Use a left bound and a right bound to build the col range
 * sums:  accumulate sum for the row
 * after we have accumulate sum for rows, we can calculate the sum of rectangle by accumulate sum of cols
 * because sum <= k, accu[j] - accu[i] <= k, accu[i] >= accu[j] - k for j > i
 * therefore, use binary search to find the lower bound of accu[i]
 * Ref:https://discuss.leetcode.com/topic/48875/accepted-c-codes-with-explanation-and-references/2
 */
class Solution {
public:
    int maxSumSubmatrix(vector<vector<int>>& matrix, int k) {
        int rows = matrix.size();
        int cols = rows? matrix[0].size() : 0;
        if (!rows || !cols) return 0;
        int res = INT_MIN;
        for (int l = 0; l < cols; l++) {
            vector<int> sums(rows);
            for (int r = l; r < cols; r++) {
                for (int i = 0; i < rows; i++) {
                    sums[i] += matrix[i][r];
                }
                
                set<int> accu;
                int cur_max = INT_MIN;
                int cur_sum = 0;
                accu.insert(0);
                for (int i = 0; i < rows; i++) {
                    cur_sum += sums[i];
                    auto it = accu.lower_bound(cur_sum - k);
                    if (it != accu.end()) {
                        cur_max = max(cur_max, cur_sum - *it);
                    }
                    accu.insert(cur_sum);
                }
                res = max(res, cur_max);
            }
        }
        return res;
    }
};