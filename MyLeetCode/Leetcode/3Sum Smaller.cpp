//https://leetcode.com/discuss/52442/o-n-2-c-solution
class Solution {
public:
    int threeSumSmaller(vector<int>& nums, int target) {
        int n = nums.size();
        if (n < 3) return 0;
        sort(nums.begin(), nums.end());
        int count = 0;
        for (int i = 0; i < n - 2; i++) {
            int left = i + 1;
            int right = n - 1;
            while(left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                if (sum >= target) {
                    right--;
                }
                else {
                    count += right - left;
                    left++;
                }
            }
        }
        return count;
    }
};
//Sean's solution
class Solution {
public:
    int threeSumSmaller(vector<int>& nums, int target) {

        sort(nums.begin(),nums.end());

        int count = 0;
        for (int i = 0; i < n - 2; i++)
            for (int j = i+1, k = n-1; j < k;)
            {
                if (nums[i] + nums[j] + nums[k] >= target)
                    k--;
                else
                {
                    count += k - j;
                    j++;
                }
            }
        return count;
    }
};