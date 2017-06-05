//https://leetcode.com/discuss/38337/my-15-line-c-code-0ms-runtime-for-test-data
class Solution {
public:
    /* 1. consider 2 cases: A. choose nums[0] and not choose nums[n-1]
                            B. not choose nums[0] and choose nums[n-1]
       2. choose the max(A, B)
    */
    int rob(vector<int>& nums) {
        if (nums.size() == 1) return nums[0];

        return max(find_max(nums, 0, nums.size()-2), find_max(nums, 1, nums.size()-1));
    }

private:
    int find_max(vector<int> &nums, int start, int end)
    {
        int last1 = 0; //the sum from index 0 to i-1
        int last2 = 0; //the sum from index 0 to i-2
        for (int i = start; i <= end; i++)
        {
            last2 = max(last1, last2 + nums[i]);
            swap(last1, last2);
        }
        return max(last1, last2);
    }
};