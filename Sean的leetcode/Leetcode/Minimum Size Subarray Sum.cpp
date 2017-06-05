class Solution {
public:
    int minSubArrayLen(int s, vector<int>& nums) {
        int min_len = INT_MAX;
        int sum = 0;
        for (int left = 0, right = 0; right < nums.size(); right++)
        {
            sum += nums[right];
            while (sum >= s)
            {
                min_len = min(min_len, right - left + 1);
                sum -= nums[left++];
            }
        }
        return min_len == INT_MAX ? 0 : min_len;
    }
};