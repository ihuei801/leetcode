class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, int>n_map;

        for (int i = 0; i < nums.size(); i++)
        {
            if (n_map.count(nums[i]))
                return true;
            n_map[nums[i]] = i;
        }
        return false;
    }
};