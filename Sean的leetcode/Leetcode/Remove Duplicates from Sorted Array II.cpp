class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (!nums.size()) return 0;

        int k = 0;
        int count = 1;
        for (int i = 1; i < nums.size(); i++)
        {
            if (nums[i] != nums[k])
            {
                nums[++k] = nums[i];
                count = 1;
            }
            else
            {
                if (count == 1)
                {
                    nums[++k] = nums[i];
                    count = 2;
                }
            }
        }
        return k+1;
    }
};