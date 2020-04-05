class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        vector<string> res;
        int size = nums.size();
        if (size == 0) return res;
        int start = nums[0];
        for (int i = 0; i < size; i++) {
            if (i == size - 1 || nums[i+1] != nums[i] + 1) {
                if (start == nums[i]) {
                    res.push_back(to_string(start));
                }
                else {
                    res.push_back(to_string(start) + "->" + to_string(nums[i]));
                }
                if (i != size - 1) {
                    start = nums[i+1];
                }
            }
        }
        return res;
    }
};