class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        vector<int> one_sol;
        vector<vector<int> >res;
        int n = nums.size();


        for (int i = 0; i < n-3;)
        {
            for (int j = i+1; j < n-2;)
            {
                for (int left = j+1, right = n-1; left < right;)
                {
                    int sum = nums[i] + nums[j] + nums[left] + nums[right];

                    if (sum < target)
                        left++;
                    else if (sum > target)
                        right--;
                    else
                    {
                        one_sol.push_back(nums[i]);
                        one_sol.push_back(nums[j]);
                        one_sol.push_back(nums[left]);
                        one_sol.push_back(nums[right]);
                        res.push_back(one_sol);
                        one_sol.clear();
                        left++, right--;

                        while (left < right && nums[left] == nums[left-1])
                            left++;
                        while (left < right && nums[right] == nums[right+1])
                            right--;
                    }
                }
                j++;
                while (j < n - 2 && nums[j] == nums[j-1])
                    j++;
            }
            i++;
            while (i < n - 3 && nums[i] == nums[i-1])
                i++;
        }
        return res;
    }
};