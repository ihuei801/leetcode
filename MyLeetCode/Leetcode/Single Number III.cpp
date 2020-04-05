//https://leetcode.com/discuss/53150/solution-time-space-understaning-with-simple-explanation
class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        vector<int>res;
        int group_a = 0, group_b = 0;
        int xor_res = 0;

        for (auto n : nums)
            xor_res ^= n;

        //get rightmost bit whose value is 1. bit "1" in xor_res means two numbers diff on this bit.
        //so, use this bit to categorize all numbers into 2 groups.
        int last_diff_bit = (xor_res & (xor_res - 1)) ^ xor_res;

        for (auto n : nums)
        {
            if (n & last_diff_bit)
                group_a ^= n;
            else
                group_b ^= n;
        }
        res.push_back(group_a);
        res.push_back(group_b);
        return res;
    }
};