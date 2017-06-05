class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int count = 0;
        int curr;
        for (int i = 0; i < nums.size(); i++)
        {
            if (count > 0)
            {
                if (curr == nums[i])
                    count++;
                else
                    count--;
            }
            else
            {
                curr = nums[i];
                count = 1;
            }
        }
        return curr;
    }
};