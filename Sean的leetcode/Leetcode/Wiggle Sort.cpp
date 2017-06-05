//https://leetcode.com/discuss/57341/c-solution-with-o-n-time-and-o-1-space-and-easy-to-understand
//http://www.cnblogs.com/easonliu/p/4798814.html
//Time: O(n), Space: O(1)
class Solution {
public:
    void wiggleSort(vector<int>& nums) {
        if(nums.size() <= 1)
            return ;
        int n = nums.size();
        for(int i = 1; i < n; i += 2){
            //compare with left neighbor
            if(nums[i - 1] > nums[i])
                swap(nums[i - 1], nums[i]);
            //compare with right neighbor
            if(i + 1 < n && nums[i + 1] > nums[i])
                swap(nums[i + 1], nums[i]);
        }
        return ;
    }
};