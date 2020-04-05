#if 1 //one-loop solution
//Time:O(n)
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int left = 0;
        int n = nums.size();
        for (int i = 0; i < n; i++)
        {
            if (nums[i])
                swap(nums[i], nums[left++]);
        }
    }
};
#else
//https://leetcode.com/discuss/58982/c-two-pointers
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int pos = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            if (nums[i])
            {
                nums[pos] = nums[i];
                pos++;
            }
        }

        while (pos < nums.size())
            nums[pos++] = 0;
    }
};
#endif