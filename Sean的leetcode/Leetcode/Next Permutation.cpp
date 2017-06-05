class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int n = nums.size();
        if (n <= 1) return;
        int l = n - 1, r = n - 1;
        while (l > 0 && nums[l-1] >= nums[l]) {
            l--;
        }
        int i = l - 1;
        while (l < r) {
            swap(nums[l++], nums[r--]);
        }
        if (i >= 0) {
            int j = i + 1;
            while (j < n && nums[j] <= nums[i]) {
                j++;
            }
            swap(nums[i], nums[j]);
        }
        
    }
};
//Sean's solution
//https://leetcode.com/discuss/47076/1-4-11-lines-c
class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int left = nums.size() - 1;
        int right = left;
        int i, j;
        while (left > 0 && nums[left-1] >= nums[left])
            left--;

        i = left;
        while (left < right)
            swap(nums[left++], nums[right--]);

        if (i > 0)
        {
            j = i;
            i--;
            while (nums[j] <= nums[i])
                j++;
            swap(nums[i], nums[j]);
        }
    }
};