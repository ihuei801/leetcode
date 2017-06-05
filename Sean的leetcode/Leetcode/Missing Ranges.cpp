class Solution {
public:
    vector<string> findMissingRanges(vector<int>& nums, int lower, int upper) {
        vector<string> res;
        int pre = lower - 1;
        int n = nums.size();

        //note: i is from 0 to n
        for (int i = 0; i <= n; i++)
        {
            int curr = i < n ? nums[i] : upper + 1;

            if (curr == pre + 2)
                res.push_back(to_string(pre+1));
            else if (curr > pre + 2)
                res.push_back(to_string(pre+1)+"->"+to_string(curr-1));
            pre = curr;
        }
        return res;
    }
};