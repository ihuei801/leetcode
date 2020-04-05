/* DP
 * consider inserting the num as the last number
 */
class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        int n = nums.size();
        if (n == 0) return 0;
        vector<int> dp(target+1);
        sort(nums.begin(), nums.end());
        dp[0] = 1;
        for (int i = 1; i <= target; i++) {
            for (int j = 0; j < n && nums[j] <= i; j++) {
                dp[i] += dp[i - nums[j]];
            }
        }
        return dp[target];
    }
};
 
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