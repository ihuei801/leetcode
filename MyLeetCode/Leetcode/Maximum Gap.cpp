//https://leetcode.com/discuss/19100/o-n-c-solution-in-20ms-and-explanation
//https://leetcode.com/discuss/36502/my-concise-and-short-c-code-with-comment-explanation
//Time: O(n), Space: O(n)
class Solution {
public:
    int maximumGap(vector<int>& nums) {

        int n = nums.size();
        if (n < 2) return 0;

        int max_value = *max_element(nums.begin(), nums.end());
        int min_value = *min_element(nums.begin(), nums.end());

        int max_diff = max_value - min_value;

        if (max_diff <= 1) return max_diff;

        int bucket_size = max(1, max_diff / (n - 1));
        int bucket_num = max_diff / bucket_size + 1;

        vector<int>bucket_min (bucket_num, INT_MAX);
        vector<int>bucket_max (bucket_num, INT_MIN);

        for (int i = 0; i < n; i++)
        {
            int idx = (nums[i] - min_value) / bucket_size;
            bucket_min[idx] = min(bucket_min[idx], nums[i]);
            bucket_max[idx] = max(bucket_max[idx], nums[i]);
        }

        //bucket_max[0] is always not INT_MIN because min_value exists.
        int pre_max = bucket_max[0];
        int max_gap = INT_MIN;
        for (int i = 1; i < bucket_num; i++)
        {
            if (bucket_max[i] == INT_MIN)
                continue;

            max_gap = max(max_gap, bucket_min[i] - pre_max);
            pre_max = bucket_max[i];
        }
        return max_gap;
    }
};