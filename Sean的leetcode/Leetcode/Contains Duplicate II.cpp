class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map<int, int>n_map;

        for (int i = 0; i < nums.size(); i++)
        {
            if (n_map.count(nums[i]))
            {
                if (abs(n_map[nums[i]] - i) <= k)
                    return true;
            }
            //note: we should update map in each iteration because duplicate number may appear in the larger index.
            n_map[nums[i]] = i;
        }
        return false;
    }
};