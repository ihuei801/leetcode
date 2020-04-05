/* DP
 * use element in nums as the last element of combination, so the number = res[i - n]
 * the number of combination is the sum of the number of all possible last elements
 * for example:
 * nums = [1, 2, 3] target = 4
 *    1        2          3          4
 *   (1)   (1  , 1)   (1,1,   1)   (1,1,1,   1)
 *         (2)        (2,     1)   (2,1,     1)
 *                    (1,     2)   (1,2      1)
 *                    (3)          (3,       1)
 *                                 (1,1,     2)
 *                                 (2,       2)
 *                                 (1,       3)
 */
class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        vector<int> res(target + 1);
        for (int i = 1; i <= target; i++) {
            for (int n : nums) {
                if (n > i) break;
                else if (n == i) {
                    res[i]++;
                }
                else{
                    res[i] += res[i - n];
                }
            }
        }
        return res[target];
    }
};