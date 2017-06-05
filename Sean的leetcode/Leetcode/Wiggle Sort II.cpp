 //https://discuss.leetcode.com/topic/32929/o-n-o-1-after-median-virtual-indexing
//Time:O(n)
//Space:O(1)
class Solution {
public:
    void wiggleSort(vector<int>& nums) {
        int n = nums.size();
        
        auto midptr = nums.begin() + n / 2;
        nth_element(nums.begin(), midptr, nums.end());
        int mid = *midptr;
        #define A(i) nums[(2 * i + 1) % (n | 1)]
        int l = 0, r = n-1;
        int i = 0;
        while (i <= r) {
            if (A(i) > mid) {
                swap(A(i++), A(l++));
            }
            else if (A(i) < mid) {
                swap(A(i), A(r--));
            }
            else{
                i++;
            }
        }
    }
};