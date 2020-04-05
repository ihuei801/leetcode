//https://oj.leetcode.com/discuss/17789/binary-search-solution
class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int n = nums.size();
        if (n == 0) return -1;
        int l = 0;
        int r = n-1;
        while(l+1 < r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] > nums[mid-1] && nums[mid] > nums[mid+1]) {
                return mid;
            }
            else if(nums[mid] < nums[mid+1]) {
                l = mid;
            }
            else {
                r = mid;
            }
        }
        return nums[l] > nums[r]? l : r;
    }
};
//Sean's solution
class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int n = nums.size();
        int left = 0;
        int right = n - 1;

        if (n == 0) return -1;
        if (n == 1) return 0;
        if (nums[0] > nums[1]) return 0;
        if (nums[n-1] > nums[n-2]) return n-1;

        while (left <= right)
        {
            int mid = (left + right) >> 1;
            if (nums[mid-1] < nums[mid] && nums[mid] > nums[mid+1])
                return mid;
            //move to the larger one number
            else if (nums[mid-1] > nums[mid])
                right = mid-1;
            else
                left = mid+1;
        }
    }
};