//http://fisherlei.blogspot.tw/2012/12/leetcode-first-missing-positive.html
/*
The answer is positive integer. So, arrange the original array to A[0]=1, A[1]=2,... A[i]=i+1

[-2, -1, 0, 5, 6] => answer: 1
[-2, 0, 1, 5, 8] => answer: 2
*/
class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int n = nums.size();
        int i;
        for (int i = 0; i < n; i++)
        {
            //0 <= nums[i] - 1 < n, if nums[i]-1 is valid index, make nums[nums[i]-1] == nums[i]
            while (nums[i] >= 1 && nums[i] - 1 < n && nums[i] != nums[nums[i]-1])
                swap(nums[i], nums[nums[i]-1]);
        }

        for (i = 0; i < n; i++)
            if (nums[i] != i+1)
                return i+1;
        return i+1;
    }
};