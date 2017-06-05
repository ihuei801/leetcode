class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int> >res;
        vector<int>one_sol;
        int n = nums.size();
        int right = nums.size() - 1;

        sort(nums.begin(), nums.end());

        for (int i = 0 ; i < n - 2;)
        {
            one_sol.push_back(nums[i]);
            for (int left = i + 1, right = n - 1; left < right;)
            {
                int sum = nums[i] + nums[left] + nums[right];
                if (sum > 0)
                    right--;
                else if (sum < 0)
                    left++;
                else
                {
                    one_sol.push_back(nums[left]);
                    one_sol.push_back(nums[right]);
                    res.push_back(one_sol);
                    one_sol.pop_back();
                    one_sol.pop_back();

                    left++, right--;
                    while (left < right && nums[left] == nums[left-1])
                        left++;

                    while (left < right && nums[right] == nums[right+1])
                        right--;
                }
            }
            one_sol.pop_back();
            i++;
            while (i < n - 2  && nums[i-1] == nums[i])
                i++;
        }
        return res;
    }
};