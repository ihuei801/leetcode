class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        int min_diff_sum = INT_MAX;
        int min_diff = INT_MAX;
        int n = nums.size();

        sort(nums.begin(), nums.end());

        for (int i = 0; i < n - 2; i++)
        {
            for (int left = i + 1, right = n - 1; left < right;)
            {
                int sum = nums[i] + nums[left] + nums[right];

                if (abs(sum - target) < min_diff)
                {
                    min_diff = abs(sum - target);
                    min_diff_sum = sum;
                }

                if (sum == target)
                    return sum;
                else if (sum > target)
                    right--;
                else
                    left++;
            }
            while (i + 1 < n - 2 && nums[i+1] == nums[i])
                i++;
        }
        return min_diff_sum;
    }
};