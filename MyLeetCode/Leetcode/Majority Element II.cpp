//https://leetcode.com/discuss/42769/o-n-time-and-in-o-1-space-c-solution
//At most two numbers are more than 1/3 (> 1/3) because at most 3 numbers in "= 1/3" condition.
class Solution {
public:

    bool isOverOneThird(vector<int>& nums, int n)
    {
        int count = 0;
        for (auto a : nums)
            count += n == a;
        return count > nums.size() / 3;
    }

    vector<int> majorityElement(vector<int>& nums) {
        vector<int> res;
        int count[2] = {0};
        int m[2];

        for (int i = 0; i < nums.size(); i++)
        {
            //note: "if, else-if" order cannot change
            if (count[0] && m[0] == nums[i])
                count[0]++;
            else if (count[1] && m[1] == nums[i])
                count[1]++;
            else if (count[0] == 0 || count[1] == 0)
            {
                int j = count[0] == 0 ? 0 : 1;
                m[j] = nums[i];
                count[j] = 1;
            }
            else
                count[0]--,count[1]--;
        }

        for (int i = 0; i < 2; i++)
        {
            if (count[i] && isOverOneThird(nums, m[i]))
                res.push_back(m[i]);
        }
        return res;
    }
};