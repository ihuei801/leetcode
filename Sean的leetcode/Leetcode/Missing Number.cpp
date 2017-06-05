//https://leetcode.com/discuss/53802/c-solution-using-bit-manipulation
//     i:     0, 1, 2
// nums[i]:   0, 1, 3
// nums.size(): 3
// XOR all above numbers can get 2.
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int res = nums.size();
        for (int i = 0; i < nums.size(); i++)
        {
            res ^= nums[i];
            res ^= i;
        }
        return res;
    }
};