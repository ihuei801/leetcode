/*
 * DP:use a 2D array to memorize the result
 * amount[left][right] : the largest amount we can earn when burn a ballon that leftside is left and rightside is right
 * O(n^3)
 */
class Solution {
public:
    int maxCoins(vector<int>& nums) {
        int size = nums.size();
        int n = size + 2;
        vector<int> ballons(n);
        for (int i = 0; i < size; i++) {
            ballons[i+1] = nums[i];
        }
        ballons[0] = ballons[n - 1] = 1;
        vector<vector<int>> mem(n, vector<int>(n));
        for(int right = 2; right < n; right++) {
            for (int left = right - 1; left >= 0; left--) {
                for (int i = left + 1; i < right; i++){
                    mem[left][right] = max(mem[left][right], ballons[i] * ballons[left] * ballons[right] + mem[left][i] + mem[i][right]);
                }
                
            }
        }
        return mem[0][n-1];
    }
    
};