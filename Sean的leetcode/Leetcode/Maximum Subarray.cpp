//refer http://fisherlei.blogspot.com/2012/12/leetcode-maximum-subarray.html
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int max_sum = INT_MIN;
        int curr_max = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            curr_max = max(nums[i], curr_max+nums[i]);
            max_sum = max(max_sum, curr_max);
        }
        return max_sum;
    }
};