//refer http://blog.csdn.net/worldwindjp/article/details/39826823
class Solution {
public:
    int maxProduct(vector<int>& nums) {

        if (nums.size() == 0) return INT_MIN;

        int curr_max = nums[0];
        int curr_min = nums[0];
        int max_val = nums[0];
        for (int i = 1; i < nums.size(); i++)
        {
            int M = curr_max * nums[i];
            int m = curr_min * nums[i];
            curr_max = max(nums[i], max(M, m));
            curr_min = min(nums[i], min(M, m));
            max_val = max(max_val, curr_max);
        }
        return max_val;
    }
};